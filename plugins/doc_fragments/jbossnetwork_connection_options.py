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
  client_id:
      description:
          - Client ID associated with to download a product from the JBoss Network API.
          - If value not set, will try environment variable C(REDHAT_PRODUCT_DOWNLOAD_CLIENT_ID)
      type: str
      required: true
  client_secret:
      description:
          - Client Secret associated with to download a product from the JBoss Network API.
          - If value not set, will try environment variable C(REDHAT_PRODUCT_DOWNLOAD_CLIENT_SECRET)
      type: str
      required: true
  sso_url:
      description:
          - Address of the Red Hat SSO Server.
      type: str
      required: false
  validate_certs:
      description:
      - If C(false), SSL certificates will not be validated.
      type: bool
      default: yes
      required: false


"""
