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

DOCUMENTATION = '''
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
options:
    username:
        description:
            - Password associated with to download a product from the JBoss Network API.
            - If value not set, will try environment variable C(REDHAT_PRODUCT_DOWNLOAD_USERNAME)
        type: str
        required: true
    password:
        description:
            - Password associated with to download a product from the JBoss Network API.
            - If value not set, will try environment variable C(REDHAT_PRODUCT_DOWNLOAD_PASSWORD)
        type: str
        required: true
    api_url:
        description:
            - Address of the JBoss Network API.
        type: str
        required: false
    sso_url:
        description:
            - Address of the Red Hat SSO Server.
        type: str
        required: false
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

    product_category:
        description:
            - Product Category to download.
        type: str
        required: false
    product_id:
        description:
            - Product ID to download.
        type: int
        required: false
    product_type:
        description:
            - Product type to Download.
        type: str
        required: false
    product_version:
        description:
            - Version of the product to download.
        type: str
        required: false
    validate_certs:
        description:
        - If C(false), SSL certificates will not be validated.
        type: bool
        default: yes
        required: false
'''


EXAMPLES = '''
- name: Download Red Hat Product
  product_download:
    username: foo@example.com
    password: bar
    dest: /tmp/eap-connectors.zip
'''

import traceback
import os
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import missing_required_lib
from ansible.module_utils._text import to_native

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    REQUESTS_IMP_ERR = traceback.format_exc()

JBOSS_NETWORK_API_URL = "https://jbossnetwork.api.redhat.com"
REDHAT_SSO_URL = "https://sso.redhat.com"
REDHAT_PRODUCT_DOWNLOAD_USERNAME_ENV_VAR = "REDHAT_PRODUCT_DOWNLOAD_USERNAME"
REDHAT_PRODUCT_DOWNLOAD_PASSWORD_ENV_VAR = "REDHAT_PRODUCT_DOWNLOAD_PASSWORD"

DEFAULT_SCOPE = "openid api.iam.service_accounts"
API_SERVICE_PATH = "/v1/middleware"
LIST_PRODUCT_CATEGORIES_ENDPOINT = "/list/categories"
SEARCH_ENDPOINT = "/search"
QUERY_PAGE_SIZE = 100
TOTAL_RECORDS_FIELD = "total_records"
NEXT_CURSOR_FIELD = "nextCursor"
RESULTS_FIELD = "results"

#DEFAULT_PRODUCT_TYPE = "DISTRIBUTION"

SEARCH_ENDPOINT = "/search"
SEARCH_PARAM_ID = "id"
SEARCH_PARAM_NAME = "name"
SEARCH_PARAM_VERSION = "version"
SEARCH_PARAM_CATEGORY = "category"
SEARCH_PARAM_TYPE = "type"


def performSerach(session, url, validate_certs, params={}):

    nextCursor = None
    results = []

    while True:

        pagination_params = {}

        # Provide parameters
        if nextCursor is not None:
            pagination_params.update({"cursor": nextCursor})
            params.pop("pageSize", None)
        else:
            pagination_params.update({"pageSize": QUERY_PAGE_SIZE})
            params.pop("cursor", None)

        params.update(pagination_params)

        query_request = session.get(url, params=params, verify=validate_certs)
        query_request.raise_for_status()

        query_result_json = query_request.json()

        results.extend(
            query_result_json[RESULTS_FIELD])
        
        if NEXT_CURSOR_FIELD not in query_result_json or query_result_json[NEXT_CURSOR_FIELD] is None:
            break

        nextCursor = query_result_json[NEXT_CURSOR_FIELD]

    return results



def main():
    module = AnsibleModule(
        argument_spec=dict(
            username=dict(required=False),
            password=dict(no_log=True, required=False),
            api_url=dict(required=False, default=JBOSS_NETWORK_API_URL),
            sso_url=dict(required=False, default=REDHAT_SSO_URL),
            dest=dict(required=True),
            product_id=dict(required=False),
            product_category=dict(required=False),
            product_type=dict(required=False),
            product_version=dict(required=False),
            validate_certs=dict(required=False,default=True, type=bool),
            force=dict(required=False,default=False, type=bool)

        ),
        add_file_common_args=True
    )

    if not HAS_REQUESTS:
        module.fail_json(msg=missing_required_lib("requests"), exception=REQUESTS_IMP_ERR)
    
    username = module.params.get('username')
    password = module.params.get('password')
    api_url = module.params.get('api_url')
    sso_url = module.params.get('sso_url')
    dest = module.params.get('dest')
    product_id = module.params.get('product_id')
    product_category = module.params.get('product_category')
    product_type = module.params.get('product_type')
    product_version = module.params.get('product_version')
    validate_certs = module.params.get('validate_certs')
    force = module.params.get('force')

    if not username:
        username = os.environ.get(REDHAT_PRODUCT_DOWNLOAD_USERNAME_ENV_VAR)

    if not username:
        module.fail_json(msg=str(f"Username not specified and unable to determine username from '{REDHAT_PRODUCT_DOWNLOAD_USERNAME_ENV_VAR}' environment variable."))

    if not password:
        password = os.environ.get(REDHAT_PRODUCT_DOWNLOAD_PASSWORD_ENV_VAR)

    if not password:
        module.fail_json(msg=str(f"Password not specified and unable to determine password from '{REDHAT_PRODUCT_DOWNLOAD_PASSWORD_ENV_VAR}' environment variable."))

    if not dest:
        module.fail_json(msg=str("Destination path not provided"))

    # if not product_id:
    #     module.fail_json(msg=str("Product ID must be provided"))

    token_request_data = {
        "client_id": username,
        "client_secret": password,
        "scope": DEFAULT_SCOPE,
        "grant_type": "client_credentials",
    }


    # Obtain Access Token
    token_request = requests.post(
        f"{sso_url}/auth/realms/redhat-external/protocol/openid-connect/token",
        data=token_request_data, verify=validate_certs)

    try:
        token_request.raise_for_status()
    except Exception as err:
        module.fail_json(msg="Error Retrieving SSO Access Token: %s" % (to_native(err)))

    access_token = token_request.json()["access_token"]

    # Setup Session
    session = requests.Session()
    session.headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    api_base_url = f"{api_url}{API_SERVICE_PATH}"

    # List Product Categories
    product_categories = []

    try:
        product_categories = performSerach(session, f"{api_base_url}{LIST_PRODUCT_CATEGORIES_ENDPOINT}",validate_certs)
    except Exception as err:
        module.fail_json(msg="Error Listing Available Product Categories: %s" % (to_native(err)))

    if product_category is not None and product_category not in product_categories:
        module.fail_json(msg=f"'{product_category}' is not a valid Product Category")

    # Search for Products
    search_results = []

    search_params = {
        SEARCH_PARAM_CATEGORY: product_category,
        SEARCH_PARAM_TYPE: product_type,
        SEARCH_PARAM_VERSION: product_version,
        SEARCH_PARAM_ID: product_id,
        # Not Implemented
        SEARCH_PARAM_NAME: None,
    }

    try:
        search_results = performSerach(session, f"{api_base_url}{SEARCH_ENDPOINT}", validate_certs,search_params)
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
