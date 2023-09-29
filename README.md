# Ansible Collection - Common
<!--start build_status -->
[![Build Status](https://github.com/ansible-middleware/common/workflows/CI/badge.svg?branch=main)](https://github.com/ansible-middleware/common/actions/workflows/ci.yml)
<!--end build_status -->
## About

Collection containing common utilities to support Ansible Middleware automation

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

## Python version compatibility

This collection has been tested against following Python versions: **>=3.6**.

<!--end requires_ansible-->


## Included content

### Modules

* `product_download`: downloads products from the JBoss Network API
* `product_search`: searches products from the JBoss Network API
* `xml`: manage bits and pieces of XML files or strings

### Filters

* `version_sort`: sort a list of strings according to version ordering


## Installation

<!--start galaxy_download -->
### Download from galaxy

    ansible-galaxy collection install middleware_automation.common
<!--end galaxy_download -->

### Build and install locally

Clone the repository, checkout the tag you want to build, or pick the main branch for the development version; then:

    ansible-galaxy collection build .
    ansible-galaxy collection install middleware_automation-common-*.tar.gz


### Dependencies

#### Python:

* [jmespath](https://jmespath.org/)
* [lxml](https://lxml.de/)

To install all the dependencies via galaxy:

    pip install -r requirements.txt

<!--start support -->
<!--end support -->

## License

[Apache License 2.0](https://github.com/ansible-middleware/common/blob/main/LICENSE)
