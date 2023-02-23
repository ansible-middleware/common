from __future__ import absolute_import, division, print_function

__metaclass__ = type

import requests

from ansible_collections.middleware_automation.common.plugins.module_utils.constants import (
    QUERY_PAGE_SIZE,
    NEXT_CURSOR_FIELD,
    RESULTS_FIELD,
    DEFAULT_SCOPE,
    CURSOR_FIELD,
    PAGE_SIZE_FIELD,
    SEARCH_PARAM_CATEGORY,
    SEARCH_PARAM_TYPE,
    SEARCH_PARAM_VERSION,
    SEARCH_PARAM_ID,
    SEARCH_PARAM_NAME
)

from ansible.module_utils._text import to_native


def get_authenticated_session(module, sso_url, validate_certs, client_id, client_secret):

    token_request_data = {
        "client_id": client_id,
        "client_secret": client_secret,
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

    return session

def generate_search_params(product_category, product_id, product_type, product_version):

    search_params = {
        SEARCH_PARAM_CATEGORY: product_category,
        SEARCH_PARAM_TYPE: product_type,
        SEARCH_PARAM_VERSION: product_version,
        SEARCH_PARAM_ID: product_id,
        # Not Implemented
        SEARCH_PARAM_NAME: None,
    }

    return search_params

def perform_search(session, url, validate_certs, params={}):

    nextCursor = None
    results = []

    while True:

        pagination_params = {}

        # Provide parameters
        if nextCursor is not None:
            pagination_params.update({CURSOR_FIELD: nextCursor})
            params.pop(PAGE_SIZE_FIELD, None)
        else:
            pagination_params.update({PAGE_SIZE_FIELD: QUERY_PAGE_SIZE})
            params.pop(CURSOR_FIELD, None)

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
