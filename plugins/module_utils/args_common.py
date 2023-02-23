from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.middleware_automation.common.plugins.module_utils.constants import (
    JBOSS_NETWORK_API_URL,
    REDHAT_SSO_URL,
)

JBOSS_NETWORK_COMMON_ARGS_SPEC = dict(
    client_id=dict(required=False),
    client_secret=dict(no_log=True, required=False),
    api_url=dict(required=False, default=JBOSS_NETWORK_API_URL),
    sso_url=dict(required=False, default=REDHAT_SSO_URL),
    validate_certs=dict(required=False,default=True, type=bool)
)

JBOSS_NETWORK_SEARCH_ARGS_SPEC = dict(
    product_id=dict(required=False),
    product_category=dict(required=False),
    product_type=dict(required=False),
    product_version=dict(required=False)
)