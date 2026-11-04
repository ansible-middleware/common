 v1.2.7
 ======
 
 Minor Changes
 -------------
 
 - AMW-624 common collection spelling and grammar checking for PRs #50
 - Replace deprecated ansible.module_utils imports #51
 
 Breaking Changes / Porting Guide
 --------------------------------
 
 - Drop unused ``fedora.linux_system_roles`` collection dependency. Consumers that relied on transitive installation of ``fedora.linux_system_roles`` via ``middleware_automation.common`` must add it explicitly to their own ``requirements.yml``. This unblocks using ``community.general`` >= 12.0.0 alongside middleware automation collections such as ``middleware_automation.keycloak``.
 
 Bugfixes
 --------
 
 - AMW-594 Upstream release is failing due to recent rules change #48
 - AMW-671 jbcs fails with invalid product category #52
 - Drop unused fedora.linux_system_roles dependency #46
 
