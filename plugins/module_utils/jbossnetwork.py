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

from ansible_collections.middleware_automation.common.plugins.module_utils.constants import (
    QUERY_LIMIT,
    PAGE_FIELD,
    LIMIT_FIELD,
    TOTAL_PAGES_FIELD,
    DATA_FIELD,
    NEXT_CURSOR_FIELD,
    RESULTS_FIELD,
    DEFAULT_SCOPE,
    SEARCH_PARAM_PRODUCT_CODE,
    SEARCH_PARAM_CONTENT_TYPE,
    SEARCH_PARAM_VERSION,
    SEARCH_PARAM_ID,
    SEARCH_PARAM_NAME
)

import json
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.urls import Request
from urllib.parse import urlencode


def get_authenticated_session(module, sso_url, validate_certs, client_id, client_secret):

    token_request_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": DEFAULT_SCOPE,
        "grant_type": "client_credentials",
    }

    # Initialize Session
    session = Request(validate_certs=validate_certs, headers={})

    try:
        token_request = session.post("{0}/auth/realms/redhat-external/protocol/openid-connect/token".format(sso_url), data=urlencode(token_request_data))

    except Exception as err:
        module.fail_json(msg="Error Retrieving SSO Access Token: %s" % (to_native(err)))

    access_token = json.loads(token_request.read())["access_token"]

    # Setup Session
    session.headers = {
        "Authorization": "Bearer {0}".format(access_token),
        "Content-Type": "application/json",
    }

    return session


def generate_search_params(product_category, product_id, product_type, product_version):
    search_params = {
        SEARCH_PARAM_PRODUCT_CODE: product_category,
        SEARCH_PARAM_CONTENT_TYPE: product_type,
        SEARCH_PARAM_VERSION: product_version,
        SEARCH_PARAM_ID: product_id,
        # Not Implemented
        SEARCH_PARAM_NAME: None,
    }

    return search_params


def perform_search(session, url, validate_certs, params=None):

    page = 1
    results = []

    if params is None:
        params = {}

    while True:

        pagination_params = {
            PAGE_FIELD: page,
            LIMIT_FIELD: QUERY_LIMIT
        }

        params.update(pagination_params)

        full_url = []
        full_url.append(url)

        if len(params) > 0:

            # Remove None Keys
            none_keys = [k for (k, v) in params.items() if v is None]
            for key in none_keys:
                del params[key]

            full_url.append("?")
            full_url.append(urlencode(params))

        query_request = session.get("".join(full_url))

        query_result_json = json.loads(query_request.read())

        if DATA_FIELD in query_result_json:
            results.extend(query_result_json[DATA_FIELD])
        elif RESULTS_FIELD in query_result_json:
            results.extend(query_result_json[RESULTS_FIELD])
        else:
            results.append(query_result_json)

        if TOTAL_PAGES_FIELD in query_result_json:
            total_pages = query_result_json[TOTAL_PAGES_FIELD]
            if page >= total_pages:
                break
        elif NEXT_CURSOR_FIELD in query_result_json and query_result_json[NEXT_CURSOR_FIELD] is None:
            break
        else:
            break

        page += 1

    return results
