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
    JBOSS_NETWORK_API_URL,
    REDHAT_SSO_URL,
)

JBOSS_NETWORK_COMMON_ARGS_SPEC = dict(
    client_id=dict(required=False),
    client_secret=dict(no_log=True, required=False),
    api_url=dict(required=False, default=JBOSS_NETWORK_API_URL),
    sso_url=dict(required=False, default=REDHAT_SSO_URL),
    validate_certs=dict(required=False, default=True, type=bool)
)

JBOSS_NETWORK_SEARCH_ARGS_SPEC = dict(
    product_id=dict(required=False),
    product_category=dict(required=False),
    product_type=dict(required=False),
    product_version=dict(required=False)
)
