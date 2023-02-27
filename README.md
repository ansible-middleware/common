# Ansible Collection - Common

[![Build Status](https://github.com/ansible-middleware/common/workflows/CI/badge.svg?branch=main)](https://github.com/ansible-middleware/common/actions/workflows/ci.yml)

## About

Collection containing common utilities to support Ansible Middleware automation

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.
<!--end requires_ansible-->


## Included content

### Modules:

* `product_download`: downloads products from the JBoss Network API
* `product_search`: searches products from the JBoss Network API

## Installation

### Download from galaxy

    ansible-galaxy collection install middleware_automation.common


### Build and install locally

Clone the repository, checkout the tag you want to build, or pick the main branch for the development version; then:

    ansible-galaxy collection build .
    ansible-galaxy collection install middleware_automation-common-*.tar.gz


### Dependencies

#### Python:

* [requests](https://requests.readthedocs.io/en/latest/)

To install all the dependencies via galaxy:

    pip install -r requirements.txt

## Support

The amq collection is a Beta release and for [Technical Preview](https://access.redhat.com/support/offerings/techpreview). If you have any issues or questions related to collection, please don't hesitate to contact us on <Ansible-middleware-core@redhat.com> or open an issue on <https://github.com/ansible-middleware/common/issues>

## License

[Apache License 2.0](https://github.com/ansible-middleware/common/blob/main/LICENSE)
