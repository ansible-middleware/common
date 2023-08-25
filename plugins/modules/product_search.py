#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright [2023] [Red Hat, Inc.]
#
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
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

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: product_search
author: Andrew Block (@sabre1041)
short_description: Searches products from the JBoss Network API.
description:
    - Searches products from the JBoss Network API.
requirements:
    - requests
extends_documentation_fragment:
    - middleware_automation.common.jbossnetwork_connection_options
"""


EXAMPLES = r"""
- name: Search Red Hat Products
  middleware_automation.common.product_search:
    client_id: 123e4567-e89b-12d3-a456-426614174000
    client_secret: 0mpkY0i8IdIRWbk6rLXBlf5Jkqq8i4nW
    product_category: webserver
    product_version: 5.5
"""

RETURN = r"""
results:
  description:
  - The objects returned from the API
  returned: success
  type: complex
  contains:
    category:
      description: Product category.
      returned: success
      type: str
    description:
      description: Description of the product.
      returned: success
      type: str
    distribution_status:
      description: Distribution status of the product.
      returned: success
      type: str
    download_path:
      description: URL where the product can be downloaded.
      returned: success
      type: str
    id:
      description: id of the product.
      returned: success
      type: int
    md5:
      description: MD5 checksum of the product.
      returned: success
      type: str
    name:
      description: Name of the product.
      returned: success
      type: str
    sha256:
      description: MD5 checksum of the product.
      returned: success
      type: str
    title:
      description: Title of the product.
      returned: success
      type: str
    type:
      description: Type of product.
      returned: success
      type: str
    version:
      description: Product version.
      returned: success
      type: str
    visibility:
      description: Product visibility.
      returned: success
      type: str
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
    requests_version = requests.__version__
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
    REQUESTS_IMP_ERR = traceback.format_exc()
else:
    REQUESTS_IMP_ERR = None


def argspec():
    argument_spec = copy.deepcopy(JBOSS_NETWORK_COMMON_ARGS_SPEC)
    argument_spec.update(copy.deepcopy(JBOSS_NETWORK_SEARCH_ARGS_SPEC))

    return argument_spec


def main():
    module = AnsibleModule(
        argument_spec=argspec(),
        add_file_common_args=False
    )

    if not HAS_REQUESTS:
        module.fail_json(msg=missing_required_lib("requests"), exception=REQUESTS_IMP_ERR)

    client_id = module.params.get('client_id')
    client_secret = module.params.get('client_secret')
    api_url = module.params.get('api_url')
    sso_url = module.params.get('sso_url')
    product_id = module.params.get('product_id')
    product_category = module.params.get('product_category')
    product_type = module.params.get('product_type')
    product_version = module.params.get('product_version')
    validate_certs = module.params.get('validate_certs')

    if not client_id:
        client_id = os.environ.get(REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID_ENV_VAR)

    if not client_id:
        module.fail_json(msg=str("Client ID not specified and unable to determine Client ID "
                                 f"from '{REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID_ENV_VAR}' environment variable."))

    if not client_secret:
        client_secret = os.environ.get(REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET_ENV_VAR)

    if not client_secret:
        module.fail_json(msg=str("Client Secret not specified and unable to determine Client Secret "
                                 f"from '{REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET_ENV_VAR}' environment variable."))

    session = get_authenticated_session(module, sso_url, validate_certs, client_id, client_secret)

    api_base_url = f"{api_url}{API_SERVICE_PATH}"

    if product_category is not None:
        # List Product Categories
        product_categories = []

        try:
            product_categories = perform_search(session, f"{api_base_url}{LIST_PRODUCT_CATEGORIES_ENDPOINT}", validate_certs)
        except Exception as err:
            module.fail_json(msg="Error Listing Available Product Categories: %s" % (to_native(err)))

        if product_category not in product_categories:
            module.fail_json(msg=f"'{product_category}' is not a valid Product Category")

    # Search for Products
    search_results = []

    search_params = generate_search_params(product_category, product_id, product_type, product_version)

    try:
        search_results = perform_search(session, f"{api_base_url}{SEARCH_ENDPOINT}", validate_certs, search_params)
    except Exception as err:
        module.fail_json(msg="Error Searching for Products: %s" % (to_native(err)))

    result = dict(
        changed=False,
        results=search_results
    )

    module.exit_json(msg="", **result)


if __name__ == '__main__':
    main()
