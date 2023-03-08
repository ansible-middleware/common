from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r"""
options:
  api_url:
      description:
          - Address of the JBoss Network API.
      type: str
      required: false
      default: 'https://jbossnetwork.api.redhat.com'
  client_id:
      description:
          - Client ID associated with to download a product from the JBoss Network API.
          - If value not set, will try environment variable C(REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID)
      type: str
      required: false
  client_secret:
      description:
          - Client Secret associated with to download a product from the JBoss Network API.
          - If value not set, will try environment variable C(REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET)
      type: str
      required: false
  sso_url:
      description:
          - Address of the Red Hat SSO Server.
      type: str
      required: false
      default: 'https://sso.redhat.com'
  validate_certs:
      description:
      - If C(false), SSL certificates will not be validated.
      type: bool
      default: yes
      required: false
  product_category:
      description:
          - Type of the Product Category
      type: str
      required: false
  product_id:
      description:
      - Product Id for the Redhat customer portal
      type: str
      required: false
  product_type:
      description:
          - Type of the Product
      type: str
      required: false
  product_version:
      description:
      - Product Version to be downloaded.
      type: str
      required: false

"""
