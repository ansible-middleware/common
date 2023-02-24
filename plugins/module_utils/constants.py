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

JBOSS_NETWORK_API_URL = "https://jbossnetwork.api.redhat.com"
REDHAT_SSO_URL = "https://sso.redhat.com"
REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID_ENV_VAR = "REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID"
REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET_ENV_VAR = "REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET"

API_SERVICE_PATH = "/v1/middleware"
LIST_PRODUCT_CATEGORIES_ENDPOINT = "/list/categories"
SEARCH_ENDPOINT = "/search"

QUERY_PAGE_SIZE = 100

CURSOR_FIELD = "cursor"
PAGE_SIZE_FIELD = "pageSize"
NEXT_CURSOR_FIELD = "nextCursor"
RESULTS_FIELD = "results"
DEFAULT_SCOPE = "openid api.iam.service_accounts"

SEARCH_PARAM_ID = "id"
SEARCH_PARAM_NAME = "name"
SEARCH_PARAM_VERSION = "version"
SEARCH_PARAM_CATEGORY = "category"
SEARCH_PARAM_TYPE = "type"
