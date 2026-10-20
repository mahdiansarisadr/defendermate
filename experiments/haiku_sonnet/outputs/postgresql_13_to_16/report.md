# PostgreSQL 13 → 16: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

PostgreSQL 13 -> 16 crosses 3 release(s) (14, 15, 16). 69 risk paths: 20 high, 36 medium, 13 low. Main risk types: changed_behavior (39), removed_api (26), changed_default (4). 7 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 15, "by_code": {"W4_no_search_queries": 15}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| high | medium | removed_api | deployment | 14 | `postgresql_01631e9f8c` pg_standby contrib program removed |
| high | medium | removed_api | database | 14 | `postgresql_0172f444ca` Postfix (right-unary) operator support removed |
| high | medium | removed_api | application_code | 14 | `postgresql_12484be158` Factorial operators ! and !! and numeric_fac() removed |
| high | medium | removed_api | configuration | 16 | `postgresql_1f2cea1199` vacuum_defer_cleanup_age server variable removed |
| high | high | removed_api | application_code | 15 | `postgresql_230760360c` PQsendQuery() no longer supported in libpq pipeline mode |
| high | medium | removed_api | application_code | 15 | `postgresql_272d063f3f` Renamed exclusive-mode backup functions pg_start_backup()/pg_stop_backup() |
| high | medium | removed_api | configuration | 14 | `postgresql_336a22a4f4` pg_hba.conf clientcert legacy values 1/0/no-verify no longer supported |
| high | high | removed_api | application_code | 15 | `postgresql_4345c09353` xml2 xml_is_well_formed() function removed |
| high | high | removed_api | application_code | 16 | `postgresql_434e0c374b` Removed pg_walinspect till_end_of_wal functions |
| high | medium | changed_behavior | configuration | 14 | `postgresql_43d19b312e` clientcert=verify-ca disallowed with cert authentication |
| high | high | changed_behavior | database | 16 | `postgresql_5f2b8ce7c3` CREATEROLE role management requires ADMIN OPTION |
| high | medium | removed_api | configuration | 16 | `postgresql_62a430b096` promote_trigger_file server variable removed |
| high | medium | changed_behavior | application_code | 14 | `postgresql_724a97cbad` EXTRACT(date) now errors for units not part of date type |
| high | medium | removed_api | database | 15 | `postgresql_7bfe01bbb4` plpython2u and plpythonu languages removed |
| high | medium | removed_api | application_code | 15 | `postgresql_91ba33fe94` Removed functions pg_backup_start_time() and pg_is_in_backup() |
| high | medium | removed_api | configuration | 14 | `postgresql_987fccfe8d` Legacy Boolean-like password_encryption values no longer accepted |
| high | medium | removed_api | application_code | 14 | `postgresql_9fbfbca3e1` Removed containment operators @ and ~ for geometric types and cube, hstore, intarray, seg |
| high | medium | removed_api | configuration | 15 | `postgresql_a1802b44d1` stats_temp_directory server variable removed |
| high | medium | removed_api | database | 16 | `postgresql_c521076895` Manual views created with ON SELECT rules |
| high | medium | changed_behavior | database | 14 | `postgresql_d1320b72a5` User-defined objects referencing array functions with anyarray signatures must be dropped and recreated |
| medium | medium | changed_default | configuration | 14 | `postgresql_063d5aa8bb` password_encryption default changed from md5 to scram-sha-256 |
| medium | medium | removed_api | deployment | 15 | `postgresql_0aeb9394ab` pg_dump --no-synchronized-snapshots option removed |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_0e147761ab` factorial() of negative numbers now disallowed |
| medium | medium | removed_api | application_code | 14 | `postgresql_1e71bd2674` Single-quoted language name in CREATE/DROP LANGUAGE now disallowed |
| medium | medium | changed_behavior | database | 16 | `postgresql_20f9520b98` Role membership inheritance now set at GRANT time |
| medium | medium | changed_behavior | database | 15 | `postgresql_24f3172f15` CREATE OR REPLACE VIEW can no longer change output column collation |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_27194e765d` to_tsquery/websearch_to_tsquery output change for queries with discarded tokens |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_28d15925c3` Infinite window frame offsets return different (corrected) results |
| medium | medium | changed_behavior | deployment | 15 | `postgresql_2a4f5f5ead` psql --single-transaction final COMMIT now becomes ROLLBACK only when ON_ERROR_STOP is set |
| medium | low | removed_api | deployment | 16 | `postgresql_2a6232c2c0` Removed postmaster binary symbolic link |
| medium | low | removed_api | configuration | 14 | `postgresql_2acbbca54c` operator_precedence_warning server parameter removed |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_40755c4ec6` interval fractional input rounding for units greater than months |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_4645b4b0d2` Regex \D and \W now match newlines in newline-sensitive mode |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_4d0f25b207` Numeric literals with trailing non-numeric characters now rejected |
| medium | medium | changed_behavior | database | 15 | `postgresql_5086aa71d0` Logical replication UPDATE/DELETE requires subscription owner SELECT permission |
| medium | medium | changed_behavior | deployment | 16 | `postgresql_55fa40f078` REINDEX DATABASE / reindexdb no longer reindex system catalog indexes |
| medium | medium | changed_behavior | configuration | 14 | `postgresql_5b9c633eb1` Custom server parameter names with characters invalid in unquoted SQL identifiers |
| medium | medium | changed_behavior | database | 15 | `postgresql_5e13cfd71d` Login role no longer has implicit ADMIN OPTION on its own role membership |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_5e668838bc` Regex back-reference matching no longer applies constraints |
| medium | medium | changed_behavior | database | 15 | `postgresql_6e42608977` Index creation relying on interval text output fails |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_72cf803a6f` "char" type output format change for non-ASCII bytes |
| medium | high | changed_behavior | application_code | 15 | `postgresql_72e0855f91` array_to_tsvector() now errors on empty-string array elements |
| medium | medium | changed_behavior | database | 16 | `postgresql_80f2889427` NULLS NOT DISTINCT primary key indexes disallowed |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_86d8236c5c` EXTRACT() return type changed from float8 to numeric |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_9623a24b4c` websearch_to_tsquery quoted adjacent discarded tokens output change |
| medium | low | changed_behavior | database | 16 | `postgresql_9d3f729496` Inherited/partitioned tables with mismatched GENERATED column status |
| medium | low | changed_behavior | application_code | 16 | `postgresql_b9ad526348` PL/pgSQL bound cursor variable string value no longer matches variable name |
| medium | low | changed_behavior | database | 15 | `postgresql_be61b83855` Logical replication into tables with row-level security policies now requires privileged subscription owner |
| medium | medium | removed_api | configuration | 16 | `postgresql_c2bc60b77a` force_parallel_mode renamed to debug_parallel_query |
| medium | medium | changed_default | application_code | 15 | `postgresql_c3d0f02569` Custom scan providers no longer assumed to support projections |
| medium | medium | changed_default | configuration | 15 | `postgresql_c49690050a` hash_mem_multiplier default increased to 2.0 |
| medium | medium | removed_api | configuration | 14 | `postgresql_c57abe8742` Removed server parameter vacuum_cleanup_index_scale_factor |
| medium | medium | removed_api | application_code | 16 | `postgresql_cc8d8091c1` Removed read-only server variables lc_collate and lc_ctype |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_f1a6f3c268` Regex character class with \w as range start or end now disallowed |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_f1bf63ef84` Custom options matching an installed extension name are deleted and cannot be created |
| medium | low | changed_default | database | 15 | `postgresql_f731db1dff` New databases/clusters no longer grant PUBLIC CREATE on public schema |
| low | medium | changed_behavior | application_code | 15 | `postgresql_076d7c8e08` Zero-length Unicode identifiers U&"" now rejected |
| low | low | changed_behavior | database | 14 | `postgresql_11b4c53a07` intarray containment operators no longer use GiST indexes |
| low | high | changed_behavior | application_code | 14 | `postgresql_167726bd25` has_column_privilege() attribute-number checks on non-existent or dropped columns now return false |
| low | high | changed_behavior | application_code | 15 | `postgresql_6642146d25` Interval justification functions now detect integer overflow |
| low | medium | changed_behavior | application_code | 15 | `postgresql_755a05d0ae` random() output changes for same seed |
| low | low | changed_behavior | application_code | 14 | `postgresql_85602454ed` tablefunc normal_rand() rejects negative values |
| low | medium | changed_behavior | application_code | 15 | `postgresql_90c31fa6ac` JSON numeric literal parsing changed to SQL/JSON standard (jsonpath) |
| low | low | removed_api | application_code | 14 | `postgresql_99cd4201b9` Removal of version 2 wire protocol support in server and libpq |
| low | medium | changed_behavior | application_code | 15 | `postgresql_9a56057ff7` chr() with negative argument now raises an error |
| low | low | changed_behavior | configuration | 15 | `postgresql_d48cf30f17` libpq and client programs now resolve the home directory from HOME |
| low | high | changed_behavior | application_code | 14 | `postgresql_dc64bb7d33` var_samp/stddev_samp return NULL instead of NaN for single NaN numeric input |
| low | low | removed_api | configuration | 14 | `postgresql_e068a86a55` SSL compression support removed |
| low | low | removed_api | database | 14 | `postgresql_f785741bfd` Removed composite types for sequences and toast tables |

### pg_standby contrib program removed

`postgresql_01631e9f8c` · high · confidence medium · introduced in 14 · fires at upgrade

The contrib program pg_standby was removed in release 14. Any deployment (e.g. warm standby scripts or recovery_command settings) that invokes pg_standby will no longer have the program available after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, in which pg_standby was removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove contrib program pg_standby (Justin Pryzby)"
- **[required] deployment** `present` `"pg_standby"`: The deployment invokes pg_standby (for example in scripts or in a recovery/restore command configuration). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Remove contrib program pg_standby (Justin Pryzby)"
  - ⚠ The text does not state how pg_standby is typically invoked (e.g. via restore_command) or name a replacement.

Actions:
- Search scripts, configuration files and recovery/restore command settings for pg_standby usage.
- Replace any pg_standby-based standby setup with an alternative approach before upgrading, since the program is removed in 14 and later.

### Postfix (right-unary) operator support removed

`postgresql_0172f444ca` · high · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 removes support for postfix (right-unary) operators. Databases that define or use postfix operators are affected; pg_dump and pg_upgrade warn if postfix operators are being dumped.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where postfix operator support was removed (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@14: "Remove support for postfix (right-unary) operators"
- **[required] database** `present` `"postfix (right-unary) operator"`: The database contains postfix (right-unary) operators, or queries/code use postfix operator syntax. (confidence medium, judge supported)
  - pg_release_notes@14: "Remove support for postfix (right-unary) operators"
  - pg_release_notes@14: "pg_dump and pg_upgrade will warn if postfix operators are being dumped."
  - ⚠ The text does not state what happens to existing postfix operators or queries using them after the upgrade, only that pg_dump and pg_upgrade warn.

Actions:
- Before upgrading, check for user-defined postfix (right-unary) operators in the database, for example via pg_operator.
- Heed warnings from pg_dump and pg_upgrade about postfix operators being dumped.
- Rework any operators or queries that rely on postfix operator syntax, e.g. use a prefix operator or a function instead.

### Factorial operators ! and !! and numeric_fac() removed

`postgresql_12484be158` · high · confidence medium · introduced in 14 · fires at upgrade

The factorial operators ! and !! and the function numeric_fac() were removed in release 14. Queries, views, functions or other objects that use them will fail on 16. The factorial() function is still supported.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which removed the factorial operators and numeric_fac(). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!, as well as function numeric_fac()"
- **[alternative] api_usage** `present` `"numeric_fac"`: Application SQL or database objects use the factorial operators ! or !! (prefix or postfix) or call numeric_fac(). (confidence medium, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!, as well as function numeric_fac()"
  - ⚠ The text does not state the exact error behavior when removed operators or functions are used.
- **[disqualifying] api_usage** `absent` `"!"`: The application uses factorial() instead of the removed operators or numeric_fac(), which is still supported. (confidence high, judge supported)
  - pg_release_notes@14: "The factorial() function is still supported."

Actions:
- Replace uses of the ! and !! operators and numeric_fac() with the factorial() function.
- Check stored functions, views, and application SQL for uses of the removed operators before upgrading.

### vacuum_defer_cleanup_age server variable removed

`postgresql_1f2cea1199` · high · confidence medium · introduced in 16 · fires at upgrade

The server variable vacuum_defer_cleanup_age is removed in PostgreSQL 16. Configurations (postgresql.conf, ALTER SYSTEM, ALTER ROLE/DATABASE settings, or startup options) that set it will no longer be valid. The release notes say it has been unnecessary since hot_standby_feedback and replication slots were added.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, in which vacuum_defer_cleanup_age is removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove the server variable vacuum_defer_cleanup_age"
- **[required] configuration** `present` `"vacuum_defer_cleanup_age"`: The deployment configuration sets the server variable vacuum_defer_cleanup_age (for example in postgresql.conf, postgresql.auto.conf, per-role or per-database settings, or startup options). (confidence medium, judge supported)
  - pg_release_notes@16: "Remove the server variable vacuum_defer_cleanup_age"
  - ⚠ The text does not state how the server behaves when a removed variable is still set (e.g. startup error).
- **[optional] configuration** `present` `"hot_standby_feedback"`: The setting was used to retain dead rows for standby queries; the replacement mechanisms are hot_standby_feedback and replication slots. (confidence medium, judge partially_supported)
  - pg_release_notes@16: "This has been unnecessary since hot_standby_feedback and replication slots were added."
  - ⚠ The text does not describe behavioral differences between the removed variable and the replacements.

Actions:
- Remove vacuum_defer_cleanup_age from postgresql.conf, postgresql.auto.conf, ALTER SYSTEM/ROLE/DATABASE settings, and any startup options or deployment templates before upgrading to 16.
- Use hot_standby_feedback and replication slots instead where the setting was used for standby query cleanup protection.

### PQsendQuery() no longer supported in libpq pipeline mode

`postgresql_230760360c` · high · confidence high · introduced in 15 · fires at first_use

libpq's PQsendQuery() is no longer supported in pipeline mode as of release 15. Applications that combine PQsendQuery() with pipeline mode must be modified to use PQsendQueryParams() instead.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where PQsendQuery() stopped being supported in pipeline mode. (confidence high, judge supported)
  - pg_release_notes@15: "libpq's PQsendQuery() function is no longer supported in pipeline mode"
- **[required] api_usage** `present` `"PQsendQuery"`: The application calls PQsendQuery() while libpq is in pipeline mode. (confidence high, judge supported)
  - pg_release_notes@15: "Applications that are using that combination will need to be modified"
- **[disqualifying] api_usage** `absent` `"PQenterPipelineMode"`: The application does not use pipeline mode, or already uses PQsendQueryParams() in pipeline mode. (confidence low, judge partially_supported)
  - pg_release_notes@15: "Applications that are using that combination will need to be modified to use PQsendQueryParams() instead."

Actions:
- Find uses of PQsendQuery() that run while libpq is in pipeline mode.
- Replace those calls with PQsendQueryParams().

### Renamed exclusive-mode backup functions pg_start_backup()/pg_stop_backup()

`postgresql_272d063f3f` · high · confidence medium · introduced in 15 · fires at first_use

Exclusive backup mode was removed. pg_start_backup() and pg_stop_backup() were renamed to pg_backup_start() and pg_backup_stop(), so backup scripts or tools that call the old names will break after upgrading past release 15.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which removed exclusive backup mode and renamed the backup functions. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Remove long-deprecated exclusive backup mode"
- **[required] api_usage** `present` `"pg_start_backup|pg_stop_backup"`: Backup scripts, tooling or application code call pg_start_backup() or pg_stop_backup(). (confidence high, judge supported)
  - pg_release_notes@15: "Functions pg_start_backup()/pg_stop_backup() have been renamed to pg_backup_start()/pg_backup_stop()"
- **[optional] behavior** `present` `"exclusive backup mode"`: Backups rely on exclusive backup mode, which no longer exists. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "The non-exclusive backup mode is considered superior for all purposes."
  - ⚠ The text does not describe how non-exclusive-mode usage differs for callers.

Actions:
- Replace calls to pg_start_backup() with pg_backup_start().
- Replace calls to pg_stop_backup() with pg_backup_stop().
- Update backup scripts to use non-exclusive backup mode.

### pg_hba.conf clientcert legacy values 1/0/no-verify no longer supported

`postgresql_336a22a4f4` · high · confidence medium · introduced in 14 · fires at upgrade

The clientcert option in pg_hba.conf no longer accepts the values 1, 0 or no-verify; only the strings verify-ca and verify-full are accepted. Existing pg_hba.conf entries using the old values must be changed.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the clientcert specification was overhauled. (confidence high, judge supported)
  - pg_release_notes@14: "Overhaul the specification of clientcert in pg_hba.conf"
- **[required] configuration** `present` `"clientcert=1, clientcert=0 or clientcert=no-verify"`: pg_hba.conf uses clientcert with the legacy values 1, 0 or no-verify. (confidence medium, judge supported)
  - pg_release_notes@14: "Values 1/0/no-verify are no longer supported"
  - ⚠ The text does not state how the server reacts (error at load time vs. ignore) to unsupported values.

Actions:
- Replace clientcert=1 with clientcert=verify-ca (or verify-full) in pg_hba.conf
- Replace clientcert=0 / no-verify by removing the clientcert option or using a supported setting, since only verify-ca and verify-full strings are supported
- Review pg_hba.conf entries before upgrading

### xml2 xml_is_well_formed() function removed

`postgresql_4345c09353` · high · confidence high · introduced in 15 · fires at upgrade

The xml2 extension's xml_is_well_formed() function is removed in release 15. Queries, views, functions or other objects that call the xml2 version will break. The text says the function has been implemented in the core backend since Postgres 9.1.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade from 13 to 16 crosses release 15, which removes xml2's xml_is_well_formed() function. (confidence high, judge supported)
  - pg_release_notes@15: "Remove xml2's xml_is_well_formed() function"
- **[required] api_usage** `present` `"xml_is_well_formed"`: The application or database uses xml_is_well_formed() from the xml2 extension (SQL queries, views, functions, or the xml2 extension installed). (confidence high, judge supported)
  - pg_release_notes@15: "Remove xml2's xml_is_well_formed() function"

Actions:
- Search application code, views and functions for xml_is_well_formed() calls.
- Use the core backend xml_is_well_formed() function, which the text says has been implemented since Postgres 9.1, in place of the xml2 version.
- Test queries that call the function after the upgrade.

### Removed pg_walinspect till_end_of_wal functions

`postgresql_434e0c374b` · high · confidence high · introduced in 16 · fires at first_use

The pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal() are removed in release 16, so any scripts, monitoring queries, or application code that call them will fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where these pg_walinspect functions are removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal()"
- **[alternative] api_usage** `present` `"pg_get_wal_records_info_till_end_of_wal"`: Application code, scripts, or monitoring queries call pg_get_wal_records_info_till_end_of_wal(). (confidence high, judge supported)
  - pg_release_notes@16: "pg_get_wal_records_info_till_end_of_wal()"
- **[alternative] api_usage** `present` `"pg_get_wal_stats_till_end_of_wal"`: Application code, scripts, or monitoring queries call pg_get_wal_stats_till_end_of_wal(). (confidence high, judge supported)
  - pg_release_notes@16: "pg_get_wal_stats_till_end_of_wal()"

Actions:
- Search code, scripts, and monitoring queries for the two removed functions and remove or rewrite those calls before upgrading to 16.
- The release note names no replacement; check the pg_walinspect documentation for 16 for alternative ways to inspect WAL ranges.

### clientcert=verify-ca disallowed with cert authentication

`postgresql_43d19b312e` · high · confidence medium · introduced in 14 · fires at upgrade

verify-ca is now disallowed for clientcert when cert authentication is enabled, because cert requires verify-full checking. Entries combining cert authentication with clientcert=verify-ca must be changed.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the clientcert specification was overhauled. (confidence high, judge supported)
  - pg_release_notes@14: "Overhaul the specification of clientcert in pg_hba.conf"
- **[required] configuration** `present` `"cert authentication with clientcert=verify-ca"`: A pg_hba.conf entry uses cert authentication together with clientcert=verify-ca. (confidence medium, judge supported)
  - pg_release_notes@14: "disallow verify-ca if cert authentication is enabled since cert requires verify-full checking"
  - ⚠ The text does not state whether the failure occurs at configuration load or connection time.

Actions:
- Change clientcert to verify-full for entries using cert authentication, or remove the explicit verify-ca setting

### CREATEROLE role management requires ADMIN OPTION

`postgresql_5f2b8ce7c3` · high · confidence high · introduced in 16 · fires at first_use

In release 16, roles with CREATEROLE can no longer change many aspects of any non-superuser role. Changes, including adding members, now require the requesting role to have ADMIN OPTION on the target role. Role properties such as CREATEDB, REPLICATION and BYPASSRLS can be changed only if the requesting role also holds those permissions. Administrative scripts or applications that rely on CREATEROLE alone may fail.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which restricts CREATEROLE privileges and its ability to modify other roles. (confidence high, judge supported)
  - pg_release_notes@16: "Restrict the privileges of CREATEROLE and its ability to modify other roles"
- **[required] database** `present` `"CREATEROLE"`: The deployment has roles with the CREATEROLE privilege that are used to alter or manage other non-superuser roles. (confidence high, judge supported)
  - pg_release_notes@16: "Previously roles with CREATEROLE privileges could change many aspects of any non-superuser role."
- **[required] behavior** `absent` `"ADMIN OPTION"`: The CREATEROLE role performs changes such as adding members (GRANT role membership) or altering role attributes without holding ADMIN OPTION on the target role. (confidence high, judge supported)
  - pg_release_notes@16: "Such changes, including adding members, now require the role requesting the change to have ADMIN OPTION permission."
- **[alternative] behavior** `present` `"CREATEDB|REPLICATION|BYPASSRLS"`: The CREATEROLE role changes the CREATEDB, REPLICATION, or BYPASSRLS properties of roles without itself holding those permissions. (confidence high, judge supported)
  - pg_release_notes@16: "they can now change the CREATEDB, REPLICATION, and BYPASSRLS properties only if they also have those permissions"

Actions:
- Find non-superuser roles with CREATEROLE and the scripts or applications that use them to manage roles.
- Grant ADMIN OPTION on the target roles to the managing CREATEROLE roles, or use a superuser for these operations.
- Ensure CREATEROLE roles that change CREATEDB, REPLICATION or BYPASSRLS also hold those permissions.
- Test role-management workflows in a staging 16 cluster before upgrading.

### promote_trigger_file server variable removed

`postgresql_62a430b096` · high · confidence medium · introduced in 16 · fires at upgrade

The server variable promote_trigger_file was removed in release 16. Standby configurations that set it (e.g. in postgresql.conf) and rely on a trigger file to promote the standby will no longer work; promotion must be done with pg_ctl promote or pg_promote().

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where promote_trigger_file was removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove server variable promote_trigger_file"
- **[required] configuration** `present` `"promote_trigger_file"`: The deployment configures the promote_trigger_file server variable (e.g. in postgresql.conf or included config files) on standbys. (confidence medium, judge supported)
  - pg_release_notes@16: "Remove server variable promote_trigger_file"
  - ⚠ The text does not state how the server behaves when the removed setting is still present in the configuration.
- **[optional] behavior** `absent` `"pg_ctl promote or pg_promote()"`: Failover or promotion tooling/scripts promote a standby by creating the trigger file rather than using pg_ctl promote or pg_promote(). (confidence low, judge partially_supported)
  - pg_release_notes@16: "This was used to promote a standby to primary"
  - ⚠ The text does not describe how specific tooling creates or uses trigger files.

Actions:
- Remove promote_trigger_file from postgresql.conf and any other configuration before or during the upgrade to 16.
- Change standby promotion procedures and automation to use pg_ctl promote or the SQL function pg_promote().

### EXTRACT(date) now errors for units not part of date type

`postgresql_724a97cbad` · high · confidence medium · introduced in 14 · fires at first_use

In release 14, EXTRACT() applied to a date value throws an error for units that are not part of the date data type, so queries that previously worked may fail.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which made EXTRACT(date) throw errors for units not part of the date type. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Also, EXTRACT(date) now throws an error for units that are not part of the date data type."
- **[required] api_usage** `present` `"EXTRACT("`: The application calls EXTRACT() on date values with units such as hour, minute or second that are not part of the date data type. (confidence medium, judge supported)
  - pg_release_notes@14: "EXTRACT(date) now throws an error for units that are not part of the date data type"
  - ⚠ The text does not list which units are not part of the date data type.

Actions:
- Audit EXTRACT() calls on date values for units not valid for date and fix or cast the input to timestamp where needed.
- Test queries that call EXTRACT() on date columns against version 16 before upgrading.

### plpython2u and plpythonu languages removed

`postgresql_7bfe01bbb4` · high · confidence medium · introduced in 15 · fires at upgrade

The server-side languages plpython2u and the generic plpythonu were removed in release 15. Databases that define functions or procedures in these languages, or that create them via CREATE EXTENSION or CREATE LANGUAGE, will not work on 16. The text states Python 2.x is no longer supported and plpythonu was removed rather than being aliased to plpython3u.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where plpython2u and plpythonu were removed (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu"
- **[alternative] database** `present` `"plpythonu or plpython2u"`: The database uses the procedural language plpythonu or plpython2u (functions, procedures, DO blocks, or installed languages/extensions). (confidence medium, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu"
  - ⚠ The text does not state exactly how existing functions in these languages behave on restore or upgrade.
- **[optional] runtime** `present` `"Python 2.x"`: The deployment relies on Python 2 for server-side code, which is no longer supported. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Python 2.x is no longer supported."

Actions:
- Inventory functions, procedures and installed languages using plpythonu or plpython2u before upgrading.
- Port the Python code to Python 3 and recreate it using plpython3u.
- Update any scripts, dumps or migrations that reference LANGUAGE plpythonu or plpython2u to use plpython3u.
- Do not expect plpythonu to be aliased to plpython3u, since it was removed instead.

### Removed functions pg_backup_start_time() and pg_is_in_backup()

`postgresql_91ba33fe94` · high · confidence medium · introduced in 15 · fires at first_use

The functions pg_backup_start_time() and pg_is_in_backup() were removed in release 15 along with exclusive backup mode, so code or monitoring that calls them will fail.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which removed pg_backup_start_time() and pg_is_in_backup(). (confidence high, judge supported)
  - pg_release_notes@15: "the functions pg_backup_start_time() and pg_is_in_backup() have been removed"
- **[required] api_usage** `present` `"pg_backup_start_time|pg_is_in_backup"`: Scripts, monitoring or application code call pg_backup_start_time() or pg_is_in_backup(). (confidence medium, judge supported)
  - pg_release_notes@15: "the functions pg_backup_start_time() and pg_is_in_backup() have been removed"
  - ⚠ The text names no replacement for these two functions.

Actions:
- Remove or rewrite code that calls pg_backup_start_time() or pg_is_in_backup(); the text names no direct replacement.

### Legacy Boolean-like password_encryption values no longer accepted

`postgresql_987fccfe8d` · high · confidence medium · introduced in 14 · fires at upgrade

The legacy (and undocumented) Boolean-like values that were synonyms for md5 are no longer accepted for password_encryption, so configurations that set them will be rejected.

- **[uncertain] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, where the legacy values stopped being accepted. (confidence low, judge not_supported)
  - pg_release_notes@14: "Change the default of the password_encryption server parameter to scram-sha-256"
  - ⚠ Judge: evidence does not support this claim. The quote only says the default of password_encryption changed to scram-sha-256 in release 14. It says nothing about legacy values ceasing to be accepted, which the claim asserts. The 13-to-16 upgrade crossing release 14 is plausible from the section metadata, but the quote does not support the legacy-value claim.
- **[required] configuration** `present` `"password_encryption"`: password_encryption is explicitly set to a legacy Boolean-like value (the text does not list the specific values). (confidence medium, judge supported)
  - pg_release_notes@14: "the legacy (and undocumented) Boolean-like values which were previously synonyms for md5 are no longer accepted"
  - ⚠ The text does not list which Boolean-like values were affected, so they cannot be matched literally.
  - ⚠ The text does not state what happens when a no-longer-accepted value is configured.

Actions:
- Search postgresql.conf, included config files, ALTER SYSTEM settings, and per-role/database settings for password_encryption values other than md5 or scram-sha-256.
- Replace any legacy Boolean-like value with md5 (or scram-sha-256) before upgrading.

### Removed containment operators @ and ~ for geometric types and cube, hstore, intarray, seg

`postgresql_9fbfbca3e1` · high · confidence medium · introduced in 14 · fires at first_use

The deprecated containment operators @ and ~ were removed for built-in geometric data types and the contrib modules cube, hstore, intarray, and seg. Queries, views, indexes, functions, or other objects using these operators will fail and must use <@ and @> instead.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, where the @ and ~ containment operators were removed. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types and contrib modules cube, hstore, intarray, and seg"
- **[required] api_usage** `present` `"@ or ~ operator used on geometric, cube, hstore, intarray, or seg types"`: Application SQL, views, functions, or other database objects use the @ or ~ containment operators with built-in geometric types or with cube, hstore, intarray, or seg data. (confidence high, judge supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types and contrib modules cube, hstore, intarray, and seg"
- **[disqualifying] api_usage** `absent` `"@ or ~ containment operators"`: The application already uses only <@ and @> instead of @ and ~. (confidence low, judge partially_supported)
  - pg_release_notes@14: "The more consistently named <@ and @> have been recommended for many years."

Actions:
- Replace uses of @ and ~ on geometric types and cube, hstore, intarray, and seg with <@ and @> before or during the upgrade.
- Review indexes, views, and functions that reference the removed operators and update them.

### stats_temp_directory server variable removed

`postgresql_a1802b44d1` · high · confidence medium · introduced in 15 · fires at upgrade

The obsolete server variable stats_temp_directory was removed in release 15. A postgresql.conf, ALTER SYSTEM setting, or startup option that still sets it will no longer be a valid server variable after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade from 13 to 16 crosses release 15, which removed the stats_temp_directory server variable. (confidence high, judge supported)
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
- **[required] configuration** `present` `"stats_temp_directory"`: The deployment configuration sets stats_temp_directory (in postgresql.conf, included files, ALTER SYSTEM, or server startup options). (confidence medium, judge supported)
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
  - ⚠ The text does not state what happens to a configuration that still sets the removed variable (e.g. whether the server refuses to start).

Actions:
- Remove stats_temp_directory from postgresql.conf, included config files, ALTER SYSTEM settings (postgresql.auto.conf), and startup scripts or container/orchestration configuration before upgrading.
- Check deployment automation and config templates for references to stats_temp_directory.

### Manual views created with ON SELECT rules

`postgresql_c521076895` · high · confidence medium · introduced in 16 · fires at first_use

PostgreSQL 16 removes the ability to create views manually with ON SELECT rules. Schema scripts, migrations or tooling that create views by issuing CREATE RULE ... ON SELECT will no longer work and must use CREATE VIEW instead.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which removes the ability to create views manually with ON SELECT rules. (confidence high, judge supported)
  - pg_release_notes@16: "Remove the ability to create views manually with ON SELECT rules"
- **[required] api_usage** `present` `"ON SELECT"`: Application code, migrations or schema scripts create views manually by defining ON SELECT rules. (confidence medium, judge supported)
  - pg_release_notes@16: "Remove the ability to create views manually with ON SELECT rules"
  - ⚠ The text does not state the exact SQL syntax (e.g. CREATE RULE ... AS ON SELECT) or the error behavior when such a command is run on version 16.

Actions:
- Search migrations, schema scripts and tooling for ON SELECT rule definitions used to create views.
- Replace manual ON SELECT rule view creation with the standard CREATE VIEW statement.
- Test schema creation and migration scripts against a version 16 instance before upgrading.

### User-defined objects referencing array functions with anyarray signatures must be dropped and recreated

`postgresql_d1320b72a5` · high · confidence medium · introduced in 14 · fires at upgrade

The built-in array functions array_append(), array_prepend(), array_cat(), array_position(), array_positions(), array_remove(), array_replace(), and width_bucket() changed their argument types from anyarray to anycompatiblearray in release 14. User-defined objects such as aggregates and operators that reference those function signatures must be dropped before upgrading and recreated after the upgrade completes.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where these array functions changed from anyarray to anycompatiblearray arguments. (confidence high, judge supported)
  - pg_release_notes@14: "used to take anyarray arguments but now take anycompatiblearray"
- **[required] database** `present` `"user-defined aggregates or operators referencing array_append, array_prepend, array_cat, array_position, array_positions, array_remove, array_replace, or width_bucket"`: The database contains user-defined objects (e.g., aggregates or operators) that reference the signatures of the affected built-in array functions. (confidence medium, judge supported)
  - pg_release_notes@14: "user-defined objects like aggregates and operators that reference those array function signatures must be dropped before upgrading"
  - ⚠ The text says 'like aggregates and operators', so other object types may also be affected; it does not give an exhaustive list.

Actions:
- Before upgrading, identify user-defined aggregates, operators, and similar objects that reference the listed array function signatures.
- Drop those objects before upgrading.
- Recreate the dropped objects once the upgrade completes.

### password_encryption default changed from md5 to scram-sha-256

`postgresql_063d5aa8bb` · medium · confidence medium · introduced in 14 · fires at rotation

The default of password_encryption changed from md5 to scram-sha-256, so new passwords are stored as SHA256 (SCRAM) unless the setting is changed or the password is given in MD5 format. Deployments or clients that depend on md5-stored new passwords may be affected.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, where the password_encryption default changed. (confidence high, judge supported)
  - pg_release_notes@14: "Change the default of the password_encryption server parameter to scram-sha-256"
- **[required] configuration** `absent` `"password_encryption"`: password_encryption is not explicitly set in the server configuration, so the new default applies. (confidence high, judge supported)
  - pg_release_notes@14: "All new passwords will be stored as SHA256 unless this server setting is changed"
- **[required] behavior** `present` `"PASSWORD"`: New passwords are created or rotated after the upgrade (e.g. CREATE ROLE/ALTER ROLE ... PASSWORD) with plain text rather than an MD5-format string. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "All new passwords will be stored as SHA256 unless this server setting is changed or the password is specified in MD5 format."
  - ⚠ The text does not say whether existing MD5 passwords continue to work or what the impact is on clients that cannot use SCRAM.
- **[uncertain] dependency** `unknown` `"md5"`: Clients or tooling that rely on md5-hashed password storage for new passwords (not stated by the text). (confidence low)
  - pg_release_notes@14: "Previously it was md5."
  - ⚠ The text does not say which clients or drivers are affected by the switch to SHA256 storage.

Actions:
- Check whether password_encryption is explicitly set in postgresql.conf or via ALTER SYSTEM; set it to md5 explicitly if MD5 storage for new passwords is still required.
- Review processes that create or rotate role passwords, since new passwords will be stored as SHA256 by default.
- Check any scripts or automation that set the password_encryption server parameter.

### pg_dump --no-synchronized-snapshots option removed

`postgresql_0aeb9394ab` · medium · confidence medium · introduced in 15 · fires at first_use

pg_dump's --no-synchronized-snapshots option was removed in release 15. Any backup script, cron job or tooling that passes this flag to pg_dump will fail once it runs against a pg_dump from version 15 or later, including 16. The option is no longer needed because all still-supported server versions support synchronized snapshots.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where pg_dump's --no-synchronized-snapshots option was removed. (confidence high, judge supported)
  - pg_release_notes@15: "Remove pg_dump's --no-synchronized-snapshots option"
- **[required] api_usage** `present` `"--no-synchronized-snapshots"`: Scripts, cron jobs, CI pipelines or other tooling invoke pg_dump with the --no-synchronized-snapshots option. (confidence medium, judge supported)
  - pg_release_notes@15: "Remove pg_dump's --no-synchronized-snapshots option"
  - ⚠ The text does not state the exact error behavior when the removed option is passed.

Actions:
- Remove --no-synchronized-snapshots from all pg_dump invocations in scripts, cron jobs, CI pipelines and backup tooling.
- Rely on the default behavior, since all still-supported server versions support synchronized snapshots.

### factorial() of negative numbers now disallowed

`postgresql_0e147761ab` · medium · confidence medium · introduced in 14 · fires at first_use

Starting in release 14, factorial() with a negative argument is disallowed, whereas previously such calls returned 1. Code or SQL that calls factorial() with negative inputs and relied on the result of 1 will be affected when upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which introduced the change disallowing factorial() of negative numbers (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@14: "Disallow factorial() of negative numbers"
- **[required] api_usage** `present` `"factorial("`: The application or database code (queries, functions, views, etc.) calls factorial(). (confidence high, judge supported)
  - pg_release_notes@14: "Disallow factorial() of negative numbers"
- **[required] behavior** `present` `"negative argument to factorial()"`: factorial() may be called with a negative argument, and the code may rely on the previous result of 1. (confidence medium, judge supported)
  - pg_release_notes@14: "Previously such cases returned 1."
  - ⚠ The text says such cases are 'disallowed' but does not state whether this is an error or another outcome.

Actions:
- Search application code, SQL scripts, views and stored functions for factorial() calls.
- Ensure factorial() is never called with a negative argument, for example by validating input or guarding the call.
- Remove any dependence on factorial() returning 1 for negative inputs.
- Test code paths that call factorial() with edge-case inputs against version 16.

### Single-quoted language name in CREATE/DROP LANGUAGE now disallowed

`postgresql_1e71bd2674` · medium · confidence medium · introduced in 14 · fires at first_use

Release 14 disallows single-quoting the language name in CREATE LANGUAGE and DROP LANGUAGE. SQL scripts, migrations, or dump/restore tooling that quote the language name will need to be changed to use an unquoted or double-quoted identifier.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which disallowed single-quoted language names in CREATE/DROP LANGUAGE. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow single-quoting of the language name in the CREATE/DROP LANGUAGE command"
- **[required] api_usage** `present` `"CREATE LANGUAGE '<name>' or DROP LANGUAGE '<name>'"`: Application code, migration scripts, or SQL files run CREATE LANGUAGE or DROP LANGUAGE with the language name in single quotes. (confidence medium, judge supported)
  - pg_release_notes@14: "Disallow single-quoting of the language name in the CREATE/DROP LANGUAGE command"
  - ⚠ The text does not state the exact error behavior when a single-quoted language name is used.

Actions:
- Search SQL scripts, migrations, and tooling for CREATE LANGUAGE and DROP LANGUAGE statements with a single-quoted language name.
- Rewrite those statements to use an unquoted language name, or a double-quoted identifier if quoting is needed.

### Role membership inheritance now set at GRANT time

`postgresql_20f9520b98` · medium · confidence medium · introduced in 16 · fires at upgrade

In release 16 the inheritance status of member roles is set at GRANT time, defaulting from the role's inheritance status, and can be overridden with GRANT ... WITH INHERIT. Previously, inheritance of member roles was controlled only by the role's inheritance status, and changing that status affected all previous and future member roles. Deployments that rely on role inheritance and change role INHERIT/NOINHERIT attributes after membership grants may see different privilege inheritance behavior.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where role inheritance for member roles is determined at GRANT time. (confidence high, judge supported)
  - pg_release_notes@16: "Role inheritance now controls the default inheritance status of member roles added during GRANT"
- **[required] database** `present` `"role memberships granted via GRANT"`: The database uses role membership (GRANT role TO role) where members' privilege inheritance depends on role inheritance settings. (confidence medium, judge supported)
  - pg_release_notes@16: "Role inheritance now controls the default inheritance status of member roles added during GRANT"
  - pg_release_notes@16: "Previously the inheritance status of member roles was controlled only by the role's inheritan"
  - ⚠ The text does not state concretely how existing memberships are treated at upgrade; it only describes the new behavior for member roles added during GRANT.
- **[optional] configuration** `present` `"INHERIT or NOINHERIT"`: Roles are created or altered with INHERIT/NOINHERIT attributes, or the application/migrations change a role's inheritance status after memberships exist. (confidence low, judge supported)
  - pg_release_notes@16: "changes to a role's inheritance status affected all previous and future member roles"
  - ⚠ The text does not state exactly how the change in a role's inheritance status affects existing memberships in 16.
- **[uncertain] database** `absent` `"role memberships"`: The deployment does not rely on any role membership inheritance (no GRANT of roles to other roles). (confidence low, judge not_supported)
  - pg_release_notes@16: "Role inheritance now controls the default inheritance status of member roles added during GRANT"
  - ⚠ Judge: evidence does not support this claim. The quote describes a behavior change for role inheritance during GRANT. It says nothing about deployments that do not use role membership, and the claim describes the opposite scenario (no GRANTs of roles), which the quote does not address.

Actions:
- Audit existing role memberships and role INHERIT/NOINHERIT attributes before and after upgrade, and verify effective privileges.
- Use GRANT ... WITH INHERIT to explicitly set the desired inheritance status for each membership.
- Update scripts that change a role's inheritance status expecting it to affect all existing members.

### CREATE OR REPLACE VIEW can no longer change output column collation

`postgresql_24f3172f15` · medium · confidence medium · introduced in 15 · fires at first_use

Starting in release 15, CREATE OR REPLACE VIEW is prevented from changing the collation of an output column. Migrations, deployment scripts or application code that redefine views with CREATE OR REPLACE VIEW and rely on altering a column's collation will no longer be able to do so.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where CREATE OR REPLACE VIEW was changed to prevent changing an output column's collation. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent CREATE OR REPLACE VIEW from changing the collation of an output column"
- **[required] api_usage** `present` `"CREATE OR REPLACE VIEW"`: Application code, migrations or deployment scripts use CREATE OR REPLACE VIEW to redefine an existing view in a way that changes the collation of an output column. (confidence medium, judge supported)
  - pg_release_notes@15: "Prevent CREATE OR REPLACE VIEW from changing the collation of an output column"
  - ⚠ The text does not state what error or behavior results when a collation change is attempted, nor the recommended workaround.

Actions:
- Search migrations, SQL scripts and application code for CREATE OR REPLACE VIEW statements that change the collation of an output column.
- Test view redefinition scripts against a version 15 or 16 instance before upgrading.

### to_tsquery/websearch_to_tsquery output change for queries with discarded tokens

`postgresql_27194e765d` · medium · confidence medium · introduced in 14 · fires at first_use

to_tsquery() and websearch_to_tsquery() now parse query text containing discarded tokens (such as underscore) correctly, so the resulting tsquery differs from the output in releases before 14. Applications, stored queries, expression indexes or tests that depend on the old output may see different results.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14 (13 -> 16), where this parsing fix was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Fix to_tsquery() and websearch_to_tsquery() to properly parse query text containing discarded tokens"
- **[required] api_usage** `present` `"to_tsquery|websearch_to_tsquery"`: The application calls to_tsquery() or websearch_to_tsquery(). (confidence high, judge supported)
  - pg_release_notes@14: "Fix to_tsquery() and websearch_to_tsquery() to properly parse query text containing discarded tokens"
- **[required] behavior** `contains` `"discarded tokens such as underscore"`: The query text passed to these functions contains discarded tokens such as underscore (for example 'pg_class'), or quoted text that includes them. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Certain discarded tokens, like underscore, caused the output of these functions to produce incorrect tsquery output"
  - ⚠ The text names underscore only as an example and does not list all discarded tokens; which tokens are discarded depends on the text search configuration, which the text does not describe.
- **[optional] test_coverage** `present` `"tsquery output comparisons or stored tsquery values"`: Results are persisted or compared against expected tsquery output (stored queries, expression indexes, tests) that rely on the old output. (confidence low, judge partially_supported)
  - pg_release_notes@14: "both websearch_to_tsquery('"pg_class pg"') and to_tsquery('pg_class <-> pg') used to output ( 'pg' & 'class' ) <-> 'pg', but now both output 'pg' <-> 'class' <-> 'pg'."
  - ⚠ The text does not state whether persisted tsquery values or indexes need rebuilding.

Actions:
- Search application code, SQL functions, views and tests for to_tsquery() and websearch_to_tsquery() calls whose input may contain underscores or other discarded tokens.
- Re-run representative queries on version 16 and compare tsquery output and search results with the old behavior.
- Update tests or expected outputs that encode the old tsquery output.

### Infinite window frame offsets return different (corrected) results

`postgresql_28d15925c3` · medium · confidence medium · introduced in 14 · fires at first_use

Window frame clauses using infinite offsets such as 'inf' PRECEDING AND 'inf' FOLLOWING previously returned incorrect results and are now handled correctly. Queries relying on the old (incorrect) output will see different results after crossing release 14.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which fixed handling of infinite window function ranges (13 -> 16 includes 14). (confidence high, judge supported)
  - pg_release_notes@14: "Fix handling of infinite window function ranges"
- **[required] api_usage** `present` `"'inf' PRECEDING"`: The application uses window frame clauses with infinite offsets such as 'inf' PRECEDING AND 'inf' FOLLOWING. (confidence medium, judge supported)
  - pg_release_notes@14: "window frame clauses like 'inf' PRECEDING AND 'inf' FOLLOWING returned incorrect results"
  - ⚠ The text gives 'inf' as an example; it does not state which data types or other infinite-offset forms (e.g. 'infinity') are affected.
- **[optional] behavior** `unknown` `"results of queries with infinite window frame offsets"`: The application or its tests depend on the previous incorrect results from such queries. (confidence medium, judge supported)
  - pg_release_notes@14: "Previously window frame clauses like 'inf' PRECEDING AND 'inf' FOLLOWING returned incorrect results."

Actions:
- Search application SQL, views and functions for window frame clauses with infinite offsets (e.g. 'inf' PRECEDING / FOLLOWING).
- Re-run affected queries on version 16 and compare results with the previous output; update expected results or tests since the old results were incorrect.

### psql --single-transaction final COMMIT now becomes ROLLBACK only when ON_ERROR_STOP is set

`postgresql_2a4f5f5ead` · medium · confidence medium · introduced in 15 · fires at first_use

In psql's --single-transaction mode, after an error the final COMMIT is changed to ROLLBACK only if ON_ERROR_STOP is set. Scripts that run psql with --single-transaction and do not set ON_ERROR_STOP may now commit the work done despite an error, where previously the transaction was rolled back. The text states only the new condition, not the prior behavior, so the exact previous behavior is not specified.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced this psql --single-transaction change. (confidence high)
  - pg_release_notes@15: "change the final COMMIT command to ROLLBACK only if ON_ERROR_STOP is set"
- **[required] api_usage** `present` `"--single-transaction"`: Scripts or deployment tooling invoke psql with the --single-transaction mode. (confidence high, judge supported)
  - pg_release_notes@15: "After an error is detected in psql's --single-transaction mode"
- **[required] configuration** `absent` `"ON_ERROR_STOP"`: ON_ERROR_STOP is not set in those psql runs, so the final COMMIT is no longer changed to ROLLBACK after an error. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "change the final COMMIT command to ROLLBACK only if ON_ERROR_STOP is set"
  - ⚠ The text does not state the behavior in earlier releases, so whether rollback previously happened without ON_ERROR_STOP is not stated.

Actions:
- Set ON_ERROR_STOP (for example with -v ON_ERROR_STOP=1) in psql scripts that use --single-transaction so that an error results in ROLLBACK.
- Review psql --single-transaction scripts that do not set ON_ERROR_STOP and test their error behavior on the new version.

### Removed postmaster binary symbolic link

`postgresql_2a6232c2c0` · medium · confidence low · introduced in 16 · fires at upgrade

Release 16 removes the symbolic links for the postmaster binary. Scripts, service units, or tooling that invoke the binary by the name 'postmaster' may fail to find it after the upgrade. The text does not name a replacement.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which removes the symbolic links for the postmaster binary. (confidence high, judge supported)
  - pg_release_notes@16: "Remove symbolic links for the postmaster binary"
- **[required] deployment** `present` `"postmaster"`: Deployment scripts, service definitions, or tooling invoke the binary through the 'postmaster' symbolic link name. (confidence low, judge supported)
  - pg_release_notes@16: "Remove symbolic links for the postmaster binary"
  - ⚠ The text does not say which paths or packaging layouts contained the symbolic links, nor does it name the binary to use instead.

Actions:
- Search init scripts, systemd units, container entrypoints, and tooling for invocations of 'postmaster'.
- Update any such invocations to call the 'postgres' executable, since the postmaster symbolic links are removed (the text itself does not name a replacement).

### operator_precedence_warning server parameter removed

`postgresql_2acbbca54c` · medium · confidence low · introduced in 14 · fires at upgrade

The server parameter operator_precedence_warning was removed in release 14. Any configuration that sets it (for example postgresql.conf, ALTER SYSTEM, ALTER DATABASE/ROLE SET, or connection options) will need to drop it. The text only says the setting was used for warning applications about PostgreSQL 9.5 changes; it does not state what happens when the removed parameter is still set.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, in which operator_precedence_warning was removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove server parameter operator_precedence_warning"
- **[required] configuration** `present` `"operator_precedence_warning"`: Configuration, role/database settings, or connection options set operator_precedence_warning. (confidence low, judge partially_supported)
  - pg_release_notes@14: "Remove server parameter operator_precedence_warning"
  - ⚠ The text does not state what happens when the removed parameter is still set (e.g. whether the server refuses to start or a SET fails).

Actions:
- Remove operator_precedence_warning from postgresql.conf, postgresql.auto.conf, ALTER SYSTEM/ROLE/DATABASE settings, and any connection options before upgrading.
- Verify that applications no longer depend on the warnings this setting produced about PostgreSQL 9.5 operator precedence changes.

### interval fractional input rounding for units greater than months

`postgresql_40755c4ec6` · medium · confidence medium · introduced in 15 · fires at first_use

When interval input gives a fractional value for a unit greater than months, the value is now rounded to the nearest month. For example, 1.99 years now becomes 2 years rather than 1 year 11 months. Applications or data loads that supply fractional years, decades, centuries or similar interval inputs may get different results.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the interval fractional-unit rounding change was introduced (13 -> 16). (confidence high)
  - pg_release_notes@15: "round to the nearest month"
  - pg_release_notes@15: "Improve consistency of interval parsing with trailing periods"
- **[required] api_usage** `present` `"interval input with fractional years or other unit greater than months"`: The application or its data supplies interval input with a fractional value for a unit greater than months (e.g. '1.99 years'). (confidence medium, judge supported)
  - pg_release_notes@15: "When interval input provides a fractional value for a unit greater than months"
  - ⚠ The text does not list which units are greater than months; years is the only unit given in the example.
- **[optional] behavior** `equals` `"1.99 years previously yielded 1 year 11 months"`: Application logic or stored results depend on the previous result, such as 1.99 years being converted to 1 year 11 months. (confidence low, judge supported)
  - pg_release_notes@15: "convert 1.99 years to 2 years, not 1 year 11 months as before"
  - pg_release_notes@15: "Numbers with trailing periods were rejected on some platforms."
  - ⚠ The text does not give example input strings or state which platforms rejected such numbers.
  - ⚠ The text does not state the new behavior explicitly (accepted vs. rejected on all platforms).

Actions:
- Search application code, SQL, and data loading scripts for interval literals or inputs with fractional years or other units greater than months.
- Test those inputs on version 16 and compare the results with those on 13.
- Update tests or logic that expect results such as 1 year 11 months for 1.99 years.
- Where a specific result is needed, supply interval inputs in whole units or in months.
- Review code and data that pass interval strings containing numbers with trailing periods and test their parse results on version 16.
- Add or run tests for interval input validation on the target platform.

### Regex \D and \W now match newlines in newline-sensitive mode

`postgresql_4645b4b0d2` · medium · confidence medium · introduced in 14 · fires at first_use

In regular expression newline-sensitive mode, the \D and \W shorthands now match newlines; previously they did not. Queries or code relying on the old behavior may return different matches. The old behavior can be restored with [^[:digit:]] or [^[:word:]].

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14 (13 -> 16), where the \D and \W newline-matching change was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Allow \D and \W shorthands to match newlines in regular expression newline-sensitive mode"
- **[required] api_usage** `present` `"\\D or \\W"`: The application uses the \D or \W regex shorthands in regular expressions evaluated in newline-sensitive mode. (confidence medium, judge supported)
  - pg_release_notes@14: "Allow \D and \W shorthands to match newlines in regular expression newline-sensitive mode"
  - ⚠ The text does not state how newline-sensitive mode is enabled, so it is unclear which flags or settings place a regex in that mode.
- **[optional] behavior** `present` `"reliance on \\D/\\W not matching newlines"`: The application depends on \D or \W not matching newlines, for example by relying on the old match results. (confidence medium, judge supported)
  - pg_release_notes@14: "Previously they did not match newlines in this mode"

Actions:
- Find regular expressions using \D or \W that run in newline-sensitive mode.
- Where the old behavior is needed, replace \D with [^[:digit:]] and \W with [^[:word:]].
- Test affected queries and code against inputs containing newlines.

### Numeric literals with trailing non-numeric characters now rejected

`postgresql_4d0f25b207` · medium · confidence medium · introduced in 15 · fires at first_use

Starting in release 15, numeric literals can no longer have non-numeric trailing characters. Query text like 123abc was previously interpreted as 123 followed by a separate token abc; such SQL text is now prevented (rejected), so queries relying on that tokenization can break.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the restriction on numeric literals with trailing non-numeric characters. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent numeric literals from having non-numeric trailing characters"
- **[required] api_usage** `present` `"numeric literal immediately followed by letters, e.g. 123abc"`: Application SQL text contains numeric literals immediately followed by non-numeric characters (e.g. 123abc), relying on the old tokenization as a number followed by a separate token. (confidence medium, judge supported)
  - pg_release_notes@15: "Previously, query text like 123abc would be interpreted as 123 followed by a separate token abc."
  - ⚠ The text does not state the exact error behavior or the full set of trailing characters that are rejected.

Actions:
- Search application SQL and generated queries for numeric literals directly followed by letters and insert whitespace or correct the syntax (e.g. write 123 abc if two tokens were intended).
- Run the application's SQL test suite against PostgreSQL 16 to detect queries that now fail to parse.

### Logical replication UPDATE/DELETE requires subscription owner SELECT permission

`postgresql_5086aa71d0` · medium · confidence medium · introduced in 15 · fires at first_use

Starting in release 15, UPDATE and DELETE logical replication operations are prevented on tables where the subscription owner lacks SELECT permission on the table. Existing logical replication subscriptions whose owner lacks SELECT on a target table will have those UPDATE/DELETE operations blocked.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the requirement that the subscription owner have SELECT permission for replicated UPDATE and DELETE. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent UPDATE and DELETE logical replication operations on tables where the subscription owner does not have SELECT permission on the table"
- **[required] deployment** `present` `"logical replication subscription"`: The deployment uses logical replication subscriptions that apply UPDATE or DELETE operations to subscriber tables. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent UPDATE and DELETE logical replication operations on tables"
- **[required] database** `absent` `"SELECT privilege for subscription owner on subscribed tables"`: The subscription owner does not have SELECT permission on a subscribed table that receives UPDATE or DELETE operations. (confidence medium, judge supported)
  - pg_release_notes@15: "where the subscription owner does not have SELECT permission on the table"
  - ⚠ The text does not state how the failure manifests (e.g. error or stalled replication).

Actions:
- Identify subscription owners and the tables they replicate into, and verify each owner has SELECT permission on those tables.
- Grant SELECT on the subscribed tables to the subscription owner where UPDATE or DELETE operations are replicated.

### REINDEX DATABASE / reindexdb no longer reindex system catalog indexes

`postgresql_55fa40f078` · medium · confidence medium · introduced in 16 · fires at first_use

Starting in 16, REINDEX DATABASE and reindexdb do not process indexes on system catalogs. Maintenance jobs that relied on them to rebuild system catalog indexes will skip those indexes. They can still be processed with REINDEX SYSTEM and reindexdb --system.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where REINDEX DATABASE and reindexdb stop processing system catalog indexes. (confidence high, judge supported)
  - pg_release_notes@16: "Change REINDEX DATABASE and reindexdb to not process indexes on system catalogs"
- **[required] api_usage** `present` `"REINDEX DATABASE"`: Scripts, cron jobs or runbooks run REINDEX DATABASE or reindexdb (without --system) and rely on it to reindex system catalog indexes. (confidence medium, judge supported)
  - pg_release_notes@16: "Change REINDEX DATABASE and reindexdb to not process indexes on system catalogs"
  - ⚠ The text does not say whether any application depends on system catalog indexes being reindexed by these commands.
- **[disqualifying] api_usage** `present` `"REINDEX SYSTEM"`: The maintenance job already runs REINDEX SYSTEM or reindexdb --system separately, so system catalog indexes are still processed. (confidence high, judge supported)
  - pg_release_notes@16: "Processing such indexes is still possible using REINDEX SYSTEM and reindexdb --system."

Actions:
- Find scripts and jobs that run REINDEX DATABASE or reindexdb.
- If system catalog indexes must still be reindexed, add REINDEX SYSTEM or reindexdb --system to those jobs.

### Custom server parameter names with characters invalid in unquoted SQL identifiers

`postgresql_5b9c633eb1` · medium · confidence medium · introduced in 14 · fires at upgrade

Starting in release 14, custom server parameter names (e.g. extension-style names like prefix.name) must use only characters valid in unquoted SQL identifiers. Configurations or application code that set custom parameter names containing other characters may no longer be accepted after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which introduced the requirement on custom server parameter names. (confidence high, judge supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters that are valid in unquoted SQL identifiers"
- **[required] configuration** `present` `"custom server parameter name containing characters invalid in unquoted SQL identifiers"`: The deployment or application defines or sets custom server parameters whose names contain characters not valid in unquoted SQL identifiers. (confidence medium, judge supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters that are valid in unquoted SQL identifiers"
  - ⚠ The text does not state what exact failure occurs (error, rejection, or ignoring) for invalid names.
  - ⚠ The text does not state where custom parameters may be set (postgresql.conf, SET, ALTER ROLE/DATABASE, etc.).

Actions:
- Audit postgresql.conf, ALTER SYSTEM/ROLE/DATABASE settings, and application SET/set_config calls for custom parameter names containing characters outside those valid in unquoted SQL identifiers.
- Rename any such custom parameters to use only characters valid in unquoted SQL identifiers, and update the code or extensions that read them.

### Login role no longer has implicit ADMIN OPTION on its own role membership

`postgresql_5e13cfd71d` · medium · confidence medium · introduced in 15 · fires at first_use

In release 15 the default ADMIN OPTION privilege a login role had on its own role membership was removed. Previously a login role could add or remove members of its own role without ADMIN OPTION. Applications or deployment scripts that rely on a login role managing its own membership (GRANT/REVOKE of that role) without an explicit ADMIN OPTION grant may fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the default ADMIN OPTION on a login role's own membership was removed. (confidence high, judge supported)
  - pg_release_notes@15: "Remove the default ADMIN OPTION privilege a login role has on its own role membership"
- **[required] behavior** `present` `"login role managing membership of its own role without explicit ADMIN OPTION"`: A login role adds or removes members of its own role (e.g. via GRANT/REVOKE of that role) without having been explicitly granted ADMIN OPTION. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Previously, a login role could add/remove members of its own role, even without ADMIN OPTION privilege."
  - ⚠ The text does not state the exact error or SQL commands affected; GRANT/REVOKE role membership is an inference of how members are added or removed.
- **[uncertain] database** `present` `"explicit ADMIN OPTION grant"`: The role is explicitly granted ADMIN OPTION on its own membership, in which case the behavior is not lost. (confidence low, judge not_supported)
  - pg_release_notes@15: "even without ADMIN OPTION privilege"
  - ⚠ The text does not explicitly describe how to grant ADMIN OPTION explicitly as a remedy.
  - ⚠ Judge: evidence does not support this claim. The quote only says that previously a login role could add/remove members even without ADMIN OPTION. It does not state that an explicit grant of ADMIN OPTION on the role's own membership preserves the behavior after the change.

Actions:
- Identify login roles that manage membership of their own role and grant ADMIN OPTION explicitly where this is still required.
- Review scripts and applications that add or remove members of login roles and test them against the new version.

### Regex back-reference matching no longer applies constraints

`postgresql_5e668838bc` · medium · confidence medium · introduced in 14 · fires at first_use

In release 14, regular expression back-references are matched disregarding constraints. For example, in (^\d+).*\1 the ^ constraint applies at the start of the string but not when matching \1. Regexes that use back-references together with constraints may produce different match results than on version 13.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the back-reference matching change was introduced (13 -> 16). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Disregard constraints when matching regular expression back-references"
- **[required] api_usage** `present` `"regular expression with back-reference such as \\1 and a constraint such as ^"`: The application or database objects use regular expressions containing back-references (e.g. \1) combined with constraints such as ^. (confidence medium, judge supported)
  - pg_release_notes@14: "in (^\d+).*\1, the ^ constraint should be applied at the start of the string, but not when matching \1"
  - ⚠ The text does not say which other constraints besides ^ are affected or how match results may differ in practice.

Actions:
- Search application code, SQL, views, functions and constraints for regular expressions that use back-references (\1 to \9) combined with constraints such as ^.
- Test those regular expressions on version 16 and compare results with version 13 before upgrading.

### Index creation relying on interval text output fails

`postgresql_6e42608977` · medium · confidence medium · introduced in 15 · fires at first_use

The interval output function is now marked stable rather than immutable because it depends on IntervalStyle. Creating indexes that rely on the text output of interval values (for example, expression indexes casting interval to text) will fail.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the interval output function was changed from immutable to stable. (confidence high, judge supported)
  - pg_release_notes@15: "Mark the interval output function as stable, not immutable, since it depends on IntervalStyle"
- **[required] database** `present` `"index expression using interval text output"`: The database defines or creates indexes (or other immutable-requiring expressions) that rely on the text output of interval values. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "cause creation of indexes relying on the text output of interval values to fail"
  - ⚠ The text does not say whether existing indexes are affected on restore or only new index creation; it says creation of such indexes fails.
  - ⚠ The text does not name specific expressions (e.g. casts to text) that count as relying on interval text output.

Actions:
- Find indexes whose expressions depend on the text output of interval values and redesign them to avoid relying on interval-to-text conversion.
- Test dump/restore or schema creation scripts on version 16 to confirm such index creation no longer fails.

### "char" type output format change for non-ASCII bytes

`postgresql_72cf803a6f` · medium · confidence medium · introduced in 15 · fires at first_use

The I/O format of type "char" changed for non-ASCII characters: bytes with the high bit set are now output as a backslash and three octal digits instead of the raw byte. Applications that read or compare "char" values containing such bytes may see different output.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the "char" I/O format change (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "Change the I/O format of type "char" for non-ASCII characters"
- **[required] database** `present` `"\"char\""`: The database or application uses the type "char" (not char(n)) for columns or values containing non-ASCII bytes (high bit set) whose output is read or compared. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Bytes with the high bit set are now output as a backslash and three octal digits"
  - ⚠ The text does not say how common non-ASCII data in "char" columns is or whether stored data is altered; it only describes the output format.

Actions:
- Identify columns and expressions of type "char" that may hold non-ASCII bytes.
- Test application code that reads, parses or compares "char" output for the new backslash plus three octal digit format.
- Adjust code to handle the backslash-octal output for bytes with the high bit set.

### array_to_tsvector() now errors on empty-string array elements

`postgresql_72e0855f91` · medium · confidence high · introduced in 15 · fires at first_use

Starting in release 15, array_to_tsvector() generates an error if passed an empty-string array element, because lexemes should never be empty. Applications calling it with arrays that may contain empty strings will now fail. Additionally, empty lexemes stored by previous releases can cause dump/restore failures and inconsistent results, so existing data should be verified.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the error on empty-string array elements in array_to_tsvector(). (confidence high, judge supported)
  - pg_release_notes@15: "Generate an error if array_to_tsvector() is passed an empty-string array element"
- **[required] api_usage** `present` `"array_to_tsvector"`: The application calls array_to_tsvector() with arrays that may contain empty-string elements. (confidence high, judge supported)
  - pg_release_notes@15: "array_to_tsvector() is passed an empty-string array element"
- **[optional] database** `present` `"empty lexemes in stored tsvector values"`: Existing stored tsvector data from earlier releases may contain empty lexemes, which can cause dump/restore failures and inconsistent results. (confidence medium, judge supported)
  - pg_release_notes@15: "Users of previous Postgres releases should verify that no empty lexemes are stored because they can lead to dump/restore failures and inconsistent results."
  - ⚠ The text does not state how to detect empty lexemes or which columns are affected.

Actions:
- Ensure arrays passed to array_to_tsvector() contain no empty-string elements, filtering or cleaning them before the call.
- Before migrating, verify that no empty lexemes are stored in tsvector data in the existing database.
- Test dump/restore of databases with tsvector data before the upgrade.

### NULLS NOT DISTINCT primary key indexes disallowed

`postgresql_80f2889427` · medium · confidence medium · introduced in 16 · fires at first_use

Release 16 disallows NULLS NOT DISTINCT indexes for primary keys. Schemas, migrations or DDL that define a primary key with NULLS NOT DISTINCT may fail once on version 16.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which disallows NULLS NOT DISTINCT indexes for primary keys. (confidence high, judge supported)
  - pg_release_notes@16: "Disallow NULLS NOT DISTINCT indexes for primary keys"
- **[required] database** `present` `"NULLS NOT DISTINCT"`: Schemas, migrations or application DDL define a primary key index using NULLS NOT DISTINCT. (confidence medium, judge supported)
  - pg_release_notes@16: "Disallow NULLS NOT DISTINCT indexes for primary keys"
  - ⚠ The text does not say whether existing such indexes fail on upgrade or only new definitions are rejected.
  - ⚠ The text does not state the exact error or the behavior of the ALTER/CREATE statements.

Actions:
- Search DDL, migrations and schema dumps for primary keys defined with NULLS NOT DISTINCT.
- Remove NULLS NOT DISTINCT from primary key definitions before upgrading, or use a different approach to enforce the desired uniqueness semantics (for example a separate unique index) if NULL handling matters.

### EXTRACT() return type changed from float8 to numeric

`postgresql_86d8236c5c` · medium · confidence medium · introduced in 14 · fires at first_use

In release 14 EXTRACT() returns numeric instead of float8. Queries, views, application code or functions that depend on the float8 result type may see different types, values or formatting. The old behavior can still be obtained by calling date_part().

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which changed EXTRACT() to return numeric. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Change EXTRACT() to return type numeric instead of float8"
- **[required] api_usage** `present` `"EXTRACT("`: The application, SQL queries, views or functions call EXTRACT() and depend on its float8 result type. (confidence medium, judge supported)
  - pg_release_notes@14: "Change EXTRACT() to return type numeric instead of float8"
  - ⚠ The text does not say which usages are affected beyond mentioning that precision loss is avoided 'in some usages'.
- **[disqualifying] api_usage** `present` `"date_part("`: The application already uses date_part() instead of EXTRACT(), which retains the old behavior. (confidence high, judge supported)
  - pg_release_notes@14: "The old behavior can still be obtained by using the old underlying function date_part()"

Actions:
- Find all EXTRACT() usages in application SQL, views, functions and generated columns, and test them for the numeric result type.
- Replace EXTRACT() with date_part() where the previous float8 result is required.
- Review code that depends on float8 result types, casts or formatting of EXTRACT() output.

### websearch_to_tsquery quoted adjacent discarded tokens output change

`postgresql_9623a24b4c` · medium · confidence medium · introduced in 14 · fires at first_use

In release 14, websearch_to_tsquery() parses quoted text containing multiple adjacent discarded tokens differently. Previously such tokens were treated as multiple tokens, producing a distance operator like <2>; now the output uses <->. Applications, stored tsqueries, or tests that depend on the old tsquery output or on search results derived from it may see different results.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14 (13 -> 16), where websearch_to_tsquery() parsing of adjacent discarded tokens in quotes changed. (confidence high, judge supported)
  - pg_release_notes@14: "Fix websearch_to_tsquery() to properly parse multiple adjacent discarded tokens in quotes"
- **[required] api_usage** `present` `"websearch_to_tsquery"`: The application calls websearch_to_tsquery() with quoted text that can contain multiple adjacent discarded tokens (e.g. punctuation such as ': '). (confidence medium, judge supported)
  - pg_release_notes@14: "Fix websearch_to_tsquery() to properly parse multiple adjacent discarded tokens in quotes"
  - ⚠ The text does not define which tokens count as discarded beyond the examples of underscore and the ': ' sequence.
- **[optional] behavior** `contains` `"<2>"`: The application or its tests depend on the exact tsquery output (e.g. the old 'aaa' <2> 'bbb' form) or on matching behavior derived from it. (confidence low, judge partially_supported)
  - pg_release_notes@14: "websearch_to_tsquery('"aaa: bbb"') used to output 'aaa' <2> 'bbb', but now outputs 'aaa' <-> 'bbb'."

Actions:
- Find usages of websearch_to_tsquery() with quoted phrases and re-test their output and search results on version 16.
- Update tests or expected outputs that encode the old 'aaa' <2> 'bbb' form to the new 'aaa' <-> 'bbb' form.
- Regenerate any stored tsquery values or indexes/materialized results derived from websearch_to_tsquery() on quoted text if they must reflect the corrected parsing.

### Inherited/partitioned tables with mismatched GENERATED column status

`postgresql_9d3f729496` · medium · confidence low · introduced in 16 · fires at first_use

Release 16 tightens GENERATED expression restrictions on inherited and partitioned tables. Columns of parent/partitioned and child/partition tables must all have the same generation status, though the actual generation expressions may now differ. Schemas or DDL where parent and child columns differ in generation status may be rejected.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where the GENERATED expression restrictions on inherited and partitioned tables were tightened. (confidence high, judge supported)
  - pg_release_notes@16: "Tighten GENERATED expression restrictions on inherited and partitioned tables"
- **[required] database** `present` `"GENERATED"`: The database uses inheritance or partitioning with GENERATED columns in parent/partitioned and child/partition tables. (confidence high, judge supported)
  - pg_release_notes@16: "Columns of parent/partitioned and child/partition tables must all have the same generation status"
- **[required] database** `present` `"mismatched generation status between parent and child columns"`: A parent/partitioned table column and the corresponding child/partition column differ in generation status (one generated, the other not). (confidence low, judge partially_supported)
  - pg_release_notes@16: "must all have the same generation status"
  - ⚠ The text does not state whether existing mismatched tables fail during upgrade or only when DDL is executed, or what the exact error behavior is.

Actions:
- Audit inheritance and partition hierarchies for columns where parent and child differ in generation status (generated vs. not generated).
- Align the generation status of the columns across parent/partitioned and child/partition tables before migrating.
- Generation expressions themselves may differ between parent and child in version 16.

### PL/pgSQL bound cursor variable string value no longer matches variable name

`postgresql_b9ad526348` · medium · confidence low · introduced in 16 · fires at first_use

In PL/pgSQL, the string value (portal name) of bound cursor variables is now assigned during OPEN and no longer matches the variable name. Code relying on the portal name equaling the cursor variable name may break. Workaround: assign the desired portal name to the cursor variable before OPEN.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which changes the assignment rules for PL/pgSQL bound cursor variables. (confidence high, judge supported)
  - pg_release_notes@16: "Change assignment rules for PL/pgSQL bound cursor variables"
- **[required] api_usage** `present` `"PL/pgSQL bound cursor variables"`: The application uses PL/pgSQL bound cursor variables (cursors declared with a query) that are opened with OPEN. (confidence high, judge supported)
  - pg_release_notes@16: "Change assignment rules for PL/pgSQL bound cursor variables"
  - pg_release_notes@16: "now it will be assigned during OPEN"
- **[required] behavior** `present` `"reliance on cursor variable string value equal to variable name"`: The code depends on the cursor variable's string value (portal name) matching the variable name, for example by referencing the portal by that name in FETCH/MOVE/CLOSE or in other sessions/statements. (confidence low, judge partially_supported)
  - pg_release_notes@16: "will not match the variable name"
  - ⚠ The text does not state how code would depend on the portal name, so which usages are affected is not specified.
- **[disqualifying] behavior** `present` `"assignment of portal name to cursor variable before OPEN"`: The application already assigns the desired portal name to the cursor variable before OPEN. (confidence medium, judge partially_supported)
  - pg_release_notes@16: "assign the desired portal name to the cursor variable before OPEN"

Actions:
- Search PL/pgSQL functions and procedures for bound cursor variables and check whether they depend on the portal name matching the variable name.
- To restore the previous behavior, assign the desired portal name to the cursor variable before OPEN.

### Logical replication into tables with row-level security policies now requires privileged subscription owner

`postgresql_be61b83855` · medium · confidence low · introduced in 15 · fires at first_use

In release 15, logical replication can run as the owner of the subscription. Because row-level security policies are not checked, only superusers, roles with bypassrls, and table owners can replicate into tables with row-level security policies. Subscriptions whose owner lacks one of these attributes may be unable to replicate into RLS-protected tables.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where logical replication was changed to run as the subscription owner. (confidence high, judge supported)
  - pg_release_notes@15: "Allow logical replication to run as the owner of the subscription"
- **[required] database** `present` `"tables with row-level security policies as logical replication subscription targets"`: The deployment uses logical replication (subscriptions) that replicate into tables with row-level security policies. (confidence high, judge supported)
  - pg_release_notes@15: "only superusers, roles with bypassrls, and table owners can replicate into tables with row-level security policies"
- **[required] database** `absent` `"superuser, bypassrls, or table ownership for the subscription owner"`: The subscription owner is not a superuser, does not have bypassrls, and does not own the target tables. (confidence low, judge supported)
  - pg_release_notes@15: "only superusers, roles with bypassrls, and table owners can replicate into tables with row-level security policies"
  - ⚠ The text does not state what error or failure mode occurs when the subscription owner lacks these privileges.

Actions:
- Identify subscriptions that replicate into tables with row-level security policies.
- Verify each such subscription owner is a superuser, has bypassrls, or owns the target tables; adjust ownership or role attributes if not.

### force_parallel_mode renamed to debug_parallel_query

`postgresql_c2bc60b77a` · medium · confidence medium · introduced in 16 · fires at upgrade

The server variable force_parallel_mode was renamed to debug_parallel_query in release 16. Configuration, scripts, or session code that sets force_parallel_mode under the old name needs to use the new name.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where force_parallel_mode was renamed to debug_parallel_query. (confidence high, judge supported)
  - pg_release_notes@16: "Rename server variable force_parallel_mode to debug_parallel_query"
- **[required] configuration** `present` `"force_parallel_mode"`: Configuration files, role/database settings, scripts, or application code reference the server variable force_parallel_mode. (confidence medium, judge supported)
  - pg_release_notes@16: "Rename server variable force_parallel_mode to debug_parallel_query"
  - ⚠ The text does not state whether the old name is still accepted as an alias or what error results from using it.

Actions:
- Search postgresql.conf, included config files, ALTER SYSTEM/ALTER ROLE/ALTER DATABASE settings, session SET statements, test harnesses, and connection options for force_parallel_mode.
- Replace force_parallel_mode with debug_parallel_query.

### Custom scan providers no longer assumed to support projections

`postgresql_c3d0f02569` · medium · confidence medium · introduced in 15 · fires at upgrade

In release 15, custom scan providers are assumed by default not to support projections. Providers that do support projections must be updated to indicate this. Otherwise they are treated as not supporting projections.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the default for custom scan provider projection support changed. (confidence high, judge supported)
  - pg_release_notes@15: "The default is now that custom scan providers are assumed to not support projections"
- **[required] dependency** `present` `"custom scan provider supporting projections"`: The deployment uses a custom scan provider (typically an extension or custom C code) that supports projections. (confidence medium, judge supported)
  - pg_release_notes@15: "those that do will need to be updated for this release"
  - ⚠ The text does not name the specific flag or API a provider must set to indicate projection support.
  - ⚠ The text does not state the consequence of not updating, only that the default is now no projection support.

Actions:
- Identify any extensions or code in the deployment that implement custom scan providers.
- For providers that support projections, update them for release 15 or later so they indicate projection support.
- Check with the extension vendor or maintainer for a release compatible with PostgreSQL 15 or later before upgrading.

### hash_mem_multiplier default increased to 2.0

`postgresql_c49690050a` · medium · confidence medium · introduced in 15 · fires at upgrade

The default hash_mem_multiplier is now 2.0, so query hash operations may use more memory than work_mem for other operations. Deployments that did not set hash_mem_multiplier explicitly and size memory around work_mem may see higher memory use per query.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the hash_mem_multiplier default was increased. (confidence high, judge supported)
  - pg_release_notes@15: "Increase hash_mem_multiplier default to 2.0"
- **[required] configuration** `absent` `"hash_mem_multiplier"`: The deployment relies on the default value of hash_mem_multiplier (does not set it explicitly in postgresql.conf, ALTER SYSTEM, per-role/database settings, or session settings). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Increase hash_mem_multiplier default to 2.0"
  - ⚠ The text does not state the previous default value.
- **[required] behavior** `present` `"work_mem"`: Workloads run queries with hash operations (e.g., hash joins or hash aggregates) and memory is sized based on work_mem. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "This allows query hash operations to use more work_mem memory than other operations."
  - ⚠ The text does not state how much total memory increase to expect or any failure mode.

Actions:
- Review memory capacity and work_mem sizing given that hash operations can use more memory than work_mem.
- If previous memory behavior is desired, set hash_mem_multiplier explicitly to the prior value in the configuration.
- Test representative hash-heavy queries under production-like concurrency after upgrading.

### Removed server parameter vacuum_cleanup_index_scale_factor

`postgresql_c57abe8742` · medium · confidence medium · introduced in 14 · fires at upgrade

The server parameter vacuum_cleanup_index_scale_factor was removed in release 14. It had already been ignored since 13.3, so setting it had no effect, but configuration that still sets it (e.g. in postgresql.conf, ALTER SYSTEM, ALTER DATABASE/ROLE SET, or connection options) references a parameter that no longer exists in the target version.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where vacuum_cleanup_index_scale_factor was removed (13 -> 16). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Remove server parameter vacuum_cleanup_index_scale_factor"
- **[required] configuration** `present` `"vacuum_cleanup_index_scale_factor"`: The deployment configuration sets the server parameter vacuum_cleanup_index_scale_factor (in postgresql.conf, postgresql.auto.conf, per-database/role settings, or startup/connection options). (confidence medium, judge supported)
  - pg_release_notes@14: "Remove server parameter vacuum_cleanup_index_scale_factor"
  - ⚠ The text does not state what happens when a removed parameter is still set (e.g. whether the server refuses to start or reports an error).
- **[optional] behavior** `greater_than` `"13.3"`: The setting is already ignored starting in PostgreSQL 13.3, so removing it does not change vacuum behavior on versions 13.3 and later. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "This setting was ignored starting in PostgreSQL version 13.3."

Actions:
- Remove vacuum_cleanup_index_scale_factor from postgresql.conf, postgresql.auto.conf (ALTER SYSTEM RESET), per-database/role settings, and any provisioning or config-management templates before upgrading to 16.

### Removed read-only server variables lc_collate and lc_ctype

`postgresql_cc8d8091c1` · medium · confidence medium · introduced in 16 · fires at upgrade

The read-only server variables lc_collate and lc_ctype are removed in release 16. Applications, scripts or monitoring that read them (e.g. via SHOW or current_setting) will no longer find these variables.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where lc_collate and lc_ctype are removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove read-only server variables lc_collate and lc_ctype"
- **[required] api_usage** `present` `"lc_collate|lc_ctype"`: Application code, scripts, or monitoring reference the server variable lc_collate or lc_ctype (e.g. SHOW lc_collate, current_setting('lc_collate')). (confidence medium, judge supported)
  - pg_release_notes@16: "Remove read-only server variables lc_collate and lc_ctype"
  - ⚠ The text does not state what error occurs when a removed variable is accessed, nor does it name a replacement.

Actions:
- Search application code, scripts, monitoring and configuration for references to lc_collate and lc_ctype and remove or replace them.
- Since collations and locales can vary between databases, obtain per-database locale settings from per-database metadata instead of a server variable.

### Regex character class with \w as range start or end now disallowed

`postgresql_f1a6f3c268` · medium · confidence medium · introduced in 14 · fires at first_use

Starting in release 14, PostgreSQL disallows \w as a range start or end in regular expression character classes. This was previously allowed but produced unexpected results. Patterns that use such a range will now be rejected, so queries or application code containing them need to be rewritten.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which disallows \w as a range start or end in regex character classes. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow \w as a range start or end in regular expression character classes"
- **[required] api_usage** `present` `"\\w as a range start or end within a regex character class"`: The application or database code uses regular expressions with \w as the start or end of a range inside a character class (e.g. [\w-x] or [a-\w]). (confidence medium, judge supported)
  - pg_release_notes@14: "Disallow \w as a range start or end in regular expression character classes"
  - ⚠ The text does not state whether the disallowed usage raises an error or what the exact failure mode is.

Actions:
- Search application code, SQL functions, views, constraints and queries for regex character classes where \w is used as a range start or end.
- Rewrite such patterns so \w is not used as a range endpoint, e.g. place \w separately in the class instead of as part of a range.
- Test affected regex patterns against a version 14+ server before upgrading.

### Custom options matching an installed extension name are deleted and cannot be created

`postgresql_f1bf63ef84` · medium · confidence medium · introduced in 15 · fires at first_use

Starting in release 15, custom options (custom GUC variables) whose names match an installed extension's name, but which are not variables declared by that extension, are deleted when the extension loads. New ones of that kind cannot be created later in the session. Applications or configurations that rely on such variables will lose them or fail to set them.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15 (13 -> 16), where this change was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "Disallow setting custom options that match the name of an installed extension, but are not one of the extension's declared variables"
- **[required] api_usage** `present` `"custom option named with an installed extension's name as prefix, not declared by the extension"`: The application or configuration sets custom options whose prefix matches the name of an installed extension but which are not variables declared by that extension. (confidence medium, judge supported)
  - pg_release_notes@15: "custom options that match the name of an installed extension, but are not one of the extension's declared variables"
  - ⚠ The text does not state the exact naming format of a matching option, such as an extension_name.variable prefix.
- **[required] behavior** `present` `"custom option set before the extension loads, or created after the extension is loaded in the session"`: The matching custom options are set before the extension is loaded, or an attempt is made to set them after the extension is loaded in the same session. (confidence high, judge supported)
  - pg_release_notes@15: "This change causes any such pre-existing variables to be deleted during extension load, and then prevents new ones from being created later in the session."

Actions:
- Search application code, role and database settings, and configuration for custom options whose names match installed extension names but are not declared by those extensions.
- Rename such custom options to a prefix that does not match an installed extension name.
- Test sessions that set such options before and after loading the extension on 16.

### New databases/clusters no longer grant PUBLIC CREATE on public schema

`postgresql_f731db1dff` · medium · confidence low · introduced in 15 · fires at first_use

From release 15, PUBLIC no longer has CREATE permission on the public schema in new clusters and in newly-created databases in existing clusters. Existing databases keep their permissions through upgrade or restore. Applications or provisioning scripts that create new databases (or new clusters) and expect ordinary users to create objects in the public schema will not get the earlier behavior unless CREATE is granted explicitly.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which changes the default for new clusters and newly-created databases. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "The change applies to new database clusters and to newly-created databases in existing clusters."
- **[required] database** `present` `"CREATE DATABASE or new cluster where non-owner roles create objects in public schema"`: The deployment creates new databases or new clusters after the upgrade, and non-owner roles rely on creating objects in the public schema of those databases. (confidence low, judge partially_supported)
  - pg_release_notes@15: "For new databases having no need to defend against insider threats, granting CREATE permission will yield the behavior of prior releases."
  - ⚠ The text does not describe the exact error that non-owner roles see when they try to create objects in the public schema.
- **[disqualifying] database** `absent` `"no newly-created databases or new clusters"`: If all databases used come only from upgrading a cluster or restoring a dump, they keep their existing public schema permissions, so this risk does not apply to them. (confidence high, judge supported)
  - pg_release_notes@15: "Upgrading a cluster or restoring a database dump will preserve public's existing permissions."

Actions:
- For newly created databases where non-owner roles need to create objects in the public schema, explicitly run GRANT CREATE ON SCHEMA public TO PUBLIC (or to specific roles) to get the behavior of prior releases.
- For existing databases, especially those with multiple users, consider REVOKE CREATE ON SCHEMA public FROM PUBLIC to adopt the new secure default.
- Review provisioning scripts and tests that create databases and then create objects in the public schema as non-owner roles.

### Zero-length Unicode identifiers U&"" now rejected

`postgresql_076d7c8e08` · low · confidence medium · introduced in 15 · fires at first_use

Release 15 disallows zero-length Unicode identifiers such as U&"". SQL that uses such an identifier (previously accepted) will now be rejected. Non-Unicode zero-length identifiers were already disallowed.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which disallows zero-length Unicode identifiers (13 -> 16 spans 15). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Disallow zero-length Unicode identifiers, e.g., U&"""
- **[required] api_usage** `present` `"U&\"\""`: Application SQL, schema definitions, or dumps contain a zero-length Unicode identifier such as U&"". (confidence medium, judge supported)
  - pg_release_notes@15: "Disallow zero-length Unicode identifiers, e.g., U&"""
  - ⚠ The text does not state the exact error or whether pre-15 servers accepted such identifiers in all contexts.

Actions:
- Search application SQL, migrations, and dump files for zero-length Unicode identifiers such as U&"" and replace them with valid non-empty identifiers.
- Test affected statements against a version 15+ server before upgrading.

### intarray containment operators no longer use GiST indexes

`postgresql_11b4c53a07` · low · confidence low · introduced in 14 · fires at upgrade

In release 14, the intarray containment operators <@ and @> no longer use GiST indexes and scan the heap instead. GiST indexes created only for these operators are no longer used and should be removed.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where this change was introduced (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@14: "Prevent the containment operators (<@ and @>) for intarray from using GiST indexes"
- **[required] database** `present` `"intarray"`: The intarray extension is installed in the database. (confidence high, judge supported)
  - pg_release_notes@14: "containment operators (<@ and @>) for intarray"
- **[required] database** `present` `"GiST index on intarray column used for <@ or @>"`: GiST indexes exist on integer array columns that were created to support <@ or @> queries. (confidence low, judge supported)
  - pg_release_notes@14: "Indexes created for this purpose should be removed."
  - ⚠ The text does not name the GiST operator classes (such as gist__int_ops), so identifying the affected indexes requires inference.
- **[optional] api_usage** `present` `"<@ or @>"`: Application queries use the intarray <@ or @> operators. (confidence high, judge supported)
  - pg_release_notes@14: "containment operators (<@ and @>) for intarray"

Actions:
- Find GiST indexes created for intarray <@ and @> queries and drop them.
- Confirm after the upgrade that queries using <@ and @> perform acceptably with heap scans.

### has_column_privilege() attribute-number checks on non-existent or dropped columns now return false

`postgresql_167726bd25` · low · confidence high · introduced in 14 · fires at first_use

In release 14, has_column_privilege() called with an attribute number for a non-existent or dropped column returns false. Previously such attribute numbers raised an invalid-column error. Code that relied on catching that error, or that assumes an error for such columns, will see different behavior after the upgrade from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which introduced the has_column_privilege() change. (confidence high)
  - pg_release_notes@14: "Return false for has_column_privilege() checks on non-existent or dropped columns when using attribute numbers"
- **[required] api_usage** `present` `"has_column_privilege"`: The application or database code calls has_column_privilege() with an attribute number (not a column name) as the column argument. (confidence high, judge supported)
  - pg_release_notes@14: "Return false for has_column_privilege() checks on non-existent or dropped columns when using attribute numbers"
- **[required] behavior** `present` `"non-existent or dropped column attribute number"`: The attribute number passed refers to a column that does not exist or has been dropped. (confidence high, judge supported)
  - pg_release_notes@14: "checks on non-existent or dropped columns when using attribute numbers"
- **[optional] behavior** `present` `"error handling dependent on invalid-column error"`: The application depends on the previous invalid-column error being raised, for example by catching it or treating it as a signal. (confidence low, judge partially_supported)
  - pg_release_notes@14: "Previously such attribute numbers returned an invalid-column error."
  - ⚠ The text does not state how the invalid-column error was surfaced or that applications rely on it.

Actions:
- Search application and SQL code for has_column_privilege() calls that pass attribute numbers.
- Update any logic that relied on the invalid-column error so it handles a false result for non-existent or dropped columns.
- Test has_column_privilege() with dropped or invalid attribute numbers against the target version.

### Interval justification functions now detect integer overflow

`postgresql_6642146d25` · low · confidence high · introduced in 15 · fires at first_use

Release 15 changed justify_interval(), justify_hours(), and justify_days() to detect integer overflow. The text does not say what happens when overflow is detected, so code or queries that pass extreme interval values to these functions may behave differently after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced overflow detection in the interval justification functions. (confidence high, judge supported)
  - pg_release_notes@15: "Detect integer overflow in interval justification functions"
- **[alternative] api_usage** `present` `"justify_interval"`: The application or database code calls justify_interval(). (confidence high, judge supported)
  - pg_release_notes@15: "The affected functions are justify_interval(), justify_hours(), and justify_days()."
- **[alternative] api_usage** `present` `"justify_hours"`: The application or database code calls justify_hours(). (confidence high, judge supported)
  - pg_release_notes@15: "The affected functions are justify_interval(), justify_hours(), and justify_days()."
- **[alternative] api_usage** `present` `"justify_days"`: The application or database code calls justify_days(). (confidence high, judge supported)
  - pg_release_notes@15: "The affected functions are justify_interval(), justify_hours(), and justify_days()."
- **[uncertain] behavior** `unknown` `"interval inputs large enough to overflow"`: The functions are called with interval values large enough to overflow an integer. (confidence low, judge partially_supported)
  - pg_release_notes@15: "Detect integer overflow in interval justification functions"
  - ⚠ The text does not say what happens when overflow is detected (for example, an error versus another result).
  - ⚠ The text does not say which input values trigger overflow.

Actions:
- Search application code, SQL, views and stored functions for justify_interval(), justify_hours() and justify_days().
- Test these calls against PostgreSQL 16 with extreme interval values and confirm the new overflow handling is acceptable.
- Add error handling or input validation where intervals may be very large.

### random() output changes for same seed

`postgresql_755a05d0ae` · low · confidence medium · introduced in 15 · fires at first_use

The algorithm used to compute random() was improved in release 15, so random() results differ from those of prior versions, even for the same seed value. Applications, tests or data-generation processes that rely on reproducible random() sequences from a given seed will see different values after upgrading.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the random() algorithm was changed (13 -> 16 spans 15). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Improve the algorithm used to compute random()"
- **[required] api_usage** `present` `"random()"`: The application, tests, or SQL scripts call random(), particularly depending on a seed value for reproducible results. (confidence medium, judge supported)
  - pg_release_notes@15: "This will cause random()'s results to differ from what was emitted by prior versions, even for the same seed value."
  - ⚠ The text does not mention setseed() explicitly; it only refers to 'the same seed value'.
- **[optional] behavior** `present` `"seed-dependent reproducible random() output"`: The application or tests depend on reproducible random() sequences for a given seed (e.g., golden-file tests or deterministic sampling). (confidence low, judge partially_supported)
  - pg_release_notes@15: "even for the same seed value"

Actions:
- Search application code, SQL functions, views and tests for random() usage.
- Do not rely on random() producing the same sequence for the same seed across versions; regenerate expected outputs or fixtures that depend on seeded random() results.
- Re-run tests that depend on seeded random() values after upgrading.

### tablefunc normal_rand() rejects negative values

`postgresql_85602454ed` · low · confidence low · introduced in 14 · fires at first_use

Starting in release 14, tablefunc's normal_rand() no longer accepts negative values. Code or tests that call normal_rand() with a negative value will now be rejected, which affects an upgrade from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where normal_rand() was changed to reject negative values. (confidence high, judge supported)
  - pg_release_notes@14: "Prevent tablefunc's function normal_rand() from accepting negative values"
- **[required] api_usage** `present` `"normal_rand"`: The application or database calls tablefunc's normal_rand(). (confidence high, judge supported)
  - pg_release_notes@14: "Prevent tablefunc's function normal_rand() from accepting negative values"
- **[required] behavior** `present` `"negative argument to normal_rand()"`: The calls to normal_rand() pass a negative value as an argument. (confidence low, judge partially_supported)
  - pg_release_notes@14: "Negative values produced undesirable results."
  - ⚠ The text does not say which argument(s) are affected or what normal_rand() does when it receives a negative value.

Actions:
- Find usages of normal_rand() in application code, SQL, views and functions.
- Make sure no caller passes a negative value to normal_rand().
- Test the affected queries on version 16 before upgrading.

### JSON numeric literal parsing changed to SQL/JSON standard (jsonpath)

`postgresql_90c31fa6ac` · low · confidence medium · introduced in 15 · fires at first_use

JSON numeric literal processing now matches the SQL/JSON standard. Formats like .1 and 1. are now accepted, and trailing junk after numeric literals, such as 1.type(), is now disallowed. Queries or code that relied on the previous parsing of such literals may behave differently or error.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the change in JSON numeric literal processing. (confidence high, judge supported)
  - pg_release_notes@15: "Adjust JSON numeric literal processing to match the SQL/JSON-standard"
- **[required] api_usage** `present` `"1.type()"`: The application uses JSON numeric literals with trailing junk after a numeric literal, such as 1.type(), in JSON path expressions or similar. (confidence medium, judge supported)
  - pg_release_notes@15: "disallows trailing junk after numeric literals, like 1.type()"
  - ⚠ The text does not name the specific functions or contexts (for example jsonpath) in which the numeric literal processing applies.
- **[optional] behavior** `present` `".1 or 1."`: The application relies on JSON numeric literals of the form .1 or 1. being rejected or interpreted differently, since these formats are now accepted. (confidence low, judge partially_supported)
  - pg_release_notes@15: "This accepts numeric formats like .1 and 1."
  - ⚠ The text does not state how these formats were handled in previous releases.

Actions:
- Search jsonpath expressions and JSON numeric literals for trailing characters after numeric literals, such as 1.type(), and rewrite them to valid forms.
- Test queries that use JSON numeric literals such as .1 and 1. against the new release to confirm the behavior is acceptable.

### Removal of version 2 wire protocol support in server and libpq

`postgresql_99cd4201b9` · low · confidence low · introduced in 14 · fires at upgrade

PostgreSQL 14 removed server and libpq support for the version 2 wire protocol. Clients that still speak protocol version 2 can no longer connect to the upgraded server. The text says this protocol was last the default in PostgreSQL 7.3 (2002), so the affected population is very small.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which removed server and libpq support for the version 2 wire protocol. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Remove server and libpq support for the version 2 wire protocol"
- **[required] api_usage** `present` `"version 2 wire protocol"`: An application, driver or client library connects to the server using the version 2 wire protocol, or is built against a libpq version that relies on it. (confidence low, judge supported)
  - pg_release_notes@14: "Remove server and libpq support for the version 2 wire protocol"
  - ⚠ The text does not say how a client can be identified as using protocol version 2, or what error occurs when it connects.
- **[disqualifying] behavior** `absent` `"clients that use protocol version 2"`: The clients in use are modern, since version 2 was last the default in PostgreSQL 7.3 (2002). (confidence low, judge partially_supported)
  - pg_release_notes@14: "This was last used as the default in PostgreSQL 7.3 (released in 2002)."
  - ⚠ The text does not state which client versions use a later protocol by default.

Actions:
- Identify any clients, drivers or tools that connect using the version 2 wire protocol and upgrade or reconfigure them to use a later protocol version before upgrading the server.
- Rebuild or upgrade any application linked against a very old libpq that depends on version 2 protocol support.

### chr() with negative argument now raises an error

`postgresql_9a56057ff7` · low · confidence medium · introduced in 15 · fires at first_use

Starting in release 15, chr() generates an error when supplied with a negative argument. Code or queries that call chr() with a negative value will now fail with an error instead of the prior behavior.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where chr() was changed to error on negative arguments (upgrade from 13 to 16). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Generate an error when chr() is supplied with a negative argument"
- **[required] api_usage** `present` `"chr("`: Application code, SQL queries, functions, or views call chr() and may pass a negative argument. (confidence medium, judge supported)
  - pg_release_notes@15: "Generate an error when chr() is supplied with a negative argument"
  - ⚠ The text does not state what chr() did previously with a negative argument.

Actions:
- Search application code, stored functions, and views for chr() calls.
- Ensure arguments passed to chr() cannot be negative, or validate/handle such values before calling chr().
- Test queries that use chr() with computed arguments against version 16.

### libpq and client programs now resolve the home directory from HOME

`postgresql_d48cf30f17` · low · confidence low · introduced in 15 · fires at upgrade

On non-Windows platforms, libpq and various client programs now consult the HOME environment variable to find the user's home directory. If HOME is empty or unset, they fall back to the previous <pwd.h> database lookup. Files resolved relative to the home directory, such as ~/.pgpass, may therefore be looked up in a different location than before when HOME is set and differs from the home directory in the passwd database.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the HOME-based home directory lookup (13 -> 16). (confidence high)
  - pg_release_notes@15: "consult the HOME environment variable to find the user's home directory"
- **[required] runtime** `not_equals` `"Windows"`: The client or application runs on a non-Windows platform. (confidence high, judge supported)
  - pg_release_notes@15: "On non-Windows platforms, consult the HOME environment variable"
- **[required] api_usage** `present` `".pgpass"`: The application or client programs use libpq or PostgreSQL client applications that resolve files relative to the user's home directory, such as ~/.pgpass. (confidence medium, judge supported)
  - pg_release_notes@15: "This change affects libpq (for example, while looking up ~/.pgpass) as well as various client application programs."
  - ⚠ The text does not list which client application programs are affected, or which other home-directory files besides ~/.pgpass are looked up.
- **[required] configuration** `present` `"HOME set to a directory different from the passwd home directory"`: HOME is set to a non-empty value that differs from the home directory recorded in the passwd database for the running user (for example under sudo, containers, or service managers). (confidence low, judge partially_supported)
  - pg_release_notes@15: "consult the HOME environment variable to find the user's home directory"
  - ⚠ The text does not explicitly say what happens when HOME and the passwd database disagree. This is inferred from the HOME-first lookup order.
- **[disqualifying] configuration** `absent` `"HOME unset or empty"`: If HOME is empty or unset, the lookup falls back to the previous <pwd.h> behavior, so the risk does not apply. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "If HOME is empty or unset, fall back to the previous method of checking the <pwd.h> database."

Actions:
- Check that HOME is set correctly for the users and service accounts that run libpq-based applications and PostgreSQL client programs.
- Verify that ~/.pgpass and other home-directory files are located where the HOME environment variable points.
- Where the location is ambiguous, set HOME explicitly or use PGPASSFILE to specify the password file path.

### var_samp/stddev_samp return NULL instead of NaN for single NaN numeric input

`postgresql_dc64bb7d33` · low · confidence high · introduced in 14 · fires at first_use

In release 14, var_samp() and stddev_samp() with numeric parameters return NULL when the input is a single NaN value, where NaN was previously returned. Applications that depend on a NaN result for this edge case may see different results after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which introduced this change. (confidence high, judge supported)
  - pg_release_notes@14: "Change var_samp() and stddev_samp() with numeric parameters to return NULL when the input is a single NaN value"
- **[required] api_usage** `present` `"var_samp|stddev_samp"`: The application calls var_samp() or stddev_samp() with numeric arguments. (confidence high, judge supported)
  - pg_release_notes@14: "Change var_samp() and stddev_samp() with numeric parameters to return NULL"
- **[required] behavior** `contains` `"single NaN numeric input"`: The input to the aggregate is a single NaN numeric value, for example a group containing exactly one row whose value is NaN. (confidence high, judge supported)
  - pg_release_notes@14: "when the input is a single NaN value"
- **[uncertain] behavior** `unknown` `"code expecting NaN result"`: Application code or downstream logic relies on a NaN result rather than NULL for this case. (confidence low, judge supported)
  - pg_release_notes@14: "Previously NaN was returned."
  - ⚠ The text does not say whether applications depend on NaN being returned.

Actions:
- Search application code, views, and queries for var_samp() and stddev_samp() on numeric columns that may hold NaN.
- Update result handling to treat NULL as the result for a single NaN input, for example by using COALESCE or an explicit NaN check if the old output is needed.
- Test affected queries against PostgreSQL 16 with single-NaN groups.

### SSL compression support removed

`postgresql_e068a86a55` · low · confidence low · introduced in 14 · fires at upgrade

Support for SSL compression is removed in PostgreSQL 14. The text says it was already disabled by default in previous releases and most modern OpenSSL and TLS versions no longer support it, so only deployments that explicitly enabled SSL compression are likely affected.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where SSL compression support was removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove support for SSL compression"
- **[required] configuration** `present` `"SSL compression enabled"`: The deployment relies on SSL compression for client or server connections, for example by explicitly enabling it. (confidence low, judge supported)
  - pg_release_notes@14: "Remove support for SSL compression"
  - pg_release_notes@14: "This was already disabled by default in previous PostgreSQL releases"
  - ⚠ The text does not state what happens (error or silent ignore) if a connection or configuration still requests SSL compression.
- **[optional] dependency** `present` `"OpenSSL/TLS version supporting compression"`: The deployment uses an OpenSSL/TLS version that still supports compression, so compression could actually have been in use. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "most modern OpenSSL and TLS versions no longer support it"

Actions:
- Search connection strings and client/server configuration for SSL compression settings (e.g. sslcompression) and remove them.
- Do not rely on SSL compression after upgrading; consider alternative approaches for reducing bandwidth if it was used.

### Removed composite types for sequences and toast tables

`postgresql_f785741bfd` · low · confidence low · introduced in 14 · fires at upgrade

PostgreSQL 14 removed the composite types that were formerly created for sequences and toast tables. Any application, query, or catalog-dependent tooling that references those composite row types would no longer find them after the upgrade. The text does not say which objects or names are affected beyond this.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14 (13 -> 16), where the composite types for sequences and toast tables were removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove the composite types that were formerly created for sequences and toast tables"
- **[required] database** `present` `"composite type for a sequence or toast table"`: The application, queries, or tooling reference the row/composite type of a sequence or toast table (for example, selecting a sequence as a composite type or looking up these types in pg_type). (confidence low, judge partially_supported)
  - pg_release_notes@14: "Remove the composite types that were formerly created for sequences and toast tables"
  - ⚠ The text does not state which usages (e.g. casts, function arguments, pg_type lookups) depended on these types.

Actions:
- Search application code, SQL, and catalog-inspecting tooling for references to the row types of sequences or toast tables and remove or rework them before upgrading.
- Test affected code against a PostgreSQL 14+ instance.

## Review checklist

### Low confidence or disputed

- [ ] postgresql_987fccfe8d: Legacy Boolean-like password_encryption values no longer accepted
- [ ] postgresql_20f9520b98: Role membership inheritance now set at GRANT time
- [ ] postgresql_2a6232c2c0: Removed postmaster binary symbolic link
- [ ] postgresql_2acbbca54c: operator_precedence_warning server parameter removed
- [ ] postgresql_5e13cfd71d: Login role no longer has implicit ADMIN OPTION on its own role membership
- [ ] postgresql_9d3f729496: Inherited/partitioned tables with mismatched GENERATED column status
- [ ] postgresql_b9ad526348: PL/pgSQL bound cursor variable string value no longer matches variable name
- [ ] postgresql_be61b83855: Logical replication into tables with row-level security policies now requires privileged subscription owner
- [ ] postgresql_f731db1dff: New databases/clusters no longer grant PUBLIC CREATE on public schema
- [ ] postgresql_11b4c53a07: intarray containment operators no longer use GiST indexes
- [ ] postgresql_85602454ed: tablefunc normal_rand() rejects negative values
- [ ] postgresql_99cd4201b9: Removal of version 2 wire protocol support in server and libpq
- [ ] postgresql_d48cf30f17: libpq and client programs now resolve the home directory from HOME
- [ ] postgresql_e068a86a55: SSL compression support removed
- [ ] postgresql_f785741bfd: Removed composite types for sequences and toast tables

### Inferred conditions

- [ ] postgresql_230760360c: The application does not use pipeline mode, or already uses PQsendQueryParams() in pipeline mode.
- [ ] postgresql_62a430b096: Failover or promotion tooling/scripts promote a standby by creating the trigger file rather than using pg_ctl promote or pg_promote().
- [ ] postgresql_9fbfbca3e1: The application already uses only <@ and @> instead of @ and ~.
- [ ] postgresql_063d5aa8bb: Clients or tooling that rely on md5-hashed password storage for new passwords (not stated by the text).
- [ ] postgresql_20f9520b98: Roles are created or altered with INHERIT/NOINHERIT attributes, or the application/migrations change a role's inheritance status after memberships exist.
- [ ] postgresql_20f9520b98: The deployment does not rely on any role membership inheritance (no GRANT of roles to other roles).
- [ ] postgresql_27194e765d: Results are persisted or compared against expected tsquery output (stored queries, expression indexes, tests) that rely on the old output.
- [ ] postgresql_28d15925c3: The application or its tests depend on the previous incorrect results from such queries.
- [ ] postgresql_2a6232c2c0: Deployment scripts, service definitions, or tooling invoke the binary through the 'postmaster' symbolic link name.
- [ ] postgresql_2acbbca54c: Configuration, role/database settings, or connection options set operator_precedence_warning.
- [ ] postgresql_40755c4ec6: Application logic or stored results depend on the previous result, such as 1.99 years being converted to 1 year 11 months.
- [ ] postgresql_4645b4b0d2: The application depends on \D or \W not matching newlines, for example by relying on the old match results.
- [ ] postgresql_5e13cfd71d: The role is explicitly granted ADMIN OPTION on its own membership, in which case the behavior is not lost.
- [ ] postgresql_9623a24b4c: The application or its tests depend on the exact tsquery output (e.g. the old 'aaa' <2> 'bbb' form) or on matching behavior derived from it.
- [ ] postgresql_9d3f729496: A parent/partitioned table column and the corresponding child/partition column differ in generation status (one generated, the other not).
- [ ] postgresql_b9ad526348: The code depends on the cursor variable's string value (portal name) matching the variable name, for example by referencing the portal by that name in FETCH/MOVE/CLOSE or in other sessions/statements.
- [ ] postgresql_be61b83855: The subscription owner is not a superuser, does not have bypassrls, and does not own the target tables.
- [ ] postgresql_f731db1dff: The deployment creates new databases or new clusters after the upgrade, and non-owner roles rely on creating objects in the public schema of those databases.
- [ ] postgresql_11b4c53a07: GiST indexes exist on integer array columns that were created to support <@ or @> queries.
- [ ] postgresql_167726bd25: The application depends on the previous invalid-column error being raised, for example by catching it or treating it as a signal.
- [ ] postgresql_6642146d25: The functions are called with interval values large enough to overflow an integer.
- [ ] postgresql_755a05d0ae: The application or tests depend on reproducible random() sequences for a given seed (e.g., golden-file tests or deterministic sampling).
- [ ] postgresql_85602454ed: The calls to normal_rand() pass a negative value as an argument.
- [ ] postgresql_90c31fa6ac: The application relies on JSON numeric literals of the form .1 or 1. being rejected or interpreted differently, since these formats are now accepted.
- [ ] postgresql_99cd4201b9: An application, driver or client library connects to the server using the version 2 wire protocol, or is built against a libpq version that relies on it.
- [ ] postgresql_99cd4201b9: The clients in use are modern, since version 2 was last the default in PostgreSQL 7.3 (2002).
- [ ] postgresql_d48cf30f17: HOME is set to a non-empty value that differs from the home directory recorded in the passwd database for the running user (for example under sudo, containers, or service managers).
- [ ] postgresql_dc64bb7d33: Application code or downstream logic relies on a NaN result rather than NULL for this case.
- [ ] postgresql_e068a86a55: The deployment relies on SSL compression for client or server connections, for example by explicitly enabling it.
- [ ] postgresql_f785741bfd: The application, queries, or tooling reference the row/composite type of a sequence or toast table (for example, selecting a sequence as a composite type or looking up these types in pg_type).

### Source disagreements


### Open questions

- Extensions (PostGIS, TimescaleDB, pg_partman, etc.) must have builds for the target major; their compatibility is not in core release notes.
- Backup and HA tooling (pgBackRest, Barman, Patroni, logical replication tools) and client drivers have their own version support.
- Managed services (RDS, Cloud SQL, Azure) control the upgrade method and some defaults.
- Minor-release notes (14.x, 15.x, 16.x) were intentionally excluded; they can contain post-release behavior fixes.
- [postgresql_987fccfe8d] Unconfirmed: The upgrade from 13 to 16 crosses release 14, where the legacy values stopped being accepted. (Judge: evidence does not support this claim. The quote only says the default of password_encryption changed to scram-sha-256 in release 14. It says nothing about legacy values ceasing to be accepted, )
- [postgresql_063d5aa8bb] Unconfirmed: Clients or tooling that rely on md5-hashed password storage for new passwords (not stated by the text). (The text does not say which clients or drivers are affected by the switch to SHA256 storage.)
- [postgresql_20f9520b98] Unconfirmed: The deployment does not rely on any role membership inheritance (no GRANT of roles to other roles). (Judge: evidence does not support this claim. The quote describes a behavior change for role inheritance during GRANT. It says nothing about deployments that do not use role membership, and the claim d)
- [postgresql_5e13cfd71d] Unconfirmed: The role is explicitly granted ADMIN OPTION on its own membership, in which case the behavior is not lost. (The text does not explicitly describe how to grant ADMIN OPTION explicitly as a remedy.)
- [postgresql_6642146d25] Unconfirmed: The functions are called with interval values large enough to overflow an integer. (The text does not say what happens when overflow is detected (for example, an error versus another result).)
- [postgresql_dc64bb7d33] Unconfirmed: Application code or downstream logic relies on a NaN result rather than NULL for this case. (The text does not say whether applications depend on NaN being returned.)

## Context facts (not risks)

- (14) A dump/restore using pg_dumpall or use of pg_upgrade or logical replication is required for those wishing to migrate data from any previous release. — _This item is the standard introduction to the Version 14 migration section. It says that moving data from any previous release needs a dump/restore with pg_dumpall, pg_upgrade, or logical replication, and it points to the general upgrading documentation. It names no specific API, setting, or behavior change. The specific incompatibilities are separate items and should be assessed on their own._
- (14) Process doubled quote marks in ecpg SQL command strings correctly (Tom Lane) Previously 'abc''def' was passed to the server as 'abc'def', and "abc""def" was passed as "abc"def", causing syntax errors. — _This is a bug fix in ecpg. Doubled quote marks in SQL command strings used to be passed to the server incorrectly and caused syntax errors, and they are now processed correctly. The text describes no failure, migration step, or required action for existing code at version 16._
- (15) A dump/restore using pg_dumpall or use of pg_upgrade or logical replication is required for those wishing to migrate data from any previous release. — _This item is the generic introduction to the Release 15 migration section. It says a major-version migration needs pg_dumpall dump/restore, pg_upgrade or logical replication, which is the normal procedure for any major upgrade. It names no specific API, setting or behavior, and it only says that version 15 has compatibility changes. Those changes (public schema permissions and ownership, exclusive backup mode removal, hash_mem_multiplier default, plpython2u/plpythonu removal) are separate items and should be assessed individually._
- (15) Change the owner of the public schema to be the new pg_database_owner role (Noah Misch) This allows each database's owner to have ownership privileges on the public schema within their database. — _The text says the new owner (pg_database_owner) applies only to new database clusters and newly-created databases in existing clusters. Upgrading a cluster or restoring a dump preserves the public schema's existing ownership. Databases migrated from 13 therefore keep their current ownership, and the item gives no required action or breakage for them._
- (15) Avoid unnecessary casting of constants in queries sent by postgres_fdw (Dian Fay) When column types are intentionally different between local and remote databases, such casts could cause errors. — _The item says postgres_fdw now avoids unnecessary casts of constants in queries it sends to the remote server. The text says such casts could cause errors when local and remote column types intentionally differ. This removes an error source, and the text names no required migration step, removed API, or changed setting. No action is needed at 16._
- (15) When EXPLAIN references the session's temporary object schema, refer to it as pg_temp (Amul Sul) Previously the actual schema name was reported, leading to inconsistencies across sessions. — _EXPLAIN output now shows pg_temp instead of the actual temporary schema name, a cosmetic output change that needs no user action._
- (16) A dump/restore using pg_dumpall or use of pg_upgrade or logical replication is required for those wishing to migrate data from any previous release. — _It is an introductory pointer that explains the migration paths and states that version 16 has incompatibilities listed below, with no specific action itself._

## Disqualified candidates


## Sources

| Source | Type | Tier | Status | Pinned ref |
|---|---|---|---|---|
| [pg_release_notes@14](https://www.postgresql.org/docs/release/14.0/) | official_release_notes | 1 | used | `branch:REL_14_STABLE` |
| [pg_release_notes@15](https://www.postgresql.org/docs/release/15.0/) | official_release_notes | 1 | used | `branch:REL_15_STABLE` |
| [pg_release_notes@16](https://www.postgresql.org/docs/release/16.0/) | official_release_notes | 1 | used | `branch:REL_16_STABLE` |

## What we trusted and what we did not

- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.
- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.
