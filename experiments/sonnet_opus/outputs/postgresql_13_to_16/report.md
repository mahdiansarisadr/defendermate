# PostgreSQL 13 → 16: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

PostgreSQL 13 -> 16 crosses 3 release(s) (14, 15, 16). 79 risk paths: 29 high, 25 medium, 25 low. Main risk types: changed_behavior (41), removed_api (30), changed_default (5). 0 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 11, "by_code": {"W4_no_search_queries": 11}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| high | medium | removed_api | deployment | 14 | `postgresql_01631e9f8c` pg_standby contrib program removed |
| high | high | removed_api | deployment | 15 | `postgresql_0aeb9394ab` pg_dump --no-synchronized-snapshots option removed |
| high | high | removed_api | application_code | 14 | `postgresql_12484be158` numeric_fac() function removed |
| high | medium | removed_api | application_code | 16 | `postgresql_14ae022ecb` Manual view creation via CREATE RULE ... ON SELECT removed |
| high | medium | removed_api | deployment | 15 | `postgresql_1c62b1411f` Exclusive backup mode removed |
| high | high | removed_api | database | 15 | `postgresql_1d037ae69b` plpython2u language removed |
| high | medium | removed_api | configuration | 16 | `postgresql_1f2cea1199` vacuum_defer_cleanup_age server variable removed |
| high | medium | removed_api | application_code | 15 | `postgresql_230760360c` PQsendQuery in libpq pipeline mode no longer supported |
| high | high | removed_api | deployment | 15 | `postgresql_272d063f3f` pg_start_backup/pg_stop_backup renamed |
| high | medium | removed_api | configuration | 14 | `postgresql_2acbbca54c` Removed server parameter operator_precedence_warning |
| high | medium | removed_api | configuration | 14 | `postgresql_336a22a4f4` clientcert numeric/no-verify values removed in pg_hba.conf |
| high | high | removed_api | application_code | 14 | `postgresql_345b3263a7` Single-quoted language name in CREATE/DROP LANGUAGE rejected |
| high | medium | removed_api | application_code | 16 | `postgresql_434e0c374b` pg_get_wal_records_info_till_end_of_wal removed |
| high | high | removed_api | application_code | 14 | `postgresql_601636b28d` Factorial operators ! and !! removed |
| high | medium | removed_api | configuration | 16 | `postgresql_62a430b096` promote_trigger_file server variable removed |
| high | medium | removed_api | database | 14 | `postgresql_6c2fefbf87` Postfix (right-unary) operators removed |
| high | high | changed_behavior | database | 15 | `postgresql_6fbb1043f0` Logical replication UPDATE/DELETE requires subscription owner SELECT permission |
| high | medium | removed_api | database | 15 | `postgresql_7bfe01bbb4` plpythonu generic language removed |
| high | medium | changed_behavior | configuration | 14 | `postgresql_8520f8afaf` clientcert=verify-ca disallowed with cert authentication |
| high | medium | changed_behavior | application_code | 14 | `postgresql_86d8236c5c` EXTRACT() returns numeric instead of float8 |
| high | medium | removed_api | application_code | 15 | `postgresql_91ba33fe94` pg_backup_start_time and pg_is_in_backup removed |
| high | low | removed_api | configuration | 14 | `postgresql_987fccfe8d` Legacy Boolean-like password_encryption values rejected |
| high | medium | removed_api | configuration | 15 | `postgresql_a1802b44d1` Removed server variable stats_temp_directory |
| high | medium | data_migration | database | 16 | `postgresql_af45c85281` Major-version data migration required (pg_dumpall, pg_upgrade or logical replication) |
| high | high | changed_behavior | database | 15 | `postgresql_b3c76f57c9` Logical replication apply runs as subscription owner; RLS-protected target tables require privileged owner |
| high | medium | removed_api | database | 14 | `postgresql_d00aff3b01_2` Removed @ and ~ containment operators in contrib cube, hstore, intarray, seg |
| high | medium | changed_behavior | database | 14 | `postgresql_d1320b72a5` User-defined aggregates/operators referencing built-in array functions with anyarray signatures |
| high | low | data_migration | database | 15 | `postgresql_d94a442769` Stored empty lexemes in tsvector data |
| high | medium | removed_api | application_code | 16 | `postgresql_f37345da94` pg_get_wal_stats_till_end_of_wal removed |
| medium | high | changed_default | configuration | 14 | `postgresql_063d5aa8bb` password_encryption default changed from md5 to scram-sha-256 |
| medium | low | changed_behavior | database | 16 | `postgresql_20f9520b98` Role inheritance status now fixed per membership at GRANT time |
| medium | medium | changed_behavior | database | 15 | `postgresql_24f3172f15` CREATE OR REPLACE VIEW can no longer change output column collation |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_27194e765d` to_tsquery/websearch_to_tsquery output changes for discarded tokens |
| medium | high | changed_behavior | deployment | 15 | `postgresql_2a4f5f5ead` psql --single-transaction no longer rolls back on error unless ON_ERROR_STOP is set |
| medium | medium | removed_api | deployment | 16 | `postgresql_2a6232c2c0` postmaster symlink removed |
| medium | medium | changed_default | dependencies | 15 | `postgresql_32c6a96fa1` Custom scan providers assumed not to support projections |
| medium | medium | removed_api | database | 15 | `postgresql_4345c09353` xml2 xml_is_well_formed() removed |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_4645b4b0d2` Regex \D and \W now match newlines in newline-sensitive mode |
| medium | medium | changed_behavior | deployment | 16 | `postgresql_55fa40f078` REINDEX DATABASE / reindexdb no longer reindex system catalog indexes |
| medium | medium | changed_behavior | configuration | 14 | `postgresql_5b9c633eb1` Custom server parameter names restricted to unquoted SQL identifier characters |
| medium | high | changed_behavior | database | 15 | `postgresql_5e13cfd71d` Login role can no longer manage members of its own role without ADMIN OPTION |
| medium | high | changed_behavior | database | 16 | `postgresql_5f2b8ce7c3` CREATEROLE roles lose ability to modify other roles without ADMIN OPTION |
| medium | medium | changed_behavior | configuration | 15 | `postgresql_5fd71eabce` Custom GUC options prefixed with an installed extension's name are deleted/rejected |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_6b7cd5683a` Numeric literals with trailing non-numeric characters now rejected |
| medium | high | changed_behavior | application_code | 15 | `postgresql_72e0855f91` array_to_tsvector() errors on empty-string array elements |
| medium | high | changed_behavior | application_code | 15 | `postgresql_755a05d0ae` random() output differs for same seed |
| medium | medium | configuration_change | configuration | 16 | `postgresql_892ed5d374` force_parallel_mode renamed to debug_parallel_query |
| medium | medium | changed_behavior | database | 15 | `postgresql_9564474ceb` Indexes on interval text output fail to create |
| medium | medium | changed_behavior | database | 16 | `postgresql_9d3f729496` Mismatched GENERATED status between parent/partitioned and child/partition columns rejected |
| medium | medium | changed_behavior | application_code | 16 | `postgresql_b9ad526348` PL/pgSQL bound cursor variable name no longer assigned at cursor assignment |
| medium | low | changed_default | configuration | 15 | `postgresql_c49690050a` hash_mem_multiplier default raised to 2.0 |
| medium | medium | removed_api | configuration | 14 | `postgresql_c57abe8742` Removed server parameter vacuum_cleanup_index_scale_factor |
| medium | medium | removed_api | application_code | 16 | `postgresql_cc8d8091c1` Removed read-only server variables lc_collate and lc_ctype |
| medium | low | changed_default | database | 15 | `postgresql_fcfbbf6b55` PUBLIC CREATE privilege removed from public schema in new clusters/databases |
| low | high | changed_behavior | database | 15 | `postgresql_0650d53bd7` postgres_fdw no longer casts constants in remote queries |
| low | high | changed_behavior | application_code | 15 | `postgresql_076d7c8e08` Zero-length Unicode identifiers (U&"") rejected |
| low | medium | changed_behavior | application_code | 14 | `postgresql_0e147761ab` factorial() of negative numbers now errors |
| low | medium | changed_behavior | database | 14 | `postgresql_11b4c53a07` intarray GiST indexes no longer used by <@ and @> containment operators |
| low | high | changed_behavior | application_code | 14 | `postgresql_167726bd25` has_column_privilege() with attribute numbers returns false instead of error |
| low | high | changed_behavior | application_code | 15 | `postgresql_1bae1f0746` EXPLAIN output reports temporary schema as pg_temp |
| low | medium | changed_behavior | application_code | 14 | `postgresql_28d15925c3` Window frame RANGE with infinite offsets returns different (corrected) results |
| low | high | changed_behavior | application_code | 14 | `postgresql_369e7506c5` ecpg doubled quote mark handling in SQL command strings |
| low | medium | removed_api | database | 16 | `postgresql_3d872e0449` Primary keys using NULLS NOT DISTINCT indexes are disallowed |
| low | medium | changed_behavior | application_code | 15 | `postgresql_3f790f697e` pg_statio_all_tables TOAST multi-index row aggregation change |
| low | medium | changed_behavior | application_code | 15 | `postgresql_40755c4ec6` Fractional interval input above months now rounds to nearest month |
| low | medium | changed_behavior | application_code | 14 | `postgresql_5e668838bc` Regex back-reference matching ignores constraints |
| low | medium | changed_behavior | application_code | 15 | `postgresql_614772dae3` JSON numeric literal trailing junk now rejected |
| low | medium | removed_api | database | 14 | `postgresql_62589404a7` Composite row types for sequences and toast tables removed |
| low | high | changed_behavior | application_code | 15 | `postgresql_6642146d25` Interval justification functions now detect integer overflow |
| low | medium | changed_behavior | database | 15 | `postgresql_72cf803a6f` "char" type output of non-ASCII bytes changed to octal escapes |
| low | medium | changed_behavior | application_code | 14 | `postgresql_85602454ed` tablefunc normal_rand() rejects negative values |
| low | medium | changed_behavior | application_code | 14 | `postgresql_9623a24b4c` websearch_to_tsquery adjacent discarded tokens in quotes now produce different tsquery |
| low | medium | removed_api | dependencies | 14 | `postgresql_99cd4201b9` Clients relying on version 2 wire protocol can no longer connect |
| low | medium | changed_behavior | application_code | 15 | `postgresql_9a56057ff7` chr() with negative argument now errors |
| low | low | changed_default | database | 15 | `postgresql_cfb6c3d3ce` public schema owned by pg_database_owner in new clusters/databases |
| low | low | changed_behavior | deployment | 15 | `postgresql_d48cf30f17` libpq and client programs resolve home directory from HOME instead of passwd database |
| low | high | changed_behavior | application_code | 14 | `postgresql_dc64bb7d33` var_samp/stddev_samp numeric single-NaN returns NULL |
| low | medium | changed_behavior | application_code | 14 | `postgresql_f1a6f3c268` Regex character class ranges using \w as start or end now rejected |
| low | low | removed_api | configuration | 14 | `postgresql_f7dd029384` SSL compression support removed |

### pg_standby contrib program removed

`postgresql_01631e9f8c` · high · confidence medium · introduced in 14 · fires at upgrade

The contrib program pg_standby was removed in PostgreSQL 14. Deployments that invoke pg_standby (e.g., in a standby restore_command) will break after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where pg_standby was removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove contrib program pg_standby (Justin Pryzby)"
- **[required] deployment** `present` `"pg_standby"`: The deployment invokes the pg_standby program (e.g., in scripts or recovery configuration). (confidence medium, judge supported)
  - pg_release_notes@14: "Remove contrib program pg_standby"
  - ⚠ The text does not name a replacement or state where pg_standby is typically configured.

Actions:
- Search scripts, restore_command settings and deployment manifests for pg_standby and remove or replace its usage before upgrading.
- Verify standby/recovery configuration works on the target version without pg_standby.

### pg_dump --no-synchronized-snapshots option removed

`postgresql_0aeb9394ab` · high · confidence high · introduced in 15 · fires at upgrade

pg_dump's --no-synchronized-snapshots option was removed in PostgreSQL 15. Scripts or tooling that invoke pg_dump with this option will fail when using the 15+ (here 16) pg_dump binary.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the option was removed. (confidence high, judge supported)
  - pg_release_notes@15: "Remove pg_dump's --no-synchronized-snapshots option (Tom Lane)"
- **[required] deployment** `present` `"--no-synchronized-snapshots"`: Backup scripts, cron jobs, or tooling invoke pg_dump with --no-synchronized-snapshots. (confidence high, judge supported)
  - pg_release_notes@15: "Remove pg_dump's --no-synchronized-snapshots option"

Actions:
- Remove --no-synchronized-snapshots from all pg_dump invocations in scripts, cron jobs, and container/job specs.
- Text states all still-supported server versions support synchronized snapshots, so the option is no longer needed.

### numeric_fac() function removed

`postgresql_12484be158` · high · confidence high · introduced in 14 · fires at upgrade

PostgreSQL 14 removes the numeric_fac() function. Calls to it will fail after upgrading. factorial() is still supported.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Upgrade crosses PostgreSQL release 14 (13 -> 16) (confidence high, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!, as well as function numeric_fac()"
- **[required] api_usage** `present` `"numeric_fac"`: Application SQL or database objects call numeric_fac() (confidence high, judge supported)
  - pg_release_notes@14: "as well as function numeric_fac()"

Actions:
- Replace numeric_fac(n) with factorial(n).

### Manual view creation via CREATE RULE ... ON SELECT removed

`postgresql_14ae022ecb` · high · confidence medium · introduced in 16 · fires at upgrade

PostgreSQL 16 removes the ability to create views manually with ON SELECT rules. Applications, migration scripts or schema tooling that convert tables into views by creating an ON SELECT rule will fail on 16.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, where manual view creation with ON SELECT rules is removed (confidence high, judge supported)
  - pg_release_notes@16: "Remove the ability to create views manually with ON SELECT rules"
- **[required] api_usage** `present` `"CREATE RULE ... ON SELECT"`: The application, schema migrations, or SQL scripts create ON SELECT rules to define views manually (confidence medium, judge supported)
  - pg_release_notes@16: "Remove the ability to create views manually with ON SELECT rules"
  - ⚠ The text does not say whether existing views or dumps from older releases that use such rules are handled automatically during dump/restore or pg_upgrade.

Actions:
- Search application code, migrations and SQL scripts for CREATE RULE ... ON SELECT statements and rewrite them to use CREATE VIEW (or CREATE OR REPLACE VIEW).
- Test schema migrations and restore scripts against a PostgreSQL 16 instance before upgrading.

### Exclusive backup mode removed

`postgresql_1c62b1411f` · high · confidence medium · introduced in 15 · fires at first_use

The long-deprecated exclusive backup mode was removed in PostgreSQL 15. Backup procedures relying on exclusive mode must switch to non-exclusive backup mode.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses release 15, where exclusive backup mode was removed (confidence high, judge supported)
  - pg_release_notes@15: "Remove long-deprecated exclusive backup mode"
- **[required] deployment** `present` `"exclusive backup mode"`: Backup procedures use exclusive backup mode (confidence medium, judge supported)
  - pg_release_notes@15: "Remove long-deprecated exclusive backup mode"
  - ⚠ The text does not describe how exclusive mode was invoked (e.g. specific function arguments), so detection by literal symbol is inferred.

Actions:
- Migrate backup procedures to non-exclusive backup mode using pg_backup_start()/pg_backup_stop().

### plpython2u language removed

`postgresql_1d037ae69b` · high · confidence high · introduced in 15 · fires at upgrade

PostgreSQL 15 removes the server-side language plpython2u; Python 2.x is no longer supported. Functions and extensions written in plpython2u will not work after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses PostgreSQL release 15, where plpython2u was removed (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu"
- **[required] database** `present` `"plpython2u"`: The database has the plpython2u language installed or functions written in plpython2u (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u"

Actions:
- Find all functions and extensions using plpython2u and port them to Python 3 under plpython3u before upgrading.
- Drop the plpython2u language/extension from the old cluster once migrated.

### vacuum_defer_cleanup_age server variable removed

`postgresql_1f2cea1199` · high · confidence medium · introduced in 16 · fires at upgrade

PostgreSQL 16 removes the server variable vacuum_defer_cleanup_age. Configurations or code that set it will no longer work after upgrading from 13. The text says hot_standby_feedback and replication slots made it unnecessary.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where vacuum_defer_cleanup_age is removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove the server variable vacuum_defer_cleanup_age (Andres Freund)"
- **[required] configuration** `present` `"vacuum_defer_cleanup_age"`: The deployment configuration or application code sets or references vacuum_defer_cleanup_age. (confidence medium, judge supported)
  - pg_release_notes@16: "Remove the server variable vacuum_defer_cleanup_age (Andres Freund)"
  - ⚠ The text does not state the exact failure mode (for example, a startup error or an ignored setting) when the removed variable is set.

Actions:
- Remove vacuum_defer_cleanup_age from postgresql.conf, postgresql.auto.conf, ALTER SYSTEM/ALTER DATABASE/ALTER ROLE settings, and application SET statements before upgrading.
- Use hot_standby_feedback and/or replication slots instead, as the release notes state these made vacuum_defer_cleanup_age unnecessary.

### PQsendQuery in libpq pipeline mode no longer supported

`postgresql_230760360c` · high · confidence medium · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, libpq's PQsendQuery() is no longer supported in pipeline mode. Applications calling PQsendQuery() while in pipeline mode must switch to PQsendQueryParams().

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where PQsendQuery() stopped being supported in pipeline mode. (confidence high, judge supported)
  - pg_release_notes@15: "libpq's PQsendQuery() function is no longer supported in pipeline mode"
- **[required] api_usage** `present` `"PQsendQuery"`: The application calls libpq's PQsendQuery() while the connection is in pipeline mode. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Applications that are using that combination will need to be modified to use PQsendQueryParams() instead."
  - ⚠ The text does not describe the exact failure behavior (error vs. other) when PQsendQuery() is used in pipeline mode.

Actions:
- Locate PQsendQuery() calls made while in pipeline mode (after PQenterPipelineMode()) and replace them with PQsendQueryParams().
- Test pipeline-mode code paths against a PostgreSQL 15+ libpq before upgrading.

### pg_start_backup/pg_stop_backup renamed

`postgresql_272d063f3f` · high · confidence high · introduced in 15 · fires at first_use

Functions pg_start_backup() and pg_stop_backup() were renamed to pg_backup_start() and pg_backup_stop() in PostgreSQL 15. Backup scripts or tools calling the old names will fail after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses release 15, where the functions were renamed (confidence high, judge supported)
  - pg_release_notes@15: "Functions pg_start_backup()/pg_stop_backup() have been renamed to pg_backup_start()/pg_backup_stop()"
- **[required] api_usage** `present` `"pg_start_backup"`: Backup scripts, tools or application code call pg_start_backup() or pg_stop_backup() (confidence high, judge supported)
  - pg_release_notes@15: "Functions pg_start_backup()/pg_stop_backup() have been renamed to pg_backup_start()/pg_backup_stop()"

Actions:
- Replace calls to pg_start_backup() with pg_backup_start() and pg_stop_backup() with pg_backup_stop().
- Update third-party backup tools to versions supporting PostgreSQL 15+ function names.

### Removed server parameter operator_precedence_warning

`postgresql_2acbbca54c` · high · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 removes the server parameter operator_precedence_warning. Configurations (postgresql.conf, ALTER SYSTEM, ALTER DATABASE/ROLE SET) or application sessions that set this parameter will fail on 14+.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where operator_precedence_warning was removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove server parameter operator_precedence_warning (Tom Lane)"
- **[required] configuration** `present` `"operator_precedence_warning"`: The deployment configuration or application code sets the operator_precedence_warning parameter. (confidence medium, judge supported)
  - pg_release_notes@14: "Remove server parameter operator_precedence_warning (Tom Lane)"
  - ⚠ The text does not state the exact failure mode (e.g., startup error vs. ignored) when the removed parameter is set.

Actions:
- Remove operator_precedence_warning from postgresql.conf, postgresql.auto.conf, and any ALTER SYSTEM/ALTER DATABASE/ALTER ROLE settings before upgrading.
- Remove any SET operator_precedence_warning statements or connection options from application code and drivers.

### clientcert numeric/no-verify values removed in pg_hba.conf

`postgresql_336a22a4f4` · high · confidence medium · introduced in 14 · fires at upgrade

In PostgreSQL 14, the clientcert option in pg_hba.conf no longer accepts 1, 0 or no-verify; only verify-ca and verify-full are accepted. pg_hba.conf entries using the old values must be changed.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the clientcert specification was overhauled (confidence high, judge supported)
  - pg_release_notes@14: "Overhaul the specification of clientcert in pg_hba.conf"
- **[required] configuration** `present` `"clientcert=1|clientcert=0|clientcert=no-verify"`: pg_hba.conf contains a clientcert option set to 1, 0 or no-verify (confidence medium, judge supported)
  - pg_release_notes@14: "Values 1/0/no-verify are no longer supported; only the strings verify-ca and verify-full can be used."
  - ⚠ The text does not state how the server reacts to the unsupported values (e.g. whether pg_hba.conf fails to load).

Actions:
- Replace clientcert=1 with clientcert=verify-ca or clientcert=verify-full in pg_hba.conf.
- Review clientcert=0 and clientcert=no-verify entries, since only verify-ca and verify-full are accepted values.

### Single-quoted language name in CREATE/DROP LANGUAGE rejected

`postgresql_345b3263a7` · high · confidence high · introduced in 14 · fires at first_use

Starting in PostgreSQL 14, CREATE LANGUAGE and DROP LANGUAGE no longer accept a single-quoted language name. Scripts, migrations or dumps that quote the language name with single quotes will fail.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where single-quoting of the language name was disallowed (confidence high, judge supported)
  - pg_release_notes@14: "Disallow single-quoting of the language name in the CREATE/DROP LANGUAGE command"
- **[required] api_usage** `present` `"CREATE/DROP LANGUAGE '<name>'"`: Application SQL, migrations or scripts use CREATE LANGUAGE or DROP LANGUAGE with a single-quoted language name (confidence high, judge supported)
  - pg_release_notes@14: "Disallow single-quoting of the language name in the CREATE/DROP LANGUAGE command"

Actions:
- Remove the single quotes around language names in CREATE LANGUAGE and DROP LANGUAGE statements, using unquoted or double-quoted identifiers instead.

### pg_get_wal_records_info_till_end_of_wal removed

`postgresql_434e0c374b` · high · confidence medium · introduced in 16 · fires at upgrade

The pg_walinspect function pg_get_wal_records_info_till_end_of_wal() is removed in PostgreSQL 16; calls to it will fail after upgrade.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: Upgrade crosses release 16, where the function was removed (confidence high, judge supported)
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal()"
- **[required] api_usage** `present` `"pg_get_wal_records_info_till_end_of_wal"`: Application or scripts call pg_get_wal_records_info_till_end_of_wal() (confidence medium, judge supported)
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal()"
  - ⚠ The text does not name a replacement function.

Actions:
- Find and remove or rewrite calls to pg_get_wal_records_info_till_end_of_wal() before upgrading to 16.

### Factorial operators ! and !! removed

`postgresql_601636b28d` · high · confidence high · introduced in 14 · fires at upgrade

PostgreSQL 14 removes the postfix factorial operator ! and prefix factorial operator !!. SQL or database objects that use them will fail after upgrading. Use factorial() instead.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Upgrade crosses PostgreSQL release 14 (13 -> 16) (confidence high, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!, as well as function numeric_fac()"
- **[required] api_usage** `present` `"!"`: Application SQL, views, functions or other database objects use the factorial operators ! or !! (confidence high, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!"

Actions:
- Replace uses of n! and !!n with factorial(n), which is still supported.
- Find and recreate views, functions and other database objects that reference ! or !! before upgrading.

### promote_trigger_file server variable removed

`postgresql_62a430b096` · high · confidence medium · introduced in 16 · fires at upgrade

PostgreSQL 16 removes the server variable promote_trigger_file. Standby configurations that set it, or failover tooling that promotes a standby by creating the trigger file, will no longer work. Promotion must use pg_ctl promote or pg_promote().

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where promote_trigger_file is removed (confidence high, judge supported)
  - pg_release_notes@16: "Remove server variable promote_trigger_file (Simon Riggs)"
- **[required] configuration** `present` `"promote_trigger_file"`: The deployment sets promote_trigger_file in its server configuration, or relies on it to promote a standby (confidence medium, judge supported)
  - pg_release_notes@16: "This was used to promote a standby to primary"
  - ⚠ The text does not say whether a leftover setting causes a server startup error or is ignored.

Actions:
- Remove promote_trigger_file from postgresql.conf, postgresql.auto.conf and any config templates before upgrading.
- Update failover and HA tooling to promote standbys with pg_ctl promote or SELECT pg_promote() instead of creating a trigger file.
- Test standby promotion on a version 16 environment.

### Postfix (right-unary) operators removed

`postgresql_6c2fefbf87` · high · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 removes support for postfix (right-unary) operators. User-defined postfix operators, and any SQL that uses them, will no longer work. pg_dump and pg_upgrade only warn when such operators are being dumped.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Upgrade crosses PostgreSQL release 14, where postfix operator support was removed (confidence high, judge supported)
  - pg_release_notes@14: "Remove support for postfix (right-unary) operators"
- **[required] database** `present` `"postfix (right-unary) operator"`: The database defines postfix (right-unary) operators (confidence medium, judge supported)
  - pg_release_notes@14: "pg_dump and pg_upgrade will warn if postfix operators are being dumped."
  - ⚠ The text does not state whether dump/restore or pg_upgrade fails or merely warns and drops the operator. It only says they will warn.
- **[optional] api_usage** `present` `"postfix operator usage"`: Application SQL uses postfix operator syntax (e.g., factorial `n !`) (confidence low, judge partially_supported)
  - pg_release_notes@14: "Remove support for postfix (right-unary) operators"
  - ⚠ The text does not name specific built-in postfix operators that were removed.

Actions:
- Before upgrading, query pg_operator for postfix operators (oprright = 0) and drop or redefine them, e.g. as prefix operators or functions.
- Update application SQL that uses postfix operator syntax.
- Review pg_dump/pg_upgrade warnings about postfix operators during migration.

### Logical replication UPDATE/DELETE requires subscription owner SELECT permission

`postgresql_6fbb1043f0` · high · confidence high · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, logical replication UPDATE and DELETE operations are prevented on tables where the subscription owner lacks SELECT permission on the table. Subscriptions whose owners have only INSERT/UPDATE/DELETE privileges will fail to apply UPDATE/DELETE changes after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where this restriction was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent UPDATE and DELETE logical replication operations on tables where the subscription owner does not have SELECT permission on the table"
- **[required] database** `present` `"pg_subscription"`: The deployment uses logical replication subscriptions that apply UPDATE or DELETE operations. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent UPDATE and DELETE logical replication operations"
- **[required] database** `absent` `"SELECT"`: The subscription owner does not have SELECT permission on the replicated target tables. (confidence high, judge supported)
  - pg_release_notes@15: "require the subscription owner to have table SELECT permission"

Actions:
- Before upgrading, identify each subscription owner and the tables in its subscriptions.
- Grant SELECT on all replicated target tables to the subscription owner (e.g. GRANT SELECT ON <table> TO <subscription_owner>).
- After the upgrade, monitor subscriber logs for permission errors during the apply of UPDATE/DELETE operations.

### plpythonu generic language removed

`postgresql_7bfe01bbb4` · high · confidence medium · introduced in 15 · fires at upgrade

PostgreSQL 15 removes the generic Python language plpythonu. It was not changed to point to plpython3u; it was simply removed, so objects using plpythonu will break.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses PostgreSQL release 15, where plpythonu was removed (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu"
- **[required] database** `present` `"plpythonu"`: The database has the plpythonu language installed or functions or DDL scripts using LANGUAGE plpythonu (confidence medium, judge partially_supported)
  - pg_release_notes@15: "generic Python language plpythonu"
- **[optional] behavior** `absent` `"plpythonu"`: plpythonu was not redirected to plpython3u; it was removed (confidence medium, judge partially_supported)
  - pg_release_notes@15: "changing it now seems more likely to cause problems than solve them, so it's just been removed"

Actions:
- Rewrite functions and DDL scripts using LANGUAGE plpythonu to use plpython3u, porting any Python 2 code to Python 3.
- Remove plpythonu from the old cluster before upgrading.

### clientcert=verify-ca disallowed with cert authentication

`postgresql_8520f8afaf` · high · confidence medium · introduced in 14 · fires at upgrade

In PostgreSQL 14, clientcert=verify-ca is disallowed on pg_hba.conf entries using the cert authentication method, because cert requires verify-full checking.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the clientcert specification was overhauled (confidence high, judge supported)
  - pg_release_notes@14: "Overhaul the specification of clientcert in pg_hba.conf"
- **[required] configuration** `present` `"cert clientcert=verify-ca"`: pg_hba.conf has an entry using the cert authentication method together with clientcert=verify-ca (confidence medium, judge supported)
  - pg_release_notes@14: "disallow verify-ca if cert authentication is enabled since cert requires verify-full checking"
  - ⚠ The text does not state the exact failure mode when the disallowed combination is present.

Actions:
- For pg_hba.conf entries using cert authentication, remove clientcert=verify-ca or change it to clientcert=verify-full.

### EXTRACT() returns numeric instead of float8

`postgresql_86d8236c5c` · high · confidence medium · introduced in 14 · fires at upgrade

Starting in PostgreSQL 14, EXTRACT() returns numeric rather than float8. Code or client drivers that depend on the float8 result type may behave differently. The old behavior is still available through date_part().

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where EXTRACT() changed its return type. (confidence high, judge supported)
  - pg_release_notes@14: "Change EXTRACT() to return type numeric instead of float8"
  - pg_release_notes@14: "EXTRACT(date) now throws an error for units that are not part of the date data type"
- **[required] api_usage** `present` `"EXTRACT("`: The application or database objects use EXTRACT(). (confidence medium, judge supported)
  - pg_release_notes@14: "Change EXTRACT() to return type numeric instead of float8"
  - pg_release_notes@14: "EXTRACT(date) now throws an error for units that are not part of the date data type"
  - ⚠ The text does not say which downstream usages break. Only the type change is stated.
  - ⚠ The text does not list which units are considered not part of the date data type.

Actions:
- Review code that consumes EXTRACT() results and check that it handles numeric correctly (client type mapping, casts, comparisons).
- Where float8 behavior is needed, use date_part() instead of EXTRACT(), or cast the result explicitly.
- Find EXTRACT calls on date values that use time-of-day or other non-date units. Cast the input to timestamp, or use only date units.
- Consider date_part() where the old behavior is required.

### pg_backup_start_time and pg_is_in_backup removed

`postgresql_91ba33fe94` · high · confidence medium · introduced in 15 · fires at first_use

Functions pg_backup_start_time() and pg_is_in_backup() were removed in PostgreSQL 15. Monitoring or backup scripts calling them will fail after upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses release 15, where these functions were removed (confidence high, judge supported)
  - pg_release_notes@15: "the functions pg_backup_start_time() and pg_is_in_backup() have been removed"
- **[required] api_usage** `present` `"pg_is_in_backup"`: Code, monitoring or scripts call pg_backup_start_time() or pg_is_in_backup() (confidence medium, judge supported)
  - pg_release_notes@15: "the functions pg_backup_start_time() and pg_is_in_backup() have been removed"
  - ⚠ The text names no replacement for these functions.

Actions:
- Remove or replace calls to pg_backup_start_time() and pg_is_in_backup() in monitoring and backup scripts.

### Legacy Boolean-like password_encryption values rejected

`postgresql_987fccfe8d` · high · confidence low · introduced in 14 · fires at upgrade

Starting in release 14, password_encryption no longer accepts the legacy, undocumented Boolean-like values that were previously synonyms for md5. Configurations using such values will be rejected.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where legacy Boolean-like values for password_encryption stopped being accepted. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "the legacy (and undocumented) Boolean-like values which were previously synonyms for md5 are no longer accepted"
- **[required] configuration** `present` `"password_encryption = on|true|yes|1|off|false|no|0"`: password_encryption is set to a legacy Boolean-like value, such as on, off, true, false, yes, no, 1 or 0. (confidence low, judge partially_supported)
  - pg_release_notes@14: "Boolean-like values which were previously synonyms for md5 are no longer accepted"
  - ⚠ The text does not list the specific Boolean-like values; the list in this condition is inferred.
  - ⚠ The text does not say whether the server fails to start or only rejects the setting at SET time.

Actions:
- Replace any Boolean-like password_encryption value with md5 or scram-sha-256 before upgrading.

### Removed server variable stats_temp_directory

`postgresql_a1802b44d1` · high · confidence medium · introduced in 15 · fires at upgrade

PostgreSQL 15 removes the obsolete server variable stats_temp_directory. Configurations that set it may fail to load after upgrading to 16, and scripts or queries that reference it may break.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15 (13 -> 16), where stats_temp_directory was removed (confidence high, judge supported)
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
- **[required] configuration** `present` `"stats_temp_directory"`: The server configuration, deployment manifests or application code reference stats_temp_directory (confidence medium, judge supported)
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
  - ⚠ The text does not state the exact failure mode (startup error vs. warning) when the variable is still set.

Actions:
- Remove stats_temp_directory from postgresql.conf, postgresql.auto.conf (ALTER SYSTEM RESET stats_temp_directory), Helm values, ConfigMaps and operator specs before upgrading.
- Remove any monitoring or scripts that query or SET stats_temp_directory.
- Remove any tmpfs mounts dedicated to the stats temp directory if they exist only for this setting.

### Major-version data migration required (pg_dumpall, pg_upgrade or logical replication)

`postgresql_af45c85281` · high · confidence medium · introduced in 16 · fires at upgrade

Moving to PostgreSQL 16 from any previous release requires migrating the data with a dump/restore using pg_dumpall, pg_upgrade, or logical replication. Existing data from the 13 cluster cannot be carried over without one of these steps.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade moves from a release before 16 to release 16, which requires a data migration step. (confidence medium, judge supported)
  - pg_release_notes@16: "A dump/restore using pg_dumpall or use of pg_upgrade or logical replication is required for those wishing to migrate data from any previous release."
  - pg_release_notes@14: "for those wishing to migrate data from any previous release"
  - pg_release_notes@15: "required for those wishing to migrate data from any previous release"
  - ⚠ History: in 14, 'Major version data migration required (pg_dumpall, pg_upgrade or logical replication)' applied to the same symbol (pg_upgrade); superseded by the 16 change (R2).
  - ⚠ History: in 15, 'Major-version data migration required (dump/restore, pg_upgrade, or logical replication)' applied to the same symbol (pg_upgrade); superseded by the 16 change (R2).
- **[required] deployment** `present` `"existing pre-16 data directory/cluster to migrate"`: The deployment has existing data in a pre-16 cluster that must be carried over to the new release. (confidence high, judge supported)
  - pg_release_notes@16: "required for those wishing to migrate data from any previous release"

Actions:
- Plan the data migration using pg_dumpall dump/restore, pg_upgrade, or logical replication before moving to PostgreSQL 16.
- Review the general upgrading documentation for migrating to new major releases.
- Review the listed version 16 incompatibilities before migrating.

### Logical replication apply runs as subscription owner; RLS-protected target tables require privileged owner

`postgresql_b3c76f57c9` · high · confidence high · introduced in 15 · fires at upgrade

Starting in PostgreSQL 15, logical replication runs as the owner of the subscription. Row-level security policies are not checked during apply, so only superusers, roles with bypassrls, and table owners can replicate into tables that have row-level security policies. Subscriptions owned by other roles that replicate into RLS-protected tables will be unable to replicate into them.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where logical replication began running as the subscription owner. (confidence high, judge supported)
  - pg_release_notes@15: "Allow logical replication to run as the owner of the subscription"
- **[required] deployment** `present` `"pg_subscription"`: The deployment uses logical replication subscriptions on the subscriber side. (confidence high, judge supported)
  - pg_release_notes@15: "Allow logical replication to run as the owner of the subscription"
- **[required] database** `present` `"relrowsecurity = true"`: Replicated target tables on the subscriber have row-level security policies. (confidence high, judge supported)
  - pg_release_notes@15: "only superusers, roles with bypassrls, and table owners can replicate into tables with row-level security policies"
- **[required] database** `equals` `"rolsuper = false AND rolbypassrls = false AND not table owner"`: The subscription owner is not a superuser, does not have bypassrls, and does not own the RLS-protected target tables. (confidence high, judge supported)
  - pg_release_notes@15: "only superusers, roles with bypassrls, and table owners can replicate into tables with row-level security policies"
- **[uncertain] database** `unknown` `"INSERT/UPDATE/DELETE privileges on target tables"`: The subscription owner may also need ordinary privileges on target tables now that apply runs as that role. (confidence low, judge partially_supported)
  - pg_release_notes@15: "Allow logical replication to run as the owner of the subscription"
  - ⚠ The text only states the row-level security restriction; it does not explicitly state other privilege checks on target tables.

Actions:
- Before upgrading, list subscriptions and their owners and identify replicated target tables with row-level security enabled.
- For affected subscriptions, make the subscription owner a superuser, grant it BYPASSRLS, or make it the owner of the RLS-protected target tables (e.g. ALTER SUBSCRIPTION ... OWNER TO ... / ALTER ROLE ... BYPASSRLS).
- After upgrading, monitor subscriber logs and pg_stat_subscription for apply errors.

### Removed @ and ~ containment operators in contrib cube, hstore, intarray, seg

`postgresql_d00aff3b01_2` · high · confidence medium · introduced in 14 · fires at upgrade

Release 14 removes the deprecated containment operators @ and ~ from the contrib modules cube, hstore, intarray, and seg. Queries or stored objects that use these operators with those extensions' types will no longer work after upgrading from 13 to 16; <@ and @> are the recommended replacements.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the @ and ~ containment operators were removed from these contrib modules. (confidence high, judge supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types and contrib modules cube, hstore, intarray, and seg"
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types"
- **[required] dependency** `present` `"cube, hstore, intarray, or seg extension"`: The database has one or more of the cube, hstore, intarray, or seg extensions installed. (confidence high, judge supported)
  - pg_release_notes@14: "contrib modules cube, hstore, intarray, and seg"
- **[required] api_usage** `present` `"@ or ~ operator on cube, hstore, intarray (int[]), or seg values"`: The application or database objects use the @ or ~ containment operators provided by these modules. (confidence medium, judge supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types and contrib modules cube, hstore, intarray, and seg"
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types"
  - ⚠ The text does not say which old operator corresponds to <@ versus @>, so the exact rewrite of each usage must be determined separately.

Actions:
- Rewrite usages of @ and ~ with cube, hstore, intarray, and seg types to the replacement operators <@ and @> before upgrading.
- Recreate any views, functions, or indexes that reference the removed operators so they use <@ and @>.
- Rewrite usages of @ and ~ on geometric types to the replacement operators <@ and @> before upgrading.

### User-defined aggregates/operators referencing built-in array functions with anyarray signatures

`postgresql_d1320b72a5` · high · confidence medium · introduced in 14 · fires at upgrade

In PostgreSQL 14, array_append(), array_prepend(), array_cat(), array_position(), array_positions(), array_remove(), array_replace(), and width_bucket() changed from anyarray arguments to anycompatiblearray arguments. User-defined objects such as aggregates and operators that reference those function signatures must be dropped before upgrading and recreated once the upgrade completes.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where these array functions changed from anyarray to anycompatiblearray arguments. (confidence high, judge supported)
  - pg_release_notes@14: "used to take anyarray arguments but now take anycompatiblearray"
- **[required] database** `present` `"user-defined aggregate or operator referencing array_append/array_prepend/array_cat/array_position/array_positions/array_remove/array_replace/width_bucket"`: The database contains user-defined objects (e.g. aggregates or operators) that reference the anyarray signatures of array_append, array_prepend, array_cat, array_position, array_positions, array_remove, array_replace, or width_bucket. (confidence medium, judge supported)
  - pg_release_notes@14: "user-defined objects like aggregates and operators that reference those array function signatures must be dropped before upgrading"
  - pg_release_notes@14: "array_append(), array_prepend(), array_cat(), array_position(), array_positions(), array_remove(), array_replace(), and width_bucket()"
  - ⚠ The text says 'objects like aggregates and operators', so other kinds of user-defined objects referencing these signatures may also be affected; the text does not enumerate them.
  - ⚠ The text does not state the exact failure mode if the objects are not dropped before upgrading.

Actions:
- Before upgrading, identify user-defined aggregates and operators that reference array_append, array_prepend, array_cat, array_position, array_positions, array_remove, array_replace, or width_bucket.
- Drop those user-defined objects before upgrading and save their definitions.
- After the upgrade completes, recreate the objects against the new anycompatiblearray signatures.

### Stored empty lexemes in tsvector data

`postgresql_d94a442769` · high · confidence low · introduced in 15 · fires at upgrade

Empty lexemes are now prohibited. Users of earlier releases should check that no empty lexemes are stored, because they can cause dump/restore failures and inconsistent results.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases"
- **[required] database** `present` `"empty lexeme in stored tsvector"`: The database contains stored tsvector values that include empty lexemes. (confidence low, judge supported)
  - pg_release_notes@15: "Users of previous Postgres releases should verify that no empty lexemes are stored"
  - ⚠ The text does not say which data types or columns could hold empty lexemes; tsvector columns are inferred as the storage location.
- **[optional] deployment** `equals` `"dump/restore"`: Data is migrated by dump/restore, where empty lexemes can cause failures. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "they can lead to dump/restore failures and inconsistent results"
  - ⚠ The text does not say whether pg_upgrade or logical replication are affected the same way.

Actions:
- Before upgrading, scan all tsvector columns for empty lexemes and remove or fix them.
- Fix any application paths that produce empty lexemes.

### pg_get_wal_stats_till_end_of_wal removed

`postgresql_f37345da94` · high · confidence medium · introduced in 16 · fires at upgrade

The pg_walinspect function pg_get_wal_stats_till_end_of_wal() is removed in PostgreSQL 16; calls to it will fail after upgrade.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: Upgrade crosses release 16, where the function was removed (confidence high, judge supported)
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal()"
- **[required] api_usage** `present` `"pg_get_wal_stats_till_end_of_wal"`: Application or scripts call pg_get_wal_stats_till_end_of_wal() (confidence medium, judge partially_supported)
  - pg_release_notes@16: "and pg_get_wal_stats_till_end_of_wal() (Bharath Rupireddy)"
  - ⚠ The text does not name a replacement function.

Actions:
- Find and remove or rewrite calls to pg_get_wal_stats_till_end_of_wal() before upgrading to 16.

### password_encryption default changed from md5 to scram-sha-256

`postgresql_063d5aa8bb` · medium · confidence high · introduced in 14 · fires at rotation

Starting in release 14, password_encryption defaults to scram-sha-256 instead of md5. Deployments that rely on the default will store all new or changed passwords as SCRAM-SHA-256. This applies unless the setting is changed or the password is supplied already in MD5 format. Clients or tooling that expect md5-stored passwords may be affected when passwords are set or rotated.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the password_encryption default changed to scram-sha-256. (confidence high, judge supported)
  - pg_release_notes@14: "Change the default of the password_encryption server parameter to scram-sha-256"
- **[required] configuration** `absent` `"password_encryption"`: The deployment relies on the default value of password_encryption, which was previously md5, and does not set it explicitly. (confidence high, judge supported)
  - pg_release_notes@14: "Previously it was md5."
  - pg_release_notes@14: "All new passwords will be stored as SHA256 unless this server setting is changed"
- **[disqualifying] configuration** `equals` `"md5"`: The deployment explicitly sets password_encryption to md5. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "unless this server setting is changed or the password is specified in MD5 format"
- **[disqualifying] behavior** `present` `"md5"`: Passwords are supplied to the server pre-hashed in MD5 format. (confidence high, judge supported)
  - pg_release_notes@14: "the password is specified in MD5 format"
- **[uncertain] dependency** `present` `"md5"`: Clients, drivers, or authentication configuration depend on md5-stored passwords and may fail once passwords are stored as SCRAM-SHA-256. (confidence low, judge partially_supported)
  - pg_release_notes@14: "All new passwords will be stored as SHA256"
  - ⚠ The text does not describe any client compatibility or authentication impact; this impact is inferred.

Actions:
- Decide whether to keep md5 by explicitly setting password_encryption = md5, or adopt scram-sha-256.
- Verify that client drivers support SCRAM-SHA-256 before setting or rotating passwords on the upgraded cluster.

### Role inheritance status now fixed per membership at GRANT time

`postgresql_20f9520b98` · medium · confidence low · introduced in 16 · fires at upgrade

In PostgreSQL 16 a role's inheritance attribute only sets the default inheritance status for member roles added during GRANT; the status is stored per membership at GRANT time. Previously, changing a role's inheritance status affected all previous and future memberships, so scripts or procedures that toggle role INHERIT/NOINHERIT to change privilege inheritance of existing memberships will no longer have that effect.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, where role inheritance became the default for member roles added during GRANT. (confidence high, judge supported)
  - pg_release_notes@16: "Role inheritance now controls the default inheritance status of member roles added during GRANT"
- **[required] behavior** `present` `"ALTER ROLE ... INHERIT|NOINHERIT"`: The application or administration tooling changes a role's inheritance status (e.g. ALTER ROLE ... INHERIT/NOINHERIT) and relies on that change affecting existing memberships. (confidence low, judge supported)
  - pg_release_notes@16: "changes to a role's inheritance status affected all previous and future member roles"
  - ⚠ The text does not name the exact SQL commands used to change a role's inheritance status; ALTER ROLE ... INHERIT/NOINHERIT is inferred.
- **[optional] database** `present` `"rolinherit = false"`: Roles with non-default inheritance status (NOINHERIT) exist and have members granted, so memberships depend on the role's inheritance status. (confidence low, judge partially_supported)
  - pg_release_notes@16: "Previously the inheritance status of member roles was controlled only by the role's inheritance status"
  - ⚠ The text does not describe how existing memberships are assigned an inheritance status when migrated via pg_upgrade or dump/restore.

Actions:
- Review scripts and procedures that toggle role INHERIT/NOINHERIT expecting it to affect existing memberships.
- Use the new GRANT ... WITH INHERIT clause to set inheritance explicitly per membership at GRANT time.
- After upgrade, verify effective privileges of member roles.

### CREATE OR REPLACE VIEW can no longer change output column collation

`postgresql_24f3172f15` · medium · confidence medium · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, CREATE OR REPLACE VIEW is prevented from changing the collation of an output column. Migration scripts or application code that relied on replacing a view with a definition whose output column collation differs will fail. The text does not name a workaround or the exact error raised.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where CREATE OR REPLACE VIEW was prevented from changing output column collation. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent CREATE OR REPLACE VIEW from changing the collation of an output column"
- **[required] api_usage** `present` `"CREATE OR REPLACE VIEW"`: Application, migration or DDL scripts use CREATE OR REPLACE VIEW. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent CREATE OR REPLACE VIEW from changing the collation of an output column"
- **[required] behavior** `present` `"output column collation change"`: The replacement view definition changes the collation of an existing output column (e.g. via a COLLATE clause or a differently-collated source expression). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "changing the collation of an output column"
  - ⚠ The text does not state what error is raised or what alternative (e.g. DROP VIEW and CREATE VIEW) should be used.

Actions:
- Review CREATE OR REPLACE VIEW statements in migrations and DDL scripts for definitions that would change an output column's collation.
- Test view-replacement migrations against PostgreSQL 16 before upgrading.

### to_tsquery/websearch_to_tsquery output changes for discarded tokens

`postgresql_27194e765d` · medium · confidence medium · introduced in 14 · fires at upgrade

In PostgreSQL 14, to_tsquery() and websearch_to_tsquery() parse query text containing discarded tokens (e.g. underscore) differently, producing different tsquery output (e.g. 'pg' <-> 'class' <-> 'pg' instead of ( 'pg' & 'class' ) <-> 'pg'). Full-text search results and any stored/compared tsquery values may change.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Upgrade crosses release 14, where to_tsquery() and websearch_to_tsquery() parsing of discarded tokens was fixed (confidence high, judge supported)
  - pg_release_notes@14: "Fix to_tsquery() and websearch_to_tsquery() to properly parse query text containing discarded tokens"
- **[required] api_usage** `present` `"to_tsquery"`: Application calls to_tsquery() or websearch_to_tsquery() (confidence high, judge supported)
  - pg_release_notes@14: "both websearch_to_tsquery('"pg_class pg"') and to_tsquery('pg_class <-> pg') used to output ( 'pg' & 'class' ) <-> 'pg'"
- **[required] behavior** `contains` `"_"`: Query text passed to these functions contains discarded tokens such as underscore (confidence medium, judge supported)
  - pg_release_notes@14: "Certain discarded tokens, like underscore, caused the output of these functions to produce incorrect tsquery output"
  - ⚠ The text names underscore as an example but does not list all discarded tokens.

Actions:
- Review full-text search queries passing text with underscores or other discarded tokens to to_tsquery()/websearch_to_tsquery() and verify results on 16.
- Re-check any stored tsquery values or tests asserting exact tsquery output.

### psql --single-transaction no longer rolls back on error unless ON_ERROR_STOP is set

`postgresql_2a4f5f5ead` · medium · confidence high · introduced in 15 · fires at first_use

In PostgreSQL 15, when psql runs in --single-transaction mode and an error is detected, the final COMMIT is changed to ROLLBACK only if ON_ERROR_STOP is set. Scripts relying on rollback after errors in --single-transaction mode without ON_ERROR_STOP may behave differently.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where this psql behavior change was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "change the final COMMIT command to ROLLBACK only if ON_ERROR_STOP is set"
- **[required] deployment** `present` `"--single-transaction"`: Scripts or tooling invoke psql with --single-transaction mode. (confidence high, judge supported)
  - pg_release_notes@15: "After an error is detected in psql's --single-transaction mode"
- **[disqualifying] configuration** `present` `"ON_ERROR_STOP"`: ON_ERROR_STOP is set for those psql invocations; if it is set, the final COMMIT is still changed to ROLLBACK after an error. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "change the final COMMIT command to ROLLBACK only if ON_ERROR_STOP is set"
  - ⚠ The text does not state what happened in prior releases regardless of ON_ERROR_STOP, nor what exactly happens now when ON_ERROR_STOP is not set.

Actions:
- Review psql invocations using --single-transaction (or -1) and set ON_ERROR_STOP (e.g. -v ON_ERROR_STOP=1) if scripts rely on the transaction being rolled back after an error.
- Test deployment/migration scripts that use psql --single-transaction against PostgreSQL 16 with deliberately failing statements.

### postmaster symlink removed

`postgresql_2a6232c2c0` · medium · confidence medium · introduced in 16 · fires at upgrade

PostgreSQL 16 no longer installs the symbolic link 'postmaster' to the server binary. Scripts, service units or tooling that invoke 'postmaster' to start the server will fail after upgrading to 16.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where the postmaster symbolic links were removed (confidence high, judge supported)
  - pg_release_notes@16: "Remove symbolic links for the postmaster binary"
- **[required] deployment** `present` `"postmaster"`: Deployment scripts, service definitions or tooling invoke the server via the 'postmaster' binary name (confidence medium, judge supported)
  - pg_release_notes@16: "Remove symbolic links for the postmaster binary"
  - ⚠ The text does not name the replacement binary; using 'postgres' is inferred, not stated.

Actions:
- Search startup scripts, systemd units, container entrypoints and monitoring checks for invocations of 'postmaster'.
- Update any 'postmaster' invocations to call the 'postgres' server binary instead (inferred replacement; the release notes do not name one).

### Custom scan providers assumed not to support projections

`postgresql_32c6a96fa1` · medium · confidence medium · introduced in 15 · fires at upgrade

Starting in PostgreSQL 15, custom scan providers are assumed by default to not support projections. Extensions implementing custom scan providers that do support projections must be updated to indicate so.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "The default is now that custom scan providers are assumed to not support projections"
- **[required] dependency** `present` `"custom scan provider"`: The deployment uses an extension or C code that implements a custom scan provider. (confidence medium, judge supported)
  - pg_release_notes@15: "custom scan providers are assumed to not support projections"
  - ⚠ The text does not name the specific API flag or struct field used to indicate projection support.
- **[required] behavior** `present` `"projection support in custom scan provider"`: The custom scan provider supports projections and relied on the previous default. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "those that do will need to be updated for this release"
  - ⚠ The text does not state the consequence if a projection-capable provider is not updated.

Actions:
- Identify extensions implementing custom scan providers and obtain versions updated for PostgreSQL 15+.
- For in-house custom scan providers that support projections, update the code to indicate projection support per the PostgreSQL 15 API.

### xml2 xml_is_well_formed() removed

`postgresql_4345c09353` · medium · confidence medium · introduced in 15 · fires at upgrade

The xml2 extension's xml_is_well_formed() function is removed in PostgreSQL 15. The core backend has provided an implementation since 9.1, so calls that resolve to the xml2 version will need to use the core function instead.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where xml2's xml_is_well_formed() was removed (confidence high, judge supported)
  - pg_release_notes@15: "Remove xml2's xml_is_well_formed() function"
- **[required] database** `present` `"xml_is_well_formed"`: The database has the xml2 extension installed and uses its xml_is_well_formed() function (confidence medium, judge supported)
  - pg_release_notes@15: "Remove xml2's xml_is_well_formed() function (Tom Lane)"
  - ⚠ The text does not say whether schema-qualified references to the xml2 function or dependent objects will fail during pg_upgrade or dump/restore, or whether unqualified calls simply resolve to the core function.

Actions:
- Use the core backend xml_is_well_formed() function, which has been available since PostgreSQL 9.1, instead of the xml2 version.
- Remove any schema qualification that points at the xml2 extension's copy of xml_is_well_formed().

### Regex \D and \W now match newlines in newline-sensitive mode

`postgresql_4645b4b0d2` · medium · confidence medium · introduced in 14 · fires at upgrade

Starting in PostgreSQL 14, the regex shorthands \D and \W match newlines when the regular expression is in newline-sensitive mode. Previously they did not. Queries that rely on the old behavior may return different matches. Use [^[:digit:]] or [^[:word:]] to get the old behavior.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where \D and \W began matching newlines in newline-sensitive mode (confidence high, judge supported)
  - pg_release_notes@14: "Allow \D and \W shorthands to match newlines in regular expression newline-sensitive mode"
- **[required] api_usage** `present` `"\\D or \\W in newline-sensitive regex"`: The application uses \D or \W in regular expressions evaluated in newline-sensitive mode (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Previously they did not match newlines in this mode"
  - ⚠ The text does not say how newline-sensitive mode is enabled, e.g. via flags or embedded options.
- **[required] behavior** `contains` `"newline characters in matched text"`: Input strings contain newlines, so matching results differ (confidence medium, judge supported)
  - pg_release_notes@14: "Allow \D and \W shorthands to match newlines"

Actions:
- Replace \D with [^[:digit:]] and \W with [^[:word:]] in newline-sensitive regexes where newlines must not match.
- Test regex-based queries against multi-line input after the upgrade.

### REINDEX DATABASE / reindexdb no longer reindex system catalog indexes

`postgresql_55fa40f078` · medium · confidence medium · introduced in 16 · fires at first_use

In PostgreSQL 16, REINDEX DATABASE and reindexdb no longer process indexes on system catalogs. Maintenance scripts that rely on them to reindex system catalogs will silently skip those indexes. Use REINDEX SYSTEM or reindexdb --system instead.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: Upgrade crosses PostgreSQL release 16, where the REINDEX DATABASE/reindexdb behavior changed (confidence high, judge supported)
  - pg_release_notes@16: "Change REINDEX DATABASE and reindexdb to not process indexes on system catalogs"
- **[required] api_usage** `present` `"REINDEX DATABASE"`: Maintenance scripts or jobs use REINDEX DATABASE or the reindexdb utility (without --system) (confidence medium, judge partially_supported)
  - pg_release_notes@16: "Change REINDEX DATABASE and reindexdb to not process indexes on system catalogs"
- **[uncertain] behavior** `present` `"system catalog reindexing via REINDEX DATABASE/reindexdb"`: The deployment relies on these commands to reindex system catalog indexes (confidence low, judge partially_supported)
  - pg_release_notes@16: "Processing such indexes is still possible using REINDEX SYSTEM and reindexdb --system."
  - ⚠ Whether a given deployment depends on system catalog reindexing via REINDEX DATABASE cannot be determined from the text.

Actions:
- Audit maintenance scripts and cron jobs for REINDEX DATABASE and reindexdb usage.
- Where system catalog indexes must be reindexed, add REINDEX SYSTEM or reindexdb --system.

### Custom server parameter names restricted to unquoted SQL identifier characters

`postgresql_5b9c633eb1` · medium · confidence medium · introduced in 14 · fires at upgrade

Starting in PostgreSQL 14, custom (extension/placeholder) server parameter names must use only characters valid in unquoted SQL identifiers. Configurations or applications that set custom parameters with other characters (e.g. hyphens) will no longer be accepted.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where custom parameter name restrictions were introduced (confidence high, judge supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters that are valid in unquoted SQL identifiers"
- **[required] configuration** `present` `"custom parameter name with characters outside unquoted SQL identifier set"`: The deployment or application defines custom server parameter names containing characters not valid in unquoted SQL identifiers (confidence medium, judge supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters that are valid in unquoted SQL identifiers"
  - ⚠ The text does not state whether invalid names produce an error at server start, a warning, or are ignored.

Actions:
- Audit postgresql.conf, ALTER SYSTEM/ALTER DATABASE/ALTER ROLE settings, and application SET/set_config calls for custom parameter names (e.g. myapp.some-setting) containing characters not valid in unquoted SQL identifiers.
- Rename such custom parameters to use only letters, digits, underscores (and dot-separated prefixes) before upgrading, and update all code that reads them via current_setting().

### Login role can no longer manage members of its own role without ADMIN OPTION

`postgresql_5e13cfd71d` · medium · confidence high · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, a login role no longer implicitly has ADMIN OPTION on its own role membership. Applications or scripts in which a login role GRANTs or REVOKEs membership in its own role, without having ADMIN OPTION, will fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where the default ADMIN OPTION on a login role's own membership was removed (confidence high, judge supported)
  - pg_release_notes@15: "Remove the default ADMIN OPTION privilege a login role has on its own role membership"
- **[required] behavior** `present` `"GRANT/REVOKE of own role executed by that login role without ADMIN OPTION"`: A login role adds or removes members of its own role (GRANT/REVOKE of its own role to others) without holding ADMIN OPTION (confidence high, judge supported)
  - pg_release_notes@15: "Previously, a login role could add/remove members of its own role, even without ADMIN OPTION privilege."

Actions:
- Identify scripts or application code where a login role grants or revokes membership in its own role.
- Explicitly grant the needed role WITH ADMIN OPTION to the managing role, or perform membership management as a role holding ADMIN OPTION (or a superuser).

### CREATEROLE roles lose ability to modify other roles without ADMIN OPTION

`postgresql_5f2b8ce7c3` · medium · confidence high · introduced in 16 · fires at first_use

In PostgreSQL 16, roles with CREATEROLE can no longer change many aspects of arbitrary non-superuser roles. Such changes, including adding members, now require ADMIN OPTION on the target role, and changing CREATEDB, REPLICATION and BYPASSRLS requires the requesting role to hold those attributes itself. Role-management automation that relies on a non-superuser CREATEROLE role may fail.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, where CREATEROLE privileges are restricted (confidence high, judge supported)
  - pg_release_notes@16: "Restrict the privileges of CREATEROLE and its ability to modify other roles"
- **[required] database** `present` `"CREATEROLE"`: The deployment uses non-superuser roles with the CREATEROLE attribute to manage other roles (confidence high, judge supported)
  - pg_release_notes@16: "Previously roles with CREATEROLE privileges could change many aspects of any non-superuser role."
- **[required] behavior** `present` `"ALTER ROLE / GRANT role membership by CREATEROLE role lacking ADMIN OPTION"`: The CREATEROLE role alters other roles or adds members to roles without holding ADMIN OPTION on them (confidence high, judge supported)
  - pg_release_notes@16: "Such changes, including adding members, now require the role requesting the change to have ADMIN OPTION permission."
- **[optional] behavior** `present` `"CREATEDB|REPLICATION|BYPASSRLS"`: The CREATEROLE role sets CREATEDB, REPLICATION, or BYPASSRLS on other roles without having those attributes itself (confidence high, judge supported)
  - pg_release_notes@16: "they can now change the CREATEDB, REPLICATION, and BYPASSRLS properties only if they also have those permissions"

Actions:
- Inventory non-superuser roles with CREATEROLE and the role-management operations they perform.
- Grant ADMIN OPTION on the roles that the CREATEROLE role must modify or add members to.
- Give the managing role the CREATEDB, REPLICATION, or BYPASSRLS attributes if it must set them on other roles, or perform those changes as a superuser.
- Test role-provisioning scripts and automation against PostgreSQL 16 before upgrading.

### Custom GUC options prefixed with an installed extension's name are deleted/rejected

`postgresql_5fd71eabce` · medium · confidence medium · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, custom options whose names match an installed extension's name but are not one of the extension's declared variables are deleted when the extension loads, and cannot be created again later in the session. Applications or configs that store their own settings under an extension's prefix (e.g. via SET or set_config) will lose those values or get errors.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "Disallow setting custom options that match the name of an installed extension"
- **[required] configuration** `present` `"custom option named <extension_name>.<undeclared_variable>"`: The application or configuration sets custom options whose prefix matches the name of an installed extension, but which are not variables declared by that extension. (confidence medium, judge supported)
  - pg_release_notes@15: "Disallow setting custom options that match the name of an installed extension, but are not one of the extension's declared variables"
  - ⚠ The text does not list which extensions or variable names are affected; this depends on which extensions are installed and what variables they declare.
- **[optional] behavior** `present` `"custom option set before extension load"`: Such pre-existing variables were set before the extension is loaded in the session (they will be deleted at extension load). (confidence high, judge supported)
  - pg_release_notes@15: "This change causes any such pre-existing variables to be deleted during extension load"

Actions:
- Inventory custom options that use an installed extension's name as their prefix and are not declared by that extension.
- Rename such application-specific options to a prefix that does not match any installed extension name.
- Test code using SET/set_config/current_setting on extension-prefixed names against PostgreSQL 15+ before upgrading.

### Numeric literals with trailing non-numeric characters now rejected

`postgresql_6b7cd5683a` · medium · confidence medium · introduced in 15 · fires at upgrade

Starting in PostgreSQL 15, numeric literals immediately followed by non-numeric characters (e.g. 123abc) are no longer split into a number token and a separate identifier token. Queries that relied on the old tokenization (e.g. column aliases written directly after a number without whitespace) may fail.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where numeric literals with trailing non-numeric characters are prevented. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent numeric literals from having non-numeric trailing characters"
- **[required] api_usage** `present` `"numeric literal immediately followed by identifier characters"`: Application SQL contains numeric literals immediately followed by letters without separating whitespace (e.g. 123abc), relying on them being parsed as a number followed by a separate token. (confidence medium, judge supported)
  - pg_release_notes@15: "Previously, query text like 123abc would be interpreted as 123 followed by a separate token abc."
  - ⚠ The text does not state whether the new behavior is a syntax error or another interpretation; it only says such literals are prevented.

Actions:
- Search application SQL, stored functions and views for numeric literals directly followed by letters (e.g. SELECT 123abc) and insert whitespace or use AS for aliases (e.g. SELECT 123 AS abc).
- Run the application's SQL test suite against PostgreSQL 15+ to detect queries that no longer parse.

### array_to_tsvector() errors on empty-string array elements

`postgresql_72e0855f91` · medium · confidence high · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, array_to_tsvector() raises an error when any array element is an empty string, because lexemes should never be empty. Application code that previously passed such arrays will now fail.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases"
- **[required] api_usage** `present` `"array_to_tsvector"`: The application calls array_to_tsvector() with arrays that may contain empty-string elements. (confidence high, judge supported)
  - pg_release_notes@15: "Generate an error if array_to_tsvector() is passed an empty-string array element"

Actions:
- Find all calls to array_to_tsvector() and filter out empty-string elements before calling it, e.g. with array_remove(arr, '').
- Add tests that pass arrays containing empty strings, to confirm the code no longer triggers the new error.

### random() output differs for same seed

`postgresql_755a05d0ae` · medium · confidence high · introduced in 15 · fires at upgrade

PostgreSQL 15 changed the algorithm behind random(), so results differ from prior versions even with the same seed. Applications or tests that depend on reproducible random sequences (e.g. via setseed()) will get different values after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses PostgreSQL release 15, where the random() algorithm changed (confidence high, judge supported)
  - pg_release_notes@15: "Improve the algorithm used to compute random()"
- **[required] api_usage** `present` `"random("`: Application or SQL code calls random() (confidence high, judge supported)
  - pg_release_notes@15: "This will cause random()'s results to differ from what was emitted by prior versions"
- **[optional] behavior** `present` `"setseed("`: Application relies on reproducible random() output for a given seed (e.g. via setseed()) (confidence low, judge supported)
  - pg_release_notes@15: "even for the same seed value"
  - ⚠ The text does not name setseed() explicitly. It only refers to the 'same seed value'.

Actions:
- Find code and tests that depend on deterministic random() output after setseed() and update expected values or remove the dependency on exact sequences.
- Regenerate any stored data or test fixtures produced from seeded random() if exact reproduction is required.

### force_parallel_mode renamed to debug_parallel_query

`postgresql_892ed5d374` · medium · confidence medium · introduced in 16 · fires at upgrade

The server variable force_parallel_mode is renamed to debug_parallel_query in PostgreSQL 16. Configuration files, SET commands, or tests referencing the old name will need to use the new name.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where force_parallel_mode was renamed (confidence high, judge supported)
  - pg_release_notes@16: "Rename server variable force_parallel_mode to debug_parallel_query (David Rowley)"
- **[required] configuration** `present` `"force_parallel_mode"`: The deployment or application references the server variable force_parallel_mode (postgresql.conf, ALTER SYSTEM, SET, connection options, tests) (confidence medium, judge supported)
  - pg_release_notes@16: "Rename server variable force_parallel_mode to debug_parallel_query"
  - ⚠ The text does not state whether the old name is kept as an alias or what happens when it is used.

Actions:
- Replace force_parallel_mode with debug_parallel_query in postgresql.conf, ALTER SYSTEM / ALTER DATABASE / ALTER ROLE settings, SET statements, connection strings and test configurations.
- Check per-role and per-database settings (pg_db_role_setting) for the old name before upgrading.

### Indexes on interval text output fail to create

`postgresql_9564474ceb` · medium · confidence medium · introduced in 15 · fires at upgrade

In PostgreSQL 15 the interval output function is marked stable instead of immutable because it depends on IntervalStyle. Creating indexes (e.g. expression indexes) that rely on the text output of interval values will fail.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: Upgrade crosses PostgreSQL release 15, where the interval output function became stable (confidence high, judge supported)
  - pg_release_notes@15: "Mark the interval output function as stable, not immutable, since it depends on IntervalStyle"
- **[required] database** `present` `"index expression using interval::text"`: The database has or creates indexes relying on the text output of interval values (e.g. expression indexes casting interval to text) (confidence medium, judge partially_supported)
  - pg_release_notes@15: "cause creation of indexes relying on the text output of interval values to fail"
  - ⚠ Text says index creation fails 'for example'; other contexts requiring immutable functions (e.g. generated columns) may also be affected but are not named.
  - ⚠ Text does not state whether existing such indexes carried over by pg_upgrade or dump/restore fail; dump/restore recreates indexes and would likely fail.

Actions:
- Identify indexes whose expressions depend on the text output of interval values and redesign them (e.g. index the interval value directly) before upgrading.
- Test dump/restore or index creation scripts against PostgreSQL 16 to detect failing index definitions.

### Mismatched GENERATED status between parent/partitioned and child/partition columns rejected

`postgresql_9d3f729496` · medium · confidence medium · introduced in 16 · fires at upgrade

In PostgreSQL 16, columns of parent/partitioned tables and their child/partition tables must all have the same generation status (all generated or all not generated). Schemas where a parent column is GENERATED but the child column is not (or vice versa) are no longer allowed; the generation expressions themselves may now differ.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, which tightens GENERATED restrictions on inherited and partitioned tables. (confidence high, judge supported)
  - pg_release_notes@16: "Tighten GENERATED expression restrictions on inherited and partitioned tables"
- **[required] database** `present` `"GENERATED"`: The database uses inherited or partitioned tables with GENERATED columns. (confidence high, judge supported)
  - pg_release_notes@16: "Columns of parent/partitioned and child/partition tables must all have the same generation status"
- **[required] database** `not_equals` `"same generation status between parent and child column"`: A parent column and corresponding child/partition column differ in generation status (one generated, the other not). (confidence medium, judge supported)
  - pg_release_notes@16: "must all have the same generation status, though now the actual generation expressions can be different"
  - ⚠ The text does not state whether existing mismatched schemas cause pg_upgrade or dump/restore to fail, or only new DDL is rejected.

Actions:
- Before upgrading, query pg_inherits/pg_attribute to find parent/child column pairs whose attgenerated differ and align them so both are generated or both are not.
- Review DDL migrations and scripts that create partitions or inheritance children (PARTITION OF, INHERITS, ATTACH PARTITION) to ensure generated column status matches the parent.
- Test a dump/restore or pg_upgrade --check of the schema on PostgreSQL 16 before production upgrade.

### PL/pgSQL bound cursor variable name no longer assigned at cursor assignment

`postgresql_b9ad526348` · medium · confidence medium · introduced in 16 · fires at first_use

In PostgreSQL 16, the string value (portal name) of PL/pgSQL bound cursor variables is assigned during OPEN rather than set to the variable name during cursor assignment, and will not match the variable name. Code that relies on the portal name equaling the cursor variable name (e.g., returning the refcursor and FETCHing by the variable name) may break.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, where bound cursor variable assignment rules changed. (confidence high, judge supported)
  - pg_release_notes@16: "Change assignment rules for PL/pgSQL bound cursor variables (Tom Lane)"
- **[required] api_usage** `present` `"CURSOR FOR"`: The application has PL/pgSQL functions/procedures that declare bound cursor variables. (confidence high, judge supported)
  - pg_release_notes@16: "Change assignment rules for PL/pgSQL bound cursor variables"
- **[required] behavior** `present` `"reliance on portal name equal to cursor variable name"`: The code relies on the cursor variable's string value (portal name) matching the variable name, e.g. returning the cursor and fetching from it by the variable name. (confidence medium, judge partially_supported)
  - pg_release_notes@16: "now it will be assigned during OPEN, and will not match the variable name"
- **[disqualifying] api_usage** `present` `"assignment of portal name to cursor variable before OPEN"`: If the code already assigns an explicit portal name to the cursor variable before OPEN, the risk does not apply. (confidence high, judge supported)
  - pg_release_notes@16: "assign the desired portal name to the cursor variable before OPEN"

Actions:
- Search PL/pgSQL code for bound cursor variables whose portal name is used by callers (e.g. returned refcursors fetched by name).
- Assign the desired portal name to the cursor variable before OPEN to restore the previous behavior (e.g. curs := 'curs'; OPEN curs;).
- Test functions returning refcursors after upgrade to confirm callers fetch from the correct portal name.

### hash_mem_multiplier default raised to 2.0

`postgresql_c49690050a` · medium · confidence low · introduced in 15 · fires at upgrade

In PostgreSQL 15 the default of hash_mem_multiplier increased to 2.0, allowing query hash operations to use more work_mem memory than other operations. Deployments relying on the previous default may see increased memory use by hash operations.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the hash_mem_multiplier default was increased to 2.0. (confidence high, judge supported)
  - pg_release_notes@15: "Increase hash_mem_multiplier default to 2.0 (Peter Geoghegan)"
- **[required] configuration** `absent` `"hash_mem_multiplier"`: The deployment does not explicitly set hash_mem_multiplier, so it relies on the default value. (confidence low, judge supported)
  - pg_release_notes@15: "Increase hash_mem_multiplier default to 2.0"
  - ⚠ The text does not state the previous default value.
- **[optional] behavior** `present` `"hash operations"`: Workloads run queries with hash operations, which may now use more memory relative to work_mem. (confidence medium, judge supported)
  - pg_release_notes@15: "This allows query hash operations to use more work_mem memory than other operations."
  - ⚠ The text does not quantify the impact on memory consumption or performance.

Actions:
- Review memory sizing for hash operations given the new hash_mem_multiplier default of 2.0 combined with work_mem.
- If the previous behavior is needed, set hash_mem_multiplier explicitly in postgresql.conf.

### Removed server parameter vacuum_cleanup_index_scale_factor

`postgresql_c57abe8742` · medium · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 removes the server parameter vacuum_cleanup_index_scale_factor. It had already been ignored since 13.3, so there is no behavior to lose. However, any configuration that still sets it references a parameter that no longer exists in 14 and later.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the parameter was removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove server parameter vacuum_cleanup_index_scale_factor (Peter Geoghegan)"
- **[required] configuration** `present` `"vacuum_cleanup_index_scale_factor"`: The deployment sets vacuum_cleanup_index_scale_factor in server configuration (postgresql.conf, ALTER SYSTEM, ALTER DATABASE/ROLE SET, or startup options). (confidence medium, judge supported)
  - pg_release_notes@14: "Remove server parameter vacuum_cleanup_index_scale_factor"
  - ⚠ The text does not state what happens when a removed parameter is still set, for example whether startup or SET statements fail.

Actions:
- Remove vacuum_cleanup_index_scale_factor from postgresql.conf, postgresql.auto.conf (ALTER SYSTEM RESET), per-database and per-role settings, and any client or startup options before upgrading.
- No replacement is needed: the setting was already ignored starting in 13.3.

### Removed read-only server variables lc_collate and lc_ctype

`postgresql_cc8d8091c1` · medium · confidence medium · introduced in 16 · fires at upgrade

PostgreSQL 16 removes the read-only server variables lc_collate and lc_ctype. Code or monitoring queries that read them (e.g. via SHOW, current_setting(), or pg_settings) will no longer find them after upgrading from 13.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, where lc_collate and lc_ctype server variables are removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove read-only server variables lc_collate and lc_ctype (Peter Eisentraut)"
- **[required] api_usage** `present` `"lc_collate|lc_ctype"`: Application code, scripts, or monitoring read the server variable lc_collate or lc_ctype (e.g. SHOW lc_collate, current_setting('lc_ctype'), pg_settings lookups). (confidence medium, judge supported)
  - pg_release_notes@16: "Remove read-only server variables lc_collate and lc_ctype"
  - ⚠ The text does not name a replacement; per-database collation and ctype information (e.g. pg_database.datcollate/datctype) is not mentioned in the text.

Actions:
- Search application code, scripts, and monitoring queries for references to lc_collate and lc_ctype server variables and remove or rewrite them before upgrading.
- Since collations and locales can vary between databases, obtain locale information per database rather than from server variables.

### PUBLIC CREATE privilege removed from public schema in new clusters/databases

`postgresql_fcfbbf6b55` · medium · confidence low · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, new database clusters and newly-created databases no longer grant CREATE on the public schema to PUBLIC. Roles that are not the database owner and relied on the old default to create objects in the public schema may get permission errors in freshly initialized clusters or newly created databases. Clusters upgraded with pg_upgrade and databases restored from a dump keep their existing public schema permissions.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL 15, where PUBLIC creation permission on the public schema was removed by default (confidence high, judge supported)
  - pg_release_notes@15: "Remove PUBLIC creation permission on the public schema"
- **[required] deployment** `present` `"new cluster or newly-created database"`: The deployment uses a newly initialized cluster or creates new databases on the 15+ server, for example with initdb or CREATE DATABASE, and provisions the schema without restoring a dump (confidence medium, judge partially_supported)
  - pg_release_notes@15: "The change applies to new database clusters and to newly-created databases in existing clusters."
- **[disqualifying] deployment** `present` `"pg_upgrade or dump restore"`: The database was carried over via pg_upgrade or restored from a dump, so the existing public schema permissions are preserved (confidence high, judge supported)
  - pg_release_notes@15: "Upgrading a cluster or restoring a database dump will preserve public's existing permissions."
- **[required] database** `absent` `"CREATE privilege on schema public for application role"`: Application roles other than the database owner create tables or other objects in the public schema and rely on PUBLIC having CREATE privilege (confidence low, judge partially_supported)
  - pg_release_notes@15: "For new databases having no need to defend against insider threats, granting CREATE permission will yield the behavior of prior releases."
  - ⚠ The text does not explicitly describe the resulting error for non-owner roles; the impact on such roles is inferred from the removed permission.

Actions:
- For new databases where the old behavior is needed and insider threats are not a concern, run GRANT CREATE ON SCHEMA public TO PUBLIC, or grant CREATE to specific application roles.
- Add explicit GRANT CREATE ON SCHEMA public statements for application roles to provisioning scripts and migrations for new databases.
- For existing databases, especially those with multiple users, consider REVOKE CREATE ON SCHEMA public FROM PUBLIC to adopt the new secure default.

### postgres_fdw no longer casts constants in remote queries

`postgresql_0650d53bd7` · low · confidence high · introduced in 15 · fires at upgrade

Starting in release 15, postgres_fdw avoids unnecessary casting of constants in the queries it sends to remote servers. The text says such casts could cause errors when column types are intentionally different between local and remote databases. Remote queries generated by postgres_fdw will therefore differ from those generated in release 13. The text does not describe any other impact.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where postgres_fdw stopped casting constants unnecessarily (confidence high, judge supported)
  - pg_release_notes@15: "Avoid unnecessary casting of constants in queries sent by postgres_fdw"
- **[required] database** `present` `"postgres_fdw"`: The deployment uses the postgres_fdw extension to query remote databases (confidence high, judge supported)
  - pg_release_notes@15: "Avoid unnecessary casting of constants in queries sent by postgres_fdw"
- **[optional] database** `present` `"local/remote column type mismatch on foreign tables"`: Foreign table column types intentionally differ from the remote table's column types (confidence medium, judge supported)
  - pg_release_notes@15: "When column types are intentionally different between local and remote databases, such casts could cause errors."
  - ⚠ The text says the old casts could cause errors in this scenario. It does not state whether removing them can change results or cause new errors for any existing queries.

Actions:
- Inventory postgres_fdw foreign tables whose local column types differ from the remote column types.
- Test queries against those foreign tables on version 16, including queries that compare columns with constants, and verify the results match expectations.

### Zero-length Unicode identifiers (U&"") rejected

`postgresql_076d7c8e08` · low · confidence high · introduced in 15 · fires at first_use

PostgreSQL 15 disallows zero-length Unicode identifiers such as U&"". SQL statements that use them will be rejected after upgrading from 13 to 16. Non-Unicode zero-length identifiers were already disallowed.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where zero-length Unicode identifiers became disallowed. (confidence high, judge supported)
  - pg_release_notes@15: "Disallow zero-length Unicode identifiers, e.g., U&"""
- **[required] api_usage** `present` `"U&\"\""`: The application's SQL (queries, scripts, migrations, functions) contains zero-length Unicode identifiers such as U&"". (confidence high, judge supported)
  - pg_release_notes@15: "Disallow zero-length Unicode identifiers, e.g., U&"""

Actions:
- Search application SQL, stored function bodies and migration scripts for U&"" and replace it with a non-empty identifier before upgrading.

### factorial() of negative numbers now errors

`postgresql_0e147761ab` · low · confidence medium · introduced in 14 · fires at first_use

Starting in PostgreSQL 14, factorial() raises an error for negative inputs; previously it returned 1. Code calling factorial() with negative arguments will fail at runtime.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where factorial() of negative numbers became disallowed. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow factorial() of negative numbers (Peter Eisentraut)"
- **[required] api_usage** `present` `"factorial("`: The application or database objects call factorial() with arguments that can be negative. (confidence medium, judge supported)
  - pg_release_notes@14: "Disallow factorial() of negative numbers"
  - pg_release_notes@14: "Previously such cases returned 1."
  - ⚠ The text does not state the exact error raised.

Actions:
- Find calls to factorial() and ensure the arguments are never negative, or guard them (e.g. with CASE) to keep the old result of 1 where the application relied on it.
- Add tests covering factorial() with negative or edge-case inputs before upgrading.

### intarray GiST indexes no longer used by <@ and @> containment operators

`postgresql_11b4c53a07` · low · confidence medium · introduced in 14 · fires at upgrade

In release 14, the intarray containment operators <@ and @> no longer use GiST indexes and scan the heap instead. GiST indexes created to support these operators become unused and should be removed.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where intarray containment operators stop using GiST indexes (confidence high, judge supported)
  - pg_release_notes@14: "Prevent the containment operators (<@ and @>) for intarray from using GiST indexes"
- **[required] database** `present` `"intarray"`: The database has the intarray extension installed and uses the <@ or @> containment operators on intarray columns (confidence high, judge supported)
  - pg_release_notes@14: "containment operators (<@ and @>) for intarray"
- **[required] database** `present` `"GiST index on intarray column"`: GiST indexes exist on intarray columns that were created to support containment queries (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Indexes created for this purpose should be removed."
  - ⚠ The text does not say whether these GiST indexes still help other operators, such as && for intarray, so it is unclear whether every such index can be dropped.

Actions:
- Identify GiST indexes on intarray columns that were created for <@ or @> queries.
- Drop those indexes after upgrading, unless they also support other operators.
- Re-check the query plans for intarray containment queries after the upgrade.

### has_column_privilege() with attribute numbers returns false instead of error

`postgresql_167726bd25` · low · confidence high · introduced in 14 · fires at first_use

Since PostgreSQL 14, has_column_privilege() called with an attribute number for a non-existent or dropped column returns false instead of raising an invalid-column error. Code relying on catching that error will no longer see it.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@14: "Return false for has_column_privilege() checks on non-existent or dropped columns when using attribute numbers"
- **[required] api_usage** `present` `"has_column_privilege"`: The application calls has_column_privilege() with attribute numbers (rather than column names). (confidence high, judge supported)
  - pg_release_notes@14: "checks on non-existent or dropped columns when using attribute numbers"
- **[required] behavior** `present` `"error handling for invalid column from has_column_privilege"`: The application relies on the invalid-column error being raised for non-existent or dropped columns. (confidence high, judge supported)
  - pg_release_notes@14: "Previously such attribute numbers returned an invalid-column error."

Actions:
- Review calls to has_column_privilege() using attribute numbers and treat a false result as possibly indicating a non-existent or dropped column instead of relying on an error.
- Update tests that expect an invalid-column error from has_column_privilege() with attribute numbers.

### EXPLAIN output reports temporary schema as pg_temp

`postgresql_1bae1f0746` · low · confidence high · introduced in 15 · fires at upgrade

Starting in PostgreSQL 15, when EXPLAIN output references the session's temporary object schema, it shows pg_temp instead of the actual schema name (e.g. pg_temp_N). Tools, tests or scripts that parse or compare EXPLAIN output containing actual temp schema names may see different output.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15 (13 -> 16), where EXPLAIN began referring to the temporary schema as pg_temp. (confidence high, judge supported)
  - pg_release_notes@15: "When EXPLAIN references the session's temporary object schema, refer to it as pg_temp"
- **[required] api_usage** `present` `"EXPLAIN"`: The application or tooling runs EXPLAIN on queries that reference temporary objects (the session's temporary schema). (confidence high, judge supported)
  - pg_release_notes@15: "When EXPLAIN references the session's temporary object schema"
- **[optional] test_coverage** `present` `"pg_temp_"`: Code or tests parse or compare EXPLAIN output and expect the actual temporary schema name (e.g. pg_temp_N). (confidence low, judge partially_supported)
  - pg_release_notes@15: "Previously the actual schema name was reported, leading to inconsistencies across sessions."
  - ⚠ The text does not state that any parsing tools or tests are affected; impact on consumers is inferred.

Actions:
- Update any tests, expected-output files, or tooling that parse EXPLAIN output to expect pg_temp instead of the actual temporary schema name (pg_temp_N).

### Window frame RANGE with infinite offsets returns different (corrected) results

`postgresql_28d15925c3` · low · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 fixed how infinite window function ranges are handled. Window frame clauses like 'inf' PRECEDING AND 'inf' FOLLOWING previously returned incorrect results. After upgrading from 13, queries using these frames return different (correct) results, so anything relying on the old output will see a change.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where infinite window function range handling was fixed. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"'inf' PRECEDING"`: The application uses window frame clauses with infinite offsets, such as 'inf' PRECEDING AND 'inf' FOLLOWING. (confidence medium, judge supported)
  - pg_release_notes@14: "Previously window frame clauses like 'inf' PRECEDING AND 'inf' FOLLOWING returned incorrect results."
  - ⚠ The text does not list every infinite-value spelling (e.g. 'infinity', '-inf') or every data type affected; it gives 'inf' only as an example.
- **[uncertain] behavior** `present` `"reliance on pre-14 infinite window frame results"`: The application or its tests depend on the previous (incorrect) results of such window queries. (confidence low, judge supported)
  - pg_release_notes@14: "Fix handling of infinite window function ranges"
  - ⚠ The text does not describe what the incorrect results were, so the scope of the output difference is unknown.

Actions:
- Find queries that use window frames with infinite offsets ('inf' PRECEDING/FOLLOWING).
- Run those queries on PostgreSQL 16 and compare results against 13. Update any downstream logic or test expectations that depended on the old results.

### ecpg doubled quote mark handling in SQL command strings

`postgresql_369e7506c5` · low · confidence high · introduced in 14 · fires at upgrade

Starting in release 14, ecpg correctly processes doubled quote marks in embedded SQL command strings. Previously 'abc''def' was passed to the server as 'abc'def' and "abc""def" as "abc"def", causing syntax errors. ecpg programs whose embedded SQL contains doubled quotes will send different text to the server after re-preprocessing with the newer ecpg. Any workaround written for the old behavior may now produce different results.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where ecpg's handling of doubled quote marks changed. (confidence high, judge supported)
  - pg_release_notes@14: "Process doubled quote marks in ecpg SQL command strings correctly"
- **[required] api_usage** `present` `"ecpg SQL command strings containing '' or \"\""`: The application uses ecpg embedded SQL whose command strings contain doubled quote marks ('' or ""). (confidence high, judge supported)
  - pg_release_notes@14: "Previously 'abc''def' was passed to the server as 'abc'def', and "abc""def" was passed as "abc"def", causing syntax errors."
- **[uncertain] behavior** `unknown` `"workaround for pre-14 ecpg quote handling"`: The application contains workarounds for the old incorrect quote handling that would behave differently now that doubled quotes are processed correctly. (confidence low, judge not_supported)
  - pg_release_notes@14: "causing syntax errors"
  - ⚠ The text does not state what impact, if any, the fix has on existing programs beyond fixing the syntax errors.
  - ⚠ Judge: evidence does not support this claim. The quote only says the old handling caused syntax errors. It says nothing about application workarounds for the old behavior, or that such workarounds would behave differently after the fix.

Actions:
- Re-preprocess ecpg (.pgc) sources with the new ecpg and review embedded SQL strings that contain doubled quote marks.
- Remove any workarounds written for the old quote handling and test the affected statements.

### Primary keys using NULLS NOT DISTINCT indexes are disallowed

`postgresql_3d872e0449` · low · confidence medium · introduced in 16 · fires at first_use

Release 16 disallows NULLS NOT DISTINCT indexes for primary keys. DDL or schema dumps that define a primary key with NULLS NOT DISTINCT would be rejected on 16.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, where NULLS NOT DISTINCT indexes for primary keys are disallowed. (confidence high, judge supported)
  - pg_release_notes@16: "Disallow NULLS NOT DISTINCT indexes for primary keys (Daniel Gustafsson)"
- **[required] database** `present` `"PRIMARY KEY ... NULLS NOT DISTINCT"`: The schema or application DDL defines a primary key using NULLS NOT DISTINCT. (confidence medium, judge supported)
  - pg_release_notes@16: "Disallow NULLS NOT DISTINCT indexes for primary keys"
  - ⚠ The text does not state in which release NULLS NOT DISTINCT was introduced, so it is unclear whether a 13 source cluster could already contain such primary keys.
  - ⚠ The text does not state whether the failure occurs during pg_upgrade/dump restore or only when new DDL is executed.

Actions:
- Search schema migrations and DDL for primary keys declared with NULLS NOT DISTINCT and remove that clause from primary key definitions before running them on 16.
- Test schema creation/restore against a PostgreSQL 16 instance.

### pg_statio_all_tables TOAST multi-index row aggregation change

`postgresql_3f790f697e` · low · confidence medium · introduced in 15 · fires at upgrade

In release 15, pg_statio_all_tables sums values for TOAST tables with multiple indexes instead of showing one row per index. Monitoring or reporting queries against this view may see fewer rows and aggregated TOAST index values. The text calls this a rare case.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where pg_statio_all_tables output changed (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"pg_statio_all_tables"`: The application or monitoring tooling queries pg_statio_all_tables (confidence high, judge supported)
  - pg_release_notes@15: "Fix pg_statio_all_tables to sum values for the rare case of TOAST tables with multiple indexes"
- **[required] database** `present` `"TOAST table with more than one index"`: The database has TOAST tables with multiple indexes, which previously produced one row per index (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Previously such cases would show one row for each index."
  - ⚠ The text does not say how such TOAST tables arise or how to detect them.

Actions:
- Review monitoring or reporting queries on pg_statio_all_tables that assume one row per TOAST index, and adjust them to expect summed values.

### Fractional interval input above months now rounds to nearest month

`postgresql_40755c4ec6` · low · confidence medium · introduced in 15 · fires at upgrade

Starting in PostgreSQL 15, interval input with a fractional value for a unit greater than months (e.g. years) is rounded to the nearest month, so '1.99 years' becomes 2 years instead of 1 year 11 months. Applications that store or compute with such interval literals may get different values.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where interval input rounding changed. (confidence high, judge supported)
  - pg_release_notes@15: "round to the nearest month (Bruce Momjian) For example, convert 1.99 years to 2 years, not 1 year 11 months as before."
  - pg_release_notes@15: "Improve consistency of interval parsing with trailing periods"
- **[required] behavior** `present` `"fractional interval input for units greater than months"`: The application or stored data supplies interval input with a fractional value for a unit greater than months (e.g. fractional years, decades, centuries, millennia). (confidence medium, judge supported)
  - pg_release_notes@15: "When interval input provides a fractional value for a unit greater than months, round to the nearest month"
  - pg_release_notes@15: "Numbers with trailing periods were rejected on some platforms."
  - ⚠ The text does not list which units count as greater than months beyond the years example.
  - ⚠ The text does not state whether such inputs are now consistently accepted or consistently rejected, nor which platforms previously rejected them.

Actions:
- Search application code, SQL, and stored procedures for interval literals with fractional year (or larger) units and verify the rounded results are acceptable.
- Where exact month precision is required, express intervals in integer years and months (e.g. '1 year 11 months') instead of fractional years.
- Add tests covering interval parsing of fractional year values after upgrading.
- Search application code and stored data for interval strings with numbers ending in a period and test them against PostgreSQL 16 to confirm parsing behavior.
- Normalize interval inputs to avoid trailing periods on numbers (e.g. '1 day' or '1.0 day').

### Regex back-reference matching ignores constraints

`postgresql_5e668838bc` · low · confidence medium · introduced in 14 · fires at upgrade

Starting in PostgreSQL 14, constraints (such as ^) are disregarded when matching regular expression back-references. Patterns like (^\d+).*\1 may match differently than in 13, changing query results.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14 (13 -> 16), where this behavior change was introduced. (confidence high, judge supported)
  - pg_release_notes@14: "Disregard constraints when matching regular expression back-references"
- **[required] api_usage** `present` `"regex back-reference to a group containing a constraint, e.g. (^\\d+).*\\1"`: The application uses regular expressions containing back-references (e.g. \1) inside a capture group that also contains a constraint such as ^. (confidence medium, judge supported)
  - pg_release_notes@14: "in (^\d+).*\1, the ^ constraint should be applied at the start of the string, but not when matching \1."
  - ⚠ The text gives only ^ as an example; which other constraints (e.g. $, \y, lookahead) are affected is not enumerated.

Actions:
- Search application code, functions, views, and check constraints for regular expressions using back-references (\1-\9) where the referenced group contains constraints like ^.
- Test such patterns against PostgreSQL 14+ to confirm match results are still as intended, and adjust the patterns if needed.

### JSON numeric literal trailing junk now rejected

`postgresql_614772dae3` · low · confidence medium · introduced in 15 · fires at first_use

In PostgreSQL 15, JSON numeric literal processing follows the SQL/JSON standard. Formats like .1 and 1. are now accepted, and trailing junk after numeric literals (e.g. 1.type()) is now disallowed. Applications that rely on the old parsing may see errors or different results.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where JSON numeric literal processing was changed (confidence high, judge supported)
  - pg_release_notes@15: "Adjust JSON numeric literal processing to match the SQL/JSON-standard"
- **[required] api_usage** `present` `"numeric literal followed by trailing junk (e.g. 1.type())"`: The application uses JSON numeric literals with trailing junk directly after the number, such as 1.type() (confidence medium, judge supported)
  - pg_release_notes@15: "disallows trailing junk after numeric literals, like 1.type()"
  - ⚠ The text does not say which functions or contexts (e.g. jsonpath expressions vs. JSON input) are affected.
- **[optional] behavior** `present` `"reliance on rejection of .1 or 1. numeric formats"`: The application depends on numeric formats like .1 or 1. being rejected (confidence high, judge supported)
  - pg_release_notes@15: "This accepts numeric formats like .1 and 1."

Actions:
- Review JSON/jsonpath expressions for numeric literals directly followed by other tokens (e.g. 1.type()) and rewrite them, e.g. by separating or parenthesizing the number.
- Test JSON-processing queries against PostgreSQL 15+ before upgrading.

### Composite row types for sequences and toast tables removed

`postgresql_62589404a7` · low · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 no longer creates composite types for sequences and toast tables. Code or objects that reference the row type of a sequence or toast table will no longer find it after upgrading from 13.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where composite types for sequences and toast tables were removed (confidence high, judge supported)
  - pg_release_notes@14: "Remove the composite types that were formerly created for sequences and toast tables"
- **[required] database** `present` `"reference to sequence/toast table composite type"`: The application or database objects reference the composite type of a sequence or toast table (confidence medium, judge supported)
  - pg_release_notes@14: "composite types that were formerly created for sequences and toast tables"
  - ⚠ The text does not describe how such types might be referenced (e.g. casts, function signatures, pg_type lookups) or what failure results.

Actions:
- Before upgrading, find objects or queries that depend on the row type of a sequence or toast table.
- Remove those dependencies or rewrite them so they do not need these types.

### Interval justification functions now detect integer overflow

`postgresql_6642146d25` · low · confidence high · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, integer overflow is detected in justify_interval(), justify_hours(), and justify_days(). Calls with inputs that overflow may behave differently than in 13, likely failing instead of returning a result, though the text does not say exactly what happens.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where overflow detection was added to the interval justification functions. (confidence high, judge supported)
  - pg_release_notes@15: "Detect integer overflow in interval justification functions"
- **[required] api_usage** `present` `"justify_interval|justify_hours|justify_days"`: The application or database objects call justify_interval(), justify_hours(), or justify_days(). (confidence high, judge supported)
  - pg_release_notes@15: "The affected functions are justify_interval(), justify_hours(), and justify_days()."
- **[uncertain] behavior** `unknown` `"interval inputs causing integer overflow"`: The function is called with interval values large enough to overflow during justification, and the new handling is likely an error rather than a silently wrong result. (confidence low, judge partially_supported)
  - pg_release_notes@15: "Detect integer overflow in interval justification functions"
  - ⚠ The text does not say what happens when overflow is detected (for example, raising an error), nor what the previous behavior was.
  - ⚠ The text does not say which input magnitudes trigger overflow.

Actions:
- Find calls to justify_interval(), justify_hours(), and justify_days() in application code, views, and functions.
- Test these calls against PostgreSQL 16 with extreme interval values to confirm how overflow is handled.
- Add error handling or input validation where very large intervals may be passed.

### "char" type output of non-ASCII bytes changed to octal escapes

`postgresql_72cf803a6f` · low · confidence medium · introduced in 15 · fires at upgrade

In PostgreSQL 15 the I/O format of the single-byte type "char" changed: bytes with the high bit set are now output as a backslash followed by three octal digits. Applications that read or compare text output of "char" columns containing non-ASCII bytes may see different values.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@15: "Change the I/O format of type "char" for non-ASCII characters"
- **[required] database** `present` `"\"char\""`: The database uses columns or values of type "char" (the single-byte internal type). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Change the I/O format of type "char" for non-ASCII characters"
- **[required] behavior** `present` `"non-ASCII bytes in \"char\" values"`: Stored "char" values contain bytes with the high bit set (non-ASCII). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Bytes with the high bit set are now output as a backslash and three octal digits"
  - ⚠ The text does not state how input of the octal escape form or of previously-dumped raw bytes is handled.

Actions:
- Identify "char" columns and check for values with the high bit set.
- Update application code that parses or compares "char" text output to handle the backslash-plus-three-octal-digit format.

### tablefunc normal_rand() rejects negative values

`postgresql_85602454ed` · low · confidence medium · introduced in 14 · fires at first_use

Starting in PostgreSQL 14, tablefunc's normal_rand() no longer accepts negative values. Calls that pass negative values, which previously produced undesirable results, will now be rejected.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where normal_rand() stopped accepting negative values (confidence high, judge supported)
  - pg_release_notes@14: "Prevent tablefunc's function normal_rand() from accepting negative values"
- **[required] api_usage** `present` `"normal_rand"`: The tablefunc extension is installed and normal_rand() is called (confidence high, judge supported)
  - pg_release_notes@14: "Prevent tablefunc's function normal_rand() from accepting negative values"
- **[required] behavior** `present` `"negative argument to normal_rand"`: normal_rand() is called with negative argument values (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Negative values produced undesirable results."
  - ⚠ The text does not specify which parameter(s) are affected or whether an error is raised versus another handling of the value.

Actions:
- Find calls to normal_rand() and make sure no negative values are passed.
- Test code paths that compute normal_rand() arguments dynamically, so negative inputs are caught before the upgrade.

### websearch_to_tsquery adjacent discarded tokens in quotes now produce different tsquery

`postgresql_9623a24b4c` · low · confidence medium · introduced in 14 · fires at upgrade

In PostgreSQL 14, websearch_to_tsquery() parses quoted text containing multiple adjacent discarded tokens differently: e.g. websearch_to_tsquery('"aaa: bbb"') previously output 'aaa' <2> 'bbb' and now outputs 'aaa' <-> 'bbb'. Full-text search results or stored/compared tsquery outputs may differ after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where websearch_to_tsquery() parsing of adjacent discarded tokens in quotes was fixed. (confidence high, judge supported)
  - pg_release_notes@14: "Fix websearch_to_tsquery() to properly parse multiple adjacent discarded tokens in quotes"
- **[required] api_usage** `present` `"websearch_to_tsquery"`: The application calls websearch_to_tsquery(). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Previously, quoted text that contained multiple adjacent discarded tokens was treated as multiple tokens, causing incorrect tsquery output"
- **[required] behavior** `present` `"quoted text with multiple adjacent discarded tokens"`: Search input passed to websearch_to_tsquery() contains quoted phrases with multiple adjacent discarded tokens (e.g. punctuation such as ': '). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "websearch_to_tsquery('"aaa: bbb"') used to output 'aaa' <2> 'bbb', but now outputs 'aaa' <-> 'bbb'"

Actions:
- Find all uses of websearch_to_tsquery() and review whether user search input can contain quoted phrases with adjacent discarded tokens (e.g. punctuation).
- Update tests or stored expected tsquery outputs that relied on the old output (e.g. 'aaa' <2> 'bbb') to the new output ('aaa' <-> 'bbb').
- Re-validate full-text phrase-search results after upgrading.

### Clients relying on version 2 wire protocol can no longer connect

`postgresql_99cd4201b9` · low · confidence medium · introduced in 14 · fires at upgrade

PostgreSQL 14 removes server and libpq support for the version 2 frontend/backend wire protocol. Clients or drivers that still speak only protocol v2 cannot connect to a 14+ server, and libpq 14+ cannot connect to servers that only support v2. Protocol v2 was last the default in PostgreSQL 7.3 (2002).

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14, where v2 wire protocol support was removed (confidence high, judge supported)
  - pg_release_notes@14: "Remove server and libpq support for the version 2 wire protocol"
- **[required] dependency** `present` `"version 2 wire protocol"`: A client, driver or tool connecting to the server uses (or forces) the version 2 wire protocol, or a libpq-based client must talk to a server supporting only protocol v2 (confidence medium, judge supported)
  - pg_release_notes@14: "Remove server and libpq support for the version 2 wire protocol"
  - ⚠ The text does not name specific drivers or connection settings that select protocol v2.

Actions:
- Verify all client drivers and tools use the version 3 wire protocol before upgrading.
- Upgrade any legacy drivers that only support protocol v2.

### chr() with negative argument now errors

`postgresql_9a56057ff7` · low · confidence medium · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, calling chr() with a negative argument generates an error. Queries or functions that pass negative values to chr() will fail after upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where chr() begins erroring on negative arguments (confidence high, judge supported)
  - pg_release_notes@15: "Generate an error when chr() is supplied with a negative argument"
- **[required] api_usage** `present` `"chr("`: The application or database code calls chr() with an argument that can be negative (confidence medium, judge supported)
  - pg_release_notes@15: "Generate an error when chr() is supplied with a negative argument"
  - ⚠ The text does not state what chr() returned for negative arguments in prior releases.

Actions:
- Find chr() calls in application SQL, functions, views and triggers and make sure arguments cannot be negative (e.g., validate or guard inputs) before upgrading.

### public schema owned by pg_database_owner in new clusters/databases

`postgresql_cfb6c3d3ce` · low · confidence low · introduced in 15 · fires at first_use

Starting in PostgreSQL 15, the public schema in new database clusters and newly-created databases in existing clusters is owned by the pg_database_owner role instead of the bootstrap superuser. Each database's owner therefore gets ownership privileges on public. Upgraded clusters and restored dumps keep their existing ownership. Provisioning scripts, privilege audits or security assumptions that expect public to be owned by the bootstrap superuser may behave differently for databases created after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where the public schema owner changed to pg_database_owner. (confidence high, judge supported)
  - pg_release_notes@15: "Change the owner of the public schema to be the new pg_database_owner role"
- **[required] deployment** `present` `"new cluster (initdb) or CREATE DATABASE after upgrade"`: The deployment creates new database clusters or new databases in existing clusters after upgrading. (confidence high, judge supported)
  - pg_release_notes@15: "This change applies to new database clusters and to newly-created databases in existing clusters."
- **[disqualifying] database** `present` `"database upgraded via pg_upgrade or restored from dump"`: The database is an existing database carried over by pg_upgrade or restored from a dump, so its existing public ownership is preserved. (confidence high, judge supported)
  - pg_release_notes@15: "Upgrading a cluster or restoring a database dump will preserve public's existing ownership specification."
- **[required] behavior** `present` `"assumption that public is owned by bootstrap superuser"`: Scripts, audits or security policies assume the public schema is owned by the bootstrap superuser, or that non-superuser database owners cannot control it. (confidence low, judge supported)
  - pg_release_notes@15: "Previously it was owned by the bootstrap superuser, so that non-superuser database owners could not do anything with it."
  - ⚠ The text does not describe specific breakages; impact on applications is inferred from the ownership change.

Actions:
- Check the owner of the public schema in newly created databases: SELECT pg_get_userbyid(nspowner) FROM pg_namespace WHERE nspname='public';
- Review provisioning scripts and privilege audits that assume public is owned by the bootstrap superuser.
- If the prior ownership is required, explicitly run ALTER SCHEMA public OWNER TO the desired role after creating new databases.

### libpq and client programs resolve home directory from HOME instead of passwd database

`postgresql_d48cf30f17` · low · confidence low · introduced in 15 · fires at upgrade

Starting in PostgreSQL 15, on non-Windows platforms libpq and various client applications use the HOME environment variable to locate the user's home directory, for example when looking up ~/.pgpass. They fall back to the <pwd.h> database only when HOME is empty or unset. If a client process has HOME set to a different directory than its passwd home directory, files such as ~/.pgpass may be looked up in a different location after the upgrade. Where the files actually live is an inference; the text does not state it.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where libpq and client programs began consulting HOME to find the home directory. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "On non-Windows platforms, consult the HOME environment variable to find the user's home directory"
- **[required] runtime** `not_equals` `"Windows"`: Client programs or libpq-based applications run on a non-Windows platform. (confidence high, judge supported)
  - pg_release_notes@15: "On non-Windows platforms, consult the HOME environment variable"
- **[required] configuration** `present` `".pgpass"`: The client relies on files in the home directory that libpq or client applications read, such as ~/.pgpass. (confidence medium, judge supported)
  - pg_release_notes@15: "This change affects libpq (for example, while looking up ~/.pgpass) as well as various client application programs."
  - ⚠ The text gives ~/.pgpass only as an example; it does not list the other affected files or client programs.
- **[required] deployment** `not_equals` `"passwd home directory"`: The HOME environment variable in the client process is set to a directory other than the user's passwd (<pwd.h>) home directory. (confidence low, judge partially_supported)
  - pg_release_notes@15: "consult the HOME environment variable to find the user's home directory"
  - ⚠ The text does not state the impact when HOME differs from the passwd entry; the mismatch scenario is inferred.
- **[disqualifying] deployment** `absent` `"HOME"`: HOME is empty or unset, in which case the previous <pwd.h> lookup is still used. (confidence high, judge supported)
  - pg_release_notes@15: "If HOME is empty or unset, fall back to the previous method of checking the <pwd.h> database."

Actions:
- For each client environment, verify that HOME points to the directory containing ~/.pgpass and other client files, or move those files to $HOME.
- Test client authentication that relies on .pgpass in service, cron and container environments after upgrading the client libraries.

### var_samp/stddev_samp numeric single-NaN returns NULL

`postgresql_dc64bb7d33` · low · confidence high · introduced in 14 · fires at first_use

In PostgreSQL 14+, var_samp() and stddev_samp() with numeric parameters return NULL instead of NaN when the input is a single NaN value. Queries or application logic expecting NaN in this case will see NULL.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14 (13 -> 16). (confidence high, judge supported)
  - pg_release_notes@14: "Change var_samp() and stddev_samp() with numeric parameters to return NULL when the input is a single NaN value"
- **[required] api_usage** `present` `"var_samp|stddev_samp"`: The application calls var_samp() or stddev_samp() with numeric parameters. (confidence high, judge supported)
  - pg_release_notes@14: "Change var_samp() and stddev_samp() with numeric parameters"
- **[required] behavior** `equals` `"single NaN input"`: The aggregated input set consists of a single NaN value and the application relies on NaN being returned. (confidence high, judge supported)
  - pg_release_notes@14: "return NULL when the input is a single NaN value"
  - pg_release_notes@14: "Previously NaN was returned."

Actions:
- Review queries using var_samp()/stddev_samp() on numeric columns and handle NULL results (e.g., via COALESCE) where NaN was previously expected for single-NaN inputs.
- Update tests that assert NaN output for single-NaN numeric inputs to these aggregates.

### Regex character class ranges using \w as start or end now rejected

`postgresql_f1a6f3c268` · low · confidence medium · introduced in 14 · fires at first_use

Starting in PostgreSQL 14, regular expressions that use \w as a range start or end inside a character class (e.g. [\w-z]) are disallowed. Previously they were accepted but produced unexpected results; such patterns will now raise errors when evaluated.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14 (13 -> 16), where \w as a range endpoint in character classes became disallowed. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow \w as a range start or end in regular expression character classes"
- **[required] api_usage** `present` `"\\w used as range endpoint in a regex bracket expression"`: The application or database objects use regular expressions with a character class range whose start or end is \w (e.g. [\w-z] or [a-\w]). (confidence medium, judge supported)
  - pg_release_notes@14: "Disallow \w as a range start or end in regular expression character classes"
  - ⚠ The text does not state whether the failure is an error at pattern compile time or another behavior; 'Disallow' implies an error.

Actions:
- Search application SQL, stored functions, CHECK constraints, views and indexes for regex bracket expressions using \w as a range start or end.
- Rewrite such patterns to state the intended characters explicitly (e.g. list \w and '-' separately, or use explicit ranges), since the old behavior produced unexpected results anyway.
- Test the affected regular expressions against PostgreSQL 14+ before upgrading.

### SSL compression support removed

`postgresql_f7dd029384` · low · confidence low · introduced in 14 · fires at upgrade

PostgreSQL 14 removes support for SSL compression. It was already disabled by default, so only deployments or clients that explicitly enabled SSL compression (e.g. via the libpq sslcompression connection option) would be affected.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where SSL compression support was removed (confidence high, judge supported)
  - pg_release_notes@14: "Remove support for SSL compression"
- **[required] configuration** `present` `"sslcompression=1"`: The deployment or client connections explicitly enable SSL compression (confidence low, judge supported)
  - pg_release_notes@14: "This was already disabled by default in previous PostgreSQL releases"
  - ⚠ The text does not name the specific setting (e.g. libpq sslcompression) or state whether connections that request compression will error or silently proceed without it.

Actions:
- Search connection strings and client configuration for sslcompression and remove it.
- Verify that clients connecting with SSL still work against PostgreSQL 16 without compression.

## Review checklist

### Low confidence or disputed

- [ ] postgresql_987fccfe8d: Legacy Boolean-like password_encryption values rejected
- [ ] postgresql_d94a442769: Stored empty lexemes in tsvector data
- [ ] postgresql_20f9520b98: Role inheritance status now fixed per membership at GRANT time
- [ ] postgresql_c49690050a: hash_mem_multiplier default raised to 2.0
- [ ] postgresql_fcfbbf6b55: PUBLIC CREATE privilege removed from public schema in new clusters/databases
- [ ] postgresql_369e7506c5: ecpg doubled quote mark handling in SQL command strings
- [ ] postgresql_cfb6c3d3ce: public schema owned by pg_database_owner in new clusters/databases
- [ ] postgresql_d48cf30f17: libpq and client programs resolve home directory from HOME instead of passwd database
- [ ] postgresql_f7dd029384: SSL compression support removed

### Inferred conditions

- [ ] postgresql_6c2fefbf87: Application SQL uses postfix operator syntax (e.g., factorial `n !`)
- [ ] postgresql_987fccfe8d: password_encryption is set to a legacy Boolean-like value, such as on, off, true, false, yes, no, 1 or 0.
- [ ] postgresql_b3c76f57c9: The subscription owner may also need ordinary privileges on target tables now that apply runs as that role.
- [ ] postgresql_d94a442769: The database contains stored tsvector values that include empty lexemes.
- [ ] postgresql_063d5aa8bb: Clients, drivers, or authentication configuration depend on md5-stored passwords and may fail once passwords are stored as SCRAM-SHA-256.
- [ ] postgresql_20f9520b98: The application or administration tooling changes a role's inheritance status (e.g. ALTER ROLE ... INHERIT/NOINHERIT) and relies on that change affecting existing memberships.
- [ ] postgresql_20f9520b98: Roles with non-default inheritance status (NOINHERIT) exist and have members granted, so memberships depend on the role's inheritance status.
- [ ] postgresql_4645b4b0d2: Input strings contain newlines, so matching results differ
- [ ] postgresql_55fa40f078: The deployment relies on these commands to reindex system catalog indexes
- [ ] postgresql_755a05d0ae: Application relies on reproducible random() output for a given seed (e.g. via setseed())
- [ ] postgresql_c49690050a: The deployment does not explicitly set hash_mem_multiplier, so it relies on the default value.
- [ ] postgresql_fcfbbf6b55: Application roles other than the database owner create tables or other objects in the public schema and rely on PUBLIC having CREATE privilege
- [ ] postgresql_1bae1f0746: Code or tests parse or compare EXPLAIN output and expect the actual temporary schema name (e.g. pg_temp_N).
- [ ] postgresql_28d15925c3: The application or its tests depend on the previous (incorrect) results of such window queries.
- [ ] postgresql_369e7506c5: The application contains workarounds for the old incorrect quote handling that would behave differently now that doubled quotes are processed correctly.
- [ ] postgresql_6642146d25: The function is called with interval values large enough to overflow during justification, and the new handling is likely an error rather than a silently wrong result.
- [ ] postgresql_cfb6c3d3ce: Scripts, audits or security policies assume the public schema is owned by the bootstrap superuser, or that non-superuser database owners cannot control it.
- [ ] postgresql_d48cf30f17: The HOME environment variable in the client process is set to a directory other than the user's passwd (<pwd.h>) home directory.
- [ ] postgresql_f7dd029384: The deployment or client connections explicitly enable SSL compression

### Source disagreements


### Open questions

- Extensions (PostGIS, TimescaleDB, pg_partman, etc.) must have builds for the target major; their compatibility is not in core release notes.
- Backup and HA tooling (pgBackRest, Barman, Patroni, logical replication tools) and client drivers have their own version support.
- Managed services (RDS, Cloud SQL, Azure) control the upgrade method and some defaults.
- Minor-release notes (14.x, 15.x, 16.x) were intentionally excluded; they can contain post-release behavior fixes.
- [postgresql_b3c76f57c9] Unconfirmed: The subscription owner may also need ordinary privileges on target tables now that apply runs as that role. (The text only states the row-level security restriction; it does not explicitly state other privilege checks on target tables.)
- [postgresql_063d5aa8bb] Unconfirmed: Clients, drivers, or authentication configuration depend on md5-stored passwords and may fail once passwords are stored as SCRAM-SHA-256. (The text does not describe any client compatibility or authentication impact; this impact is inferred.)
- [postgresql_55fa40f078] Unconfirmed: The deployment relies on these commands to reindex system catalog indexes (Whether a given deployment depends on system catalog reindexing via REINDEX DATABASE cannot be determined from the text.)
- [postgresql_28d15925c3] Unconfirmed: The application or its tests depend on the previous (incorrect) results of such window queries. (The text does not describe what the incorrect results were, so the scope of the output difference is unknown.)
- [postgresql_369e7506c5] Unconfirmed: The application contains workarounds for the old incorrect quote handling that would behave differently now that doubled quotes are processed correctly. (The text does not state what impact, if any, the fix has on existing programs beyond fixing the syntax errors.)
- [postgresql_6642146d25] Unconfirmed: The function is called with interval values large enough to overflow during justification, and the new handling is likely an error rather than a silently wrong result. (The text does not say what happens when overflow is detected (for example, raising an error), nor what the previous behavior was.)

## Context facts (not risks)


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
