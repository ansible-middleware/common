# Ansible Collection - Common
<!--start build_status -->
[![Build Status](https://github.com/ansible-middleware/common/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ansible-middleware/common/actions/workflows/ci.yml)
<!--end build_status -->
## About

Collection containing common utilities to support Ansible Middleware automation

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.16.0**.

## Python version compatibility

This collection has been tested against following Python versions: **>=3.12**.

<!--end requires_ansible-->


## Included content

### Modules

* `product_download`: downloads products from the Red Hat Unified Downloads API
* `product_search`: searches products from the Red Hat Unified Downloads API
* `maven_artifact`: downloads an Artifact from a Maven Repository
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


## Support

<!--start support -->

For bug reports and feature requests, use [GitHub Issues](https://github.com/ansible-middleware/common/issues).

<!--end support -->


## Release and Upgrade Notes

For details on changes between versions, please see the [CHANGELOG](https://github.com/ansible-middleware/common/blob/main/CHANGELOG.rst) for this collection.

## License

Apache License v2.0 or later

See [LICENSE](LICENSE) to view the full text.
