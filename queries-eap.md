EAP
===

Use case: 

 * search the installation zip file for EAP x.y
 * download EAP
 * search the most recent cumulative patch for EAP x.y (ie x.y.Z)
 * download the patch


## Search the installation zip

With the following parameters we are looking for main EAP 7.4 release:

    - name: Search EAP Product
      middleware_automation.common.product_search:
        client_id: "{{ client_id }}"
        client_secret: "{{ client_secret }}"
        product_version: 7.4
        product_type: DISTRIBUTION
        product_category: appplatform
      register: product_results


With get the following results (the want the last one):

    "results": [
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Core Source Code",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/4aa5b8821e5126aaa7bef7ef0dc2b74c/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-core-src.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-core-src.zip",
            "id": 99391,
            "md5": "380bf3b3cd48d4ef45de9f3c646fc1d9",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "c00c3f9d66642979dc605cc710704fea086b223cafad45c99df079744d5fa39c",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Core Source Code",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Server Migration Source Code",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/e3c6c61910dd8e372330568cb3717a5c/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-server-migration-src.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-server-migration-src.zip",
            "id": 99411,
            "md5": "c9e87a7bee1f4093aa69d0e76d01dda3",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "66ecc0a02e32cfa205ed63476ded164a72ec1405367277e4222ffe0a3c728142",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Server Migration Source Code",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Source Code",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/0549650c3580122ee441f7dc5b0b0d9b/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-src.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-src.zip",
            "id": 99421,
            "md5": "c040c23e5afa627b2cbc9626127fd8ba",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "7c0500b2f68a9884aa3bd2d17f6fecc83505bffeb647a9c1843ce48eb2c6f766",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Source Code",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Javadocs",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/a95caad9e60d435a55cf011908edb13a/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-javadoc.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-javadoc.zip",
            "id": 99431,
            "md5": "9fadd390242788345609029fba5c6fc6",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "b39ecdf3ed0dd803e85e5113e66896148fac67a80c7e2be8e403cff84c7b0194",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Javadocs",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Maven Repository",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/b471a8e8a3e20ace8eb7e97a33d4c554/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-maven-repository.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-maven-repository.zip",
            "id": 99441,
            "md5": "db3ab61eed51ed367e7fe12df3531fb5",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "3b0658ecf3d4a671e99df8ed6dc4270e75496348f31d26256dfd48603031686b",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Maven Repository",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Maven Repository Offliner Content List",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/ceb51d2cbca88dcc3714cea0b8dbc1b6/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-maven-repository-content-with-sha256-checksums.txt",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-maven-repository-content-with-sha256-checksums.txt",
            "id": 99451,
            "md5": "e135c7768c712fac7810e0b9e3e1d9fb",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "97c7c7a4f1e4130b6a72678cf8a67c0ad38878d099e2912faec3fd2c8e9e9d93",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Maven Repository Offliner Content List",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Quickstarts",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/a0ebf185df17c4cb925757e242a2e3f3/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-quickstarts.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-quickstarts.zip",
            "id": 99461,
            "md5": "d103358dc5d8767f6b2ba16ecc1eb099",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "7f84cd8449365eff8cf114f4bef17533ae2bd10ac3e73a8ee7db3be0e9aa20cb",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Quickstarts",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Installer",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/5574776171c25a019b79fc812556e3ca/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0-installer.jar",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0-installer.jar",
            "id": 99471,
            "md5": "6819a103e69955cb3d0bed1659919598",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "ff7a48b2633c4cff0ee70565114c64b18ec7ba1a124b41d762f27fb465cb39f8",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Installer",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/f382c99aa6984e5e0223e6437f8a4d29/64073f13/JBEAP-7.4.0/jboss-eap-7.4.0.zip",
            "file_path": "JBEAP-7.4.0/jboss-eap-7.4.0.zip",
            "id": 99481,
            "md5": "feddc39d58a29b1ed9791121a77e8b49",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "5f1f0b7a389dedcd6f91ea3c8c6c9b723e9e8609bdf5720d4088e5469d46ad3a",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4",
            "type": "DISTRIBUTION",
            "version": "7.4",
            "visibility": "PUBLIC"
        }
    ]


We can filter results using the following (which is, matching the title against name and version):

    - name: Filter install zipfile 
      ansible.builtin.set_fact:
        filtered_products: "{{ product_results.results | json_query('[?title==join(`\" \"`,[name,version])]') | list }}"

or if we know the filename:

    - name: Filter install zipfile 
        filtered_products: "{{ product_results.results | selectattr('file_path', 'match', '.*/jboss-eap-{{ eap_version }}.zip$') }}"


## Download EAP

With the received product_id it is trivial to pass it to the download endpoint:

    - name: Download EAP installation
      middleware_automation.common.product_download:
        client_id: "{{ client_id }}"
        client_secret: "{{ client_secret }}"
        product_id: "{{ (filtered_products | first).id }}"
        dest: /tmp


## Search the most recent cumulative patch for EAP x.y

We have to start with the following parameters (note: SECURITY is a subset of BUGFIX):

    - name: Search EAP patches
      middleware_automation.common.product_search:
        client_id: "{{ client_id }}"
        client_secret: "{{ client_secret }}"
        product_version: 7.4
        product_type: BUGFIX
        product_category: appplatform
      register: product_results

we get in response a long list of items:

    "results": [
        {
            "category": "appplatform",
            "description": "JmsXA connection factory not binding to java:jboss/DefaultJMSConnectionFactory",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/ca4bd7b855ab78593cc93324ae9c8219/64073fbe/jbeap-22224.zip",
            "file_path": "jbeap-22224.zip",
            "id": 99731,
            "md5": "60ef79b63654e9b0a48a9ab91a7a2e4d",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "490f2e7b4b74e979437e92b07540f839c5caeb7b0800de06fa99ccff9a674709",
            "title": "JmsXA connection factory not binding to java:jboss/DefaultJMSConnectionFactory",
            "type": "BUGFIX",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01 Source Code",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/bb319d3a0c9fa5346e475167b78da4cc/64073fbe/JBEAP-7.4.1/jboss-eap-7.4.1-src.zip",
            "file_path": "JBEAP-7.4.1/jboss-eap-7.4.1-src.zip",
            "id": 102051,
            "md5": "f8c20bc54dae244ee03102872d2f58d5",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "5e9260a2debc1e4a2d14ecdd4dc78ea6bcd84236847684a77ea46b903120cc8d",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01 Source Code",
            "type": "BUGFIX",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01 Core Source Code",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/762da2e1b1da1bd74557cb7964a3d252/64073fbe/JBEAP-7.4.1/jboss-eap-7.4.1-core-src.zip",
            "file_path": "JBEAP-7.4.1/jboss-eap-7.4.1-core-src.zip",
            "id": 102061,
            "md5": "8d3fbf4d90d0144e9c7b78fcb794846b",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "d6eee3f09df6ff510587f760a073fe714807f5874a0a39f8296f8407af4c4123",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01 Core Source Code",
            "type": "BUGFIX",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01 Incremental Maven Repository",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/3533d1265afe8f285d96e0d915cf5d4a/64073fbe/JBEAP-7.4.1/jboss-eap-7.4.1-incremental-maven-repository.zip",
            "file_path": "JBEAP-7.4.1/jboss-eap-7.4.1-incremental-maven-repository.zip",
            "id": 102071,
            "md5": "96f24a8027badc0999b0267a312706c6",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "991921a1c8adbae2614e2d2d14f2d2e4b0b949c9e2d6720740da24279de345bb",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01 Incremental Maven Repository",
            "type": "BUGFIX",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
        {
            "category": "appplatform",
            "description": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01",
            "distribution_status": "AVAILABLE",
            "download_path": "https://access.redhat.com/cspdownload/25790f633d61a927209d8b25537000b0/64073fbe/JBEAP-7.4.1/jboss-eap-7.4.1-patch.zip",
            "file_path": "JBEAP-7.4.1/jboss-eap-7.4.1-patch.zip",
            "id": 102081,
            "md5": "e473d11220221b422bdce747c3302f72",
            "name": "Red Hat JBoss Enterprise Application Platform",
            "sha256": "f4c7bc938232a491457c2c0bc06cc2760acdd978a6a70fecbdd683e5e84de2d0",
            "title": "Red Hat JBoss Enterprise Application Platform 7.4 Update 01",
            "type": "BUGFIX",
            "version": "7.4",
            "visibility": "PUBLIC"
        },
    [...] cut

For each result, notice "version": "7.4" and the patch version only showing up in textual fields: `description`, `file_path`, and `title`

Unlike before, there is no filtering on title and description because for all results, title==description; the title contains `Update ZZ` which is not included in any other field. So an attempt like the following would be very EAP specific, and we would have trouble expressing the update version, since we haven't found it yet.


    - name: Filter results
      ansible.builtin.set_fact:
        filtered_products: "{{ product_results.results | json_query('[?title==join(`\" \"`,[name,version+' Update 01'])]') | list  }}"

The most reliable way to find the latest CP seems to be:

    - name: Filter versions
      ansible.builtin.set_fact:
        filtered_versions: "{{ product_results.results | map(attribute='file_path') | select('match', '^[^/]*/jboss-eap-.*[0-9]*[.][0-9]*[.][0-9]*.*$') | map('regex_replace','[^/]*/jboss-eap-([0-9]*[.][0-9]*[.][0-9]*)-.*','\\1' ) | list | unique }}"

getting:

    "filtered_versions": [
        "7.4.1",
        "7.4.2",
        "7.4.3",
        "7.4.4",
        "7.4.5",
        "7.4.6",
        "7.4.7",
        "7.4.8",
        "7.4.9"
    ]

At this point we can version_sort (beware: it's in community.general), or accept the risk results are already sorted by insert_date (looks like so), and finally filter by file:

    - name: Determine latest version
      set_fact:
         eap_latest_version: "{{ filtered_versions | version_sort | last }}"
    - name: Filter results
      ansible.builtin.set_fact:
        filtered_products: "{{ product_results.results | selectattr('file_path', 'match', '.*/jboss-eap-{{ eap_latest_version }}.zip$') | list }}"

and we get:

        "filtered_products": [
            {
                "category": "appplatform",
                "description": "Red Hat JBoss Enterprise Application Platform 7.4 Update 09",
                "distribution_status": "AVAILABLE",
                "download_path": "https://access.redhat.com/cspdownload/06f3423cac665004eadc28efc64df19f/640745f5/JBEAP-7.4.9/jboss-eap-7.4.9-patch.zip",
                "file_path": "JBEAP-7.4.9/jboss-eap-7.4.9-patch.zip",
                "id": 105093,
                "md5": "fb259a4319f6bc3a7f63463f0b37b578",
                "name": "Red Hat JBoss Enterprise Application Platform",
                "sha256": "9a81cdba3d4200aeecd84d45ac0b848ffc8caf24ef11f38513319f94219ab488",
                "title": "Red Hat JBoss Enterprise Application Platform 7.4 Update 09",
                "type": "BUGFIX",
                "version": "7.4",
                "visibility": "PUBLIC"
            }
        ]


## Download the patch

 With the product_id, this is trivial like the main zipfile.






