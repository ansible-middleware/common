# Copyright [2023] [Red Hat, Inc.]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: product_download
author: Andrew Block (@sabre1041)
short_description: Downloads products from the JBoss Network API.
description:
    - Downloads products from the JBoss Network API.
requirements:
    - requests
extends_documentation_fragment:
    - files
    - middleware_automation.common.jbossnetwork_connection_options
    - middleware_automation.common.jbossnetwork_search_options
options:
    dest:
        description:
            - Absolute  .
        type: path
        required: true
    force:
        description:
        - If C(true) and C(dest) is not a directory, will download the file every
            time and replace the file if the contents change. If C(false), the file
            will only be downloaded if the destination does not exist.
"""


EXAMPLES = r"""
- name: Download Red Hat Product
  middleware_automation.common.product_download:
    client_id: 123e4567-e89b-12d3-a456-426614174000
    client_secret: 0mpkY0i8IdIRWbk6rLXBlf5Jkqq8i4nW
    dest: /tmp/eap-connectors.zip
    product_id: 12345
"""

RETURN = r"""
dest:
    description: destination file/path
    returned: success
    type: str
    sample: /path/to/file.txt
failed:
    description: whether an error occurred downloading the resource
    returned: success
    type: bool
    sample: false
gid:
    description: group id of the file
    returned: success
    type: int
    sample: 100
group:
    description: group of the file
    returned: success
    type: str
    sample: "httpd"
md5sum:
    description: md5 checksum of the file after download
    returned: when supported
    type: str
    sample: "2a5aeecc61dc98c4d780b14b330e3282"
mode:
    description: permissions of the target
    returned: success
    type: str
    sample: "0644"
msg:
    description: the HTTP message from the request
    returned: always
    type: str
    sample: OK (unknown bytes)
owner:
    description: owner of the file
    returned: success
    type: str
    sample: httpd
size:
    description: size of the target
    returned: success
    type: int
    sample: 1220
state:
    description: state of the target
    returned: success
    type: str
    sample: file
uid:
    description: owner id of the file, after execution
    returned: success
    type: int
    sample: 100
"""

import traceback
import os
import copy
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils._text import to_native

from ansible_collections.middleware_automation.common.plugins.module_utils.jbossnetwork import (
    get_authenticated_session,
    generate_search_params,
    perform_search
)

from ansible_collections.middleware_automation.common.plugins.module_utils.args_common import (
    JBOSS_NETWORK_COMMON_ARGS_SPEC,
    JBOSS_NETWORK_SEARCH_ARGS_SPEC
)

from ansible_collections.middleware_automation.common.plugins.module_utils.constants import (
    REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID_ENV_VAR,
    REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET_ENV_VAR,
    API_SERVICE_PATH,
    SEARCH_ENDPOINT,
    LIST_PRODUCT_CATEGORIES_ENDPOINT
)


try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    REQUESTS_IMP_ERR = traceback.format_exc()


def argspec():
    argument_spec = copy.deepcopy(JBOSS_NETWORK_COMMON_ARGS_SPEC)
    argument_spec.update(copy.deepcopy(JBOSS_NETWORK_SEARCH_ARGS_SPEC))
    argument_spec["dest"] = dict(required=True)
    argument_spec["force"] = dict(required=False,default=False, type=bool)

    return argument_spec

def main():
    module = AnsibleModule(
        argument_spec=argspec(),
        add_file_common_args=True
    )

    if not HAS_REQUESTS:
        module.fail_json(msg=missing_required_lib("requests"), exception=REQUESTS_IMP_ERR)
    
    client_id = module.params.get('client_id')
    client_secret = module.params.get('client_secret')
    api_url = module.params.get('api_url')
    sso_url = module.params.get('sso_url')
    dest = module.params.get('dest')
    product_id = module.params.get('product_id')
    product_category = module.params.get('product_category')
    product_type = module.params.get('product_type')
    product_version = module.params.get('product_version')
    validate_certs = module.params.get('validate_certs')
    force = module.params.get('force')

    if not client_id:
        client_id = os.environ.get(REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID_ENV_VAR)

    if not client_id:
        module.fail_json(msg=str(f"Client ID not specified and unable to determine Client ID from '{REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID_ENV_VAR}' environment variable."))

    if not client_secret:
        client_secret = os.environ.get(REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET_ENV_VAR)

    if not client_secret:
        module.fail_json(msg=str(f"Client Secret not specified and unable to determine Client Secret from '{REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET_ENV_VAR}' environment variable."))

    if not dest:
        module.fail_json(msg=str("Destination path not provided"))
    
    session = get_authenticated_session(module, sso_url, validate_certs, client_id, client_secret)

    api_base_url = f"{api_url}{API_SERVICE_PATH}"


    if product_category is not None:
        # List Product Categories
        product_categories = []

        try:
            product_categories = perform_search(session, f"{api_base_url}{LIST_PRODUCT_CATEGORIES_ENDPOINT}",validate_certs)
        except Exception as err:
            module.fail_json(msg="Error Listing Available Product Categories: %s" % (to_native(err)))

        if product_category not in product_categories:
            module.fail_json(msg=f"'{product_category}' is not a valid Product Category")

    # Search for Products
    search_results = []

    search_params = generate_search_params(product_category, product_id, product_type, product_version)

    try:
        search_results = perform_search(session, f"{api_base_url}{SEARCH_ENDPOINT}", validate_certs,search_params)
    except Exception as err:
        module.fail_json(msg="Error Searching for Products: %s" % (to_native(err)))

    products_found = len(search_results)

    # Print error with results if more than 1 exists
    if products_found != 1:
        msg = [
            (f"Error: Unable to locate a single product to download. '{products_found}' products found.")
        ]

        for productIdx, product in enumerate(search_results):
            msg.append(f"{productIdx+1} - ({search_results[productIdx]['id']}) {search_results[productIdx]['title']}.")
        
        module.fail_json(msg=" ".join(msg))
    
    file_name = search_results[0]['file_path'].rsplit('/')[-1]

    dest_is_dir = os.path.isdir(dest)

    if dest_is_dir:
        dest = os.path.join(dest, file_name)

    result = dict(
        changed=False,
        dest=dest
    )


    if os.path.exists(dest) and not force:
        file_args = module.load_file_common_arguments(module.params, path=dest)
        result['changed'] = module.set_fs_attributes_if_different(file_args, False)
         
        if result['changed']:
            module.exit_json(msg="file already exists but file attributes changed", **result)
        module.exit_json(msg="file already exists", **result)

    # check if there is no dest file
    if os.path.exists(dest):
        # raise an error if copy has no permission on dest
        if not os.access(dest, os.W_OK):
            module.fail_json(msg="Destination %s is not writable" % (dest), **result)
        if not os.access(dest, os.R_OK):
            module.fail_json(msg="Destination %s is not readable" % (dest), **result)
        result['checksum'] = module.sha1(dest)
    else:
        if not os.path.exists(os.path.dirname(dest)):
            module.fail_json(msg="Destination %s does not exist" % (os.path.dirname(dest)), **result)
        if not os.access(os.path.dirname(dest), os.W_OK):
            module.fail_json(msg="Destination %s is not writable" % (os.path.dirname(dest)), **result)

    try:
        with session.get(search_results[0]["download_path"], verify=validate_certs, stream=True, allow_redirects=True, headers={"User-Agent": "product_download"}) as r:
            r.raise_for_status()
            with open(dest, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        
        result['changed'] = True
    except Exception as err:
        module.fail_json(msg="Error Downloading %s: %s" % (search_results[0]['title'], to_native(err)))

    file_args = module.load_file_common_arguments(module.params, path=dest)
    result['changed'] = module.set_fs_attributes_if_different(file_args, result['changed'])

    try:
        result['md5sum'] = module.md5(dest)
    except ValueError:
        result['md5sum'] = None
    
    module.exit_json(msg="", **result)


if __name__ == '__main__':
    main()
