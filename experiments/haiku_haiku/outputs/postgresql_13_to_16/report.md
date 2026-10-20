# PostgreSQL 13 → 16: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

PostgreSQL 13 -> 16 crosses 3 release(s) (14, 15, 16). 69 risk paths: 17 high, 27 medium, 23 low. Main risk types: changed_behavior (37), removed_api (17), configuration_change (8). 8 context facts and 0 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 16, "by_code": {"W4_no_search_queries": 16}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| high | high | configuration_change | configuration | 14 | `postgresql_0690043907` pg_hba.conf clientcert values 1, 0, no-verify |
| high | medium | removed_api | application_code | 15 | `postgresql_0aeb9394ab` pg_dump --no-synchronized-snapshots option removed |
| high | high | removed_api | application_code | 14 | `postgresql_12484be158` numeric_fac() function removed |
| high | medium | configuration_change | configuration | 14 | `postgresql_1cdbf7dda4` pg_hba.conf clientcert verify-ca with cert authentication |
| high | medium | removed_api | application_code | 15 | `postgresql_230760360c` libpq PQsendQuery() in pipeline mode |
| high | medium | removed_api | application_code | 15 | `postgresql_272d063f3f` Renamed exclusive backup functions pg_start_backup/pg_stop_backup |
| high | high | removed_api | application_code | 15 | `postgresql_4345c09353` xml2 xml_is_well_formed removed |
| high | medium | removed_api | application_code | 16 | `postgresql_434e0c374b` Removed pg_walinspect till_end_of_wal functions |
| high | medium | configuration_change | configuration | 14 | `postgresql_45d46c5bee` legacy Boolean-like password_encryption values no longer accepted |
| high | medium | removed_api | application_code | 14 | `postgresql_601636b28d` Factorial operators ! and !! removed |
| high | high | changed_behavior | database | 15 | `postgresql_6e42608977` Indexes relying on text output of interval values fail to create |
| high | high | removed_api | database | 15 | `postgresql_7bfe01bbb4` Server-side Python language plpython2u or plpythonu in use |
| high | medium | changed_behavior | application_code | 14 | `postgresql_7ef197b14c` User-defined objects referencing built-in array function signatures |
| high | medium | changed_behavior | database | 16 | `postgresql_80f2889427` Primary keys defined with NULLS NOT DISTINCT indexes |
| high | medium | removed_api | application_code | 15 | `postgresql_91ba33fe94` Removed functions pg_backup_start_time and pg_is_in_backup |
| high | medium | removed_api | application_code | 14 | `postgresql_d00aff3b01` Removed containment operators @ and ~ for geometric types and cube, hstore, intarray, seg |
| high | medium | removed_api | application_code | 16 | `postgresql_d309fcf838` Manually created views using ON SELECT rules |
| medium | medium | changed_behavior | database | 15 | `postgresql_0021c27ab7` Subscription owner lacks SELECT on replicated table for UPDATE/DELETE |
| medium | medium | removed_api | deployment | 14 | `postgresql_01631e9f8c` pg_standby contrib program removed |
| medium | high | changed_default | configuration | 14 | `postgresql_063d5aa8bb` password_encryption default changed to scram-sha-256 |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_27194e765d` to_tsquery() output change for text with discarded tokens |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_2a4f5f5ead` psql --single-transaction final COMMIT without ON_ERROR_STOP |
| medium | medium | changed_behavior | deployment | 16 | `postgresql_55fa40f078` REINDEX DATABASE and reindexdb no longer process system catalog indexes |
| medium | medium | changed_behavior | database | 15 | `postgresql_5e13cfd71d` login-role-self-membership-management |
| medium | medium | changed_behavior | database | 16 | `postgresql_5f2b8ce7c3` CREATEROLE role modification restricted |
| medium | medium | configuration_change | configuration | 16 | `postgresql_614faa535b` promote_trigger_file server variable removed in 16 |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_724a97cbad` EXTRACT(date) errors on units not in the date type |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_72e0855f91` array_to_tsvector empty-string array element error |
| medium | medium | changed_behavior | database | 15 | `postgresql_7ac0a4c348` logical_replication_rls_target_tables |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_85602454ed` tablefunc normal_rand() negative input |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_86d8236c5c` EXTRACT() return type changed from float8 to numeric |
| medium | medium | configuration_change | configuration | 16 | `postgresql_892ed5d374` force_parallel_mode server variable renamed to debug_parallel_query |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_9623a24b4c` websearch_to_tsquery() output change for quoted text with discarded tokens |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_9a56057ff7` chr() negative argument now raises an error |
| medium | medium | changed_behavior | application_code | 15 | `postgresql_9c0dce9d59` Numeric literals with non-numeric trailing characters |
| medium | medium | changed_behavior | database | 16 | `postgresql_9d3f729496` Mixed generated and non-generated columns in inherited or partitioned tables |
| medium | high | changed_behavior | application_code | 14 | `postgresql_b9a4dfaa79` Regex \D and \W shorthands in newline-sensitive mode |
| medium | medium | changed_behavior | application_code | 16 | `postgresql_b9ad526348` plpgsql_bound_cursor_portal_name |
| medium | medium | changed_behavior | application_code | 14 | `postgresql_bc249e57a2` Single-quoted language name in CREATE/DROP LANGUAGE |
| medium | medium | changed_default | database | 15 | `postgresql_bc7ea5414c` public schema CREATE permission removed by default in new databases |
| medium | medium | changed_default | application_code | 15 | `postgresql_c3d0f02569` custom_scan_provider_projection_support |
| medium | medium | data_migration | deployment | 15 | `postgresql_c9d93d5231` Upgrade from 13 to 16 requires a dump/restore, pg_upgrade or logical replication to migrate data |
| medium | medium | removed_api | application_code | 16 | `postgresql_cc8d8091c1` Removed server variables lc_collate and lc_ctype |
| medium | medium | changed_behavior | application_code | 16 | `postgresql_f01d943d69` Role membership inheritance default changed by GRANT |
| low | medium | configuration_change | configuration | 14 | `postgresql_01f92d8bc8` vacuum_cleanup_index_scale_factor server parameter removed |
| low | medium | changed_behavior | application_code | 15 | `postgresql_076d7c8e08` Zero-length Unicode identifiers (U&"") in SQL |
| low | medium | changed_behavior | application_code | 14 | `postgresql_0e147761ab` factorial() with negative input |
| low | low | changed_behavior | application_code | 14 | `postgresql_167726bd25` has_column_privilege attribute-number checks on non-existent or dropped columns |
| low | medium | removed_api | configuration | 16 | `postgresql_1f2cea1199` Removed server variable vacuum_defer_cleanup_age |
| low | medium | changed_behavior | database | 15 | `postgresql_24f3172f15` CREATE OR REPLACE VIEW output column collation |
| low | medium | configuration_change | configuration | 15 | `postgresql_3346e4d810` Custom options matching installed extension names |
| low | high | operational_risk | deployment | 16 | `postgresql_39a2bc1f2e` postmaster binary symbolic link removal |
| low | high | changed_behavior | application_code | 15 | `postgresql_6642146d25` Interval justification functions now detect integer overflow |
| low | high | changed_behavior | application_code | 15 | `postgresql_755a05d0ae` random() output changes for a given seed |
| low | medium | changed_behavior | application_code | 15 | `postgresql_90c31fa6ac` Trailing junk after JSON numeric literals now rejected |
| low | high | removed_api | dependencies | 14 | `postgresql_99cd4201b9` Clients using wire protocol version 2 after upgrade |
| low | medium | removed_api | application_code | 14 | `postgresql_a5a16adb33` postfix_operator_removal |
| low | high | configuration_change | configuration | 14 | `postgresql_a7d566002e` operator_precedence_warning server parameter removed in 16 |
| low | medium | changed_behavior | application_code | 14 | `postgresql_c26657934e` intarray containment operators no longer use GiST indexes |
| low | medium | changed_default | configuration | 15 | `postgresql_c49690050a` hash_mem_multiplier default change to 2.0 |
| low | medium | changed_behavior | application_code | 14 | `postgresql_c62dd64ad1` Regex back-references ignore anchor and other constraints |
| low | medium | changed_default | database | 15 | `postgresql_cfb6c3d3ce` public schema owner changes to pg_database_owner in newly created databases |
| low | medium | changed_behavior | runtime | 15 | `postgresql_d48cf30f17` Home directory lookup via HOME on non-Windows platforms |
| low | medium | changed_behavior | application_code | 15 | `postgresql_d490291822` interval-fractional-input-rounding |
| low | medium | changed_behavior | application_code | 14 | `postgresql_dc64bb7d33` var_samp_stddev_samp_single_nan_null |
| low | medium | changed_behavior | application_code | 15 | `postgresql_de18b5aa7c` char_type_non_ascii_output_format |
| low | medium | changed_behavior | application_code | 14 | `postgresql_f1a6f3c268` Regex character class with \w as range start or end |
| unknown | medium | changed_behavior | configuration | 14 | `postgresql_5b9c633eb1` Custom server parameter names with characters invalid in unquoted SQL identifiers |
| unknown | high | removed_api | configuration | 15 | `postgresql_a1802b44d1` Removed server variable stats_temp_directory |

### pg_hba.conf clientcert values 1, 0, no-verify

`postgresql_0690043907` · high · confidence high · introduced in 14 · fires at upgrade

Values 1/0/no-verify for clientcert in pg_hba.conf are no longer supported; only verify-ca and verify-full can be used.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the clientcert change was introduced. (confidence high, judge supported)
  - pg_release_notes@14: "Overhaul the specification of clientcert in pg_hba.conf"
- **[uncertain] configuration** `equals` `"1|0|no-verify"`: pg_hba.conf sets clientcert to 1, 0, or no-verify. (confidence low, judge not_supported)
  - pg_release_notes@14: "Values 1/0/no-verify are no longer supported"
  - ⚠ The text does not state the exact pg_hba.conf line syntax; the search regex assumes key=value form.
  - ⚠ Judge: evidence does not support this claim. The quote says the values 1/0/no-verify are no longer supported in release 14, which contradicts the claim that pg_hba.conf sets clientcert to these values.

Actions:
- Replace clientcert values 1, 0, or no-verify in pg_hba.conf with verify-ca or verify-full before upgrading.

### pg_dump --no-synchronized-snapshots option removed

`postgresql_0aeb9394ab` · high · confidence medium · introduced in 15 · fires at first_use

The pg_dump option --no-synchronized-snapshots has been removed. Scripts or jobs that pass this option to pg_dump may fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the option was removed. (confidence high, judge supported)
  - pg_release_notes@15: "Remove pg_dump's --no-synchronized-snapshots option (Tom Lane)"
- **[required] api_usage** `present` `"--no-synchronized-snapshots"`: Application code, scripts, or deployment jobs invoke pg_dump with the --no-synchronized-snapshots option. (confidence medium, judge supported)
  - pg_release_notes@15: "Remove pg_dump's --no-synchronized-snapshots option (Tom Lane)"
  - ⚠ The text does not state the exact error pg_dump gives when the removed option is passed.
- **[optional] behavior** `unknown` `""`: All still-supported server versions support synchronized snapshots, so the option is no longer needed. (confidence high, judge supported)
  - pg_release_notes@15: "All still-supported server versions support synchronized snapshots, so there's no longer a need for this option."

Actions:
- Search scripts and job definitions for --no-synchronized-snapshots and remove the option from pg_dump invocations.
- Run pg_dump commands in a test environment on the target version to confirm they run without the removed option.

### numeric_fac() function removed

`postgresql_12484be158` · high · confidence high · introduced in 14 · fires at upgrade

The function numeric_fac() is removed in release 14, so calls to it will fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the function numeric_fac() is removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!, as well as function numeric_fac()"
- **[required] api_usage** `present` `"numeric_fac"`: The application or database objects call the function numeric_fac(). (confidence high, judge supported)
  - pg_release_notes@14: "as well as function numeric_fac()"

Actions:
- Replace calls to numeric_fac() with the factorial() function, which the text states is still supported.
- Test the affected queries and objects on the new version after the upgrade.

### pg_hba.conf clientcert verify-ca with cert authentication

`postgresql_1cdbf7dda4` · high · confidence medium · introduced in 14 · fires at upgrade

verify-ca is disallowed when cert authentication is enabled, because cert requires verify-full checking.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the clientcert change was introduced. (confidence high, judge supported)
  - pg_release_notes@14: "Overhaul the specification of clientcert in pg_hba.conf"
- **[uncertain] configuration** `equals` `"verify-ca"`: pg_hba.conf sets clientcert to verify-ca while cert authentication is enabled. (confidence low, judge not_supported)
  - pg_release_notes@14: "disallow verify-ca if cert authentication is enabled since cert requires verify-full checking."
  - ⚠ The text does not state how cert authentication is enabled in pg_hba.conf.
  - ⚠ Judge: evidence does not support this claim. The quote says verify-ca is disallowed when cert authentication is enabled, which contradicts a pg_hba.conf setting of clientcert to verify-ca alongside enabled cert authentication.
- **[required] configuration** `present` `"cert"`: Cert authentication is enabled in pg_hba.conf. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "cert authentication is enabled"

Actions:
- Change clientcert from verify-ca to verify-full for any entry using cert authentication.

### libpq PQsendQuery() in pipeline mode

`postgresql_230760360c` · high · confidence medium · introduced in 15 · fires at first_use

libpq's PQsendQuery() is no longer supported in pipeline mode. Applications using that combination must be modified to use PQsendQueryParams() instead.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where PQsendQuery() stopped being supported in pipeline mode. (confidence high, judge supported)
  - pg_release_notes@15: "libpq's PQsendQuery() function is no longer supported in pipeline mode"
- **[required] api_usage** `present` `"PQsendQuery()"`: The application calls PQsendQuery() while using pipeline mode. (confidence medium, judge supported)
  - pg_release_notes@15: "PQsendQuery() function is no longer supported in pipeline mode"
  - ⚠ The text does not describe how pipeline mode is entered in the application.

Actions:
- Modify applications that use PQsendQuery() in pipeline mode to use PQsendQueryParams() instead.

### Renamed exclusive backup functions pg_start_backup/pg_stop_backup

`postgresql_272d063f3f` · high · confidence medium · introduced in 15 · fires at upgrade

Exclusive backup mode was removed. The functions pg_start_backup() and pg_stop_backup() were renamed to pg_backup_start() and pg_backup_stop(), so code calling the old names must change.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the removal of exclusive backup mode. (confidence high, judge supported)
  - pg_release_notes@15: "Remove long-deprecated exclusive backup mode"
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases"
- **[required] api_usage** `present` `"pg_start_backup"`: The application calls pg_start_backup() or pg_stop_backup(). (confidence medium, judge supported)
  - pg_release_notes@15: "Functions pg_start_backup()/pg_stop_backup() have been renamed to pg_backup_start()/pg_backup_stop()"
  - ⚠ The text says the functions were renamed but does not explicitly state that the old names are no longer callable.

Actions:
- Replace calls to pg_start_backup() with pg_backup_start().
- Replace calls to pg_stop_backup() with pg_backup_stop().
- Use the non-exclusive backup mode, which the text describes as considered superior for all purposes.

### xml2 xml_is_well_formed removed

`postgresql_4345c09353` · high · confidence high · introduced in 15 · fires at upgrade

The xml2 module's xml_is_well_formed() function is removed in release 15. Application code or database objects that call it will fail after the upgrade. The text states the function has been implemented in the core backend since Postgres 9.1.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The source version is below 15, so the upgrade crosses release 15 (confidence high, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"xml_is_well_formed"`: Application code or database objects call xml_is_well_formed() (confidence high, judge supported)
  - pg_release_notes@15: "Remove xml2's xml_is_well_formed() function"
- **[required] dependency** `present` `"xml2"`: The xml2 extension is installed in the database (confidence high, judge supported)
  - pg_release_notes@15: "Remove xml2's xml_is_well_formed() function"

Actions:
- Replace calls to the xml2 xml_is_well_formed() function with the core backend implementation, which the text states has existed since Postgres 9.1.
- Verify after the change that calls resolve to the core function, since the text does not describe any behavioral difference between the two.

### Removed pg_walinspect till_end_of_wal functions

`postgresql_434e0c374b` · high · confidence medium · introduced in 16 · fires at upgrade

Release 16 removes the pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal(). Code that calls them will fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, the release that removes the pg_walinspect functions (confidence high, judge supported)
  - pg_release_notes@16: "Version 16 contains a number of changes that may affect compatibility with previous releases."
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal()"
- **[required] api_usage** `present` `"pg_get_wal_records_info_till_end_of_wal"`: The application calls pg_get_wal_records_info_till_end_of_wal() or pg_get_wal_stats_till_end_of_wal() (confidence high, judge supported)
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal()"
- **[required] dependency** `present` `"pg_walinspect"`: The application or deployment uses the pg_walinspect extension that provides these functions (confidence medium, judge supported)
  - pg_release_notes@16: "Remove pg_walinspect functions pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal()"
  - ⚠ The text does not state how the pg_walinspect extension is installed or which extension version provides these functions.

Actions:
- Find all callers of pg_get_wal_records_info_till_end_of_wal() and pg_get_wal_stats_till_end_of_wal() before upgrading to 16.
- The text does not name a replacement for these functions; check the release notes before changing those calls.
- Remove or replace the calls to the removed functions before the upgrade.

### legacy Boolean-like password_encryption values no longer accepted

`postgresql_45d46c5bee` · high · confidence medium · introduced in 14 · fires at upgrade

Legacy Boolean-like values that were previously synonyms for md5 are no longer accepted for password_encryption.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the change to password_encryption takes effect. (confidence high, judge supported)
  - pg_release_notes@14: "Change the default of the password_encryption server parameter to scram-sha-256"
- **[required] configuration** `present` `"password_encryption set to a Boolean-like value"`: The server configuration sets password_encryption to a legacy Boolean-like value previously synonymous with md5. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "the legacy (and undocumented) Boolean-like values which were previously synonyms for md5 are no longer accepted"
  - ⚠ The text does not state whether the server fails to start or only rejects the setting in some other way.

Actions:
- Search configuration files and parameter settings for password_encryption and identify any Boolean-like values.
- Replace any legacy Boolean-like password_encryption value before upgrading; the item does not name the accepted replacement values.

### Factorial operators ! and !! removed

`postgresql_601636b28d` · high · confidence medium · introduced in 14 · fires at upgrade

The factorial operators ! and !! are removed in release 14, so application SQL that uses them will fail after the upgrade. The text states that the factorial() function is still supported.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the factorial operators are removed. (confidence high, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!, as well as function numeric_fac()"
- **[required] api_usage** `present` `"!"`: The application or database objects use the factorial operator ! or !!. (confidence medium, judge supported)
  - pg_release_notes@14: "Remove factorial operators ! and !!"
  - ⚠ The text does not state how the operators are expressed in SQL, so the search patterns are heuristic.

Actions:
- Replace uses of the ! and !! factorial operators with the factorial() function, which the text states is still supported.
- Test the affected queries and objects on the new version after the upgrade.

### Indexes relying on text output of interval values fail to create

`postgresql_6e42608977` · high · confidence high · introduced in 15 · fires at first_use

The interval output function is now marked stable instead of immutable because it depends on IntervalStyle. This will, for example, cause creation of indexes relying on the text output of interval values to fail.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the interval output function volatility change was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "Mark the interval output function as stable, not immutable, since it depends on IntervalStyle"
- **[required] api_usage** `present` `"index relying on text output of interval values"`: The application or database creates an index that relies on the text output of interval values. (confidence high, judge supported)
  - pg_release_notes@15: "cause creation of indexes relying on the text output of interval values to fail"
- **[optional] configuration** `present` `"IntervalStyle"`: The index depends on settings that affect the interval text output, namely IntervalStyle. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "since it depends on IntervalStyle"
  - ⚠ The text does not state how IntervalStyle changes the text output used by indexes.

Actions:
- Identify indexes that rely on the text output of interval values before upgrading to 16.
- Review application code and migrations that create such indexes, since their creation is stated to fail after the change.

### Server-side Python language plpython2u or plpythonu in use

`postgresql_7bfe01bbb4` · high · confidence high · introduced in 15 · fires at upgrade

The server-side languages plpython2u and plpythonu were removed in release 15, so databases that define or call functions in these languages will not work after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the change was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu (Andres Freund)"
- **[alternative] database** `present` `"plpythonu"`: The database uses the plpythonu language. (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu"
- **[alternative] database** `present` `"plpython2u"`: The database uses the plpython2u language. (confidence high, judge supported)
  - pg_release_notes@15: "Remove server-side language plpython2u and generic Python language plpythonu"
- **[uncertain] behavior** `unknown` `"plpython3u"`: Whether the database could be affected through plpython3u is not stated in the text. (confidence low, judge partially_supported)
  - pg_release_notes@15: "While the original intent of plpythonu was that it could eventually refer to plpython3u"
  - ⚠ The text does not state whether plpython3u is available or affected after the upgrade.

Actions:
- Identify functions, procedures, and triggers that use plpythonu or plpython2u before upgrading.
- Migrate those routines to a supported language, because the text does not name a specific replacement language.

### User-defined objects referencing built-in array function signatures

`postgresql_7ef197b14c` · high · confidence medium · introduced in 14 · fires at upgrade

Built-in array functions and width_bucket() changed their argument types from anyarray to anycompatiblearray. User-defined objects that reference these function signatures must be dropped before upgrading and recreated after the upgrade completes.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which introduced the change to array function argument types. (confidence high, judge supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"user-defined objects referencing array function signatures"`: The database contains user-defined objects, such as aggregates and operators, that reference the array function signatures or width_bucket(). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "User-defined objects that reference certain built-in array functions along with their argument types must be recreated"
  - ⚠ The text names aggregates and operators as examples only and does not state a complete list of affected object types.

Actions:
- Before upgrading, identify user-defined objects such as aggregates and operators that reference the listed array function signatures or width_bucket().
- Drop those user-defined objects before upgrading.
- Recreate the objects once the upgrade completes, using the new anycompatiblearray argument types.

### Primary keys defined with NULLS NOT DISTINCT indexes

`postgresql_80f2889427` · high · confidence medium · introduced in 16 · fires at upgrade

Release 16 disallows NULLS NOT DISTINCT indexes for primary keys. Databases that define a primary key backed by such an index are affected by this change when moving to release 16. The text does not state the exact failure mode.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses into release 16, where the change takes effect. (confidence high, judge supported)
  - pg_release_notes@16: "Disallow NULLS NOT DISTINCT indexes for primary keys"
- **[required] database** `present` `"NULLS NOT DISTINCT"`: The database has a primary key whose backing index is defined with NULLS NOT DISTINCT. (confidence medium, judge supported)
  - pg_release_notes@16: "Disallow NULLS NOT DISTINCT indexes for primary keys"
  - ⚠ The text does not describe how these indexes are defined or what happens to them at upgrade time.

Actions:
- Search schema definitions and dump files for NULLS NOT DISTINCT on primary key indexes before upgrading to release 16.
- Review the upgrade guidance for the migration path, since the text states that dump/restore, pg_upgrade, or logical replication is required to migrate data from earlier releases.

### Removed functions pg_backup_start_time and pg_is_in_backup

`postgresql_91ba33fe94` · high · confidence medium · introduced in 15 · fires at upgrade

The functions pg_backup_start_time() and pg_is_in_backup() have been removed, so code calling them will no longer work after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which removed these functions. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Remove long-deprecated exclusive backup mode"
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases"
- **[alternative] api_usage** `present` `"pg_backup_start_time"`: The application calls pg_backup_start_time(). (confidence high, judge supported)
  - pg_release_notes@15: "the functions pg_backup_start_time() and pg_is_in_backup() have been removed"
- **[alternative] api_usage** `present` `"pg_is_in_backup"`: The application calls pg_is_in_backup(). (confidence high, judge supported)
  - pg_release_notes@15: "the functions pg_backup_start_time() and pg_is_in_backup() have been removed"

Actions:
- Remove or replace calls to pg_backup_start_time() and pg_is_in_backup() before upgrading.

### Removed containment operators @ and ~ for geometric types and cube, hstore, intarray, seg

`postgresql_d00aff3b01` · high · confidence medium · introduced in 14 · fires at upgrade

The deprecated containment operators @ and ~ were removed for built-in geometric data types and the contrib modules cube, hstore, intarray, and seg. Application code or SQL that uses these operators will no longer work after the upgrade. The text recommends <@ and @> instead.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the @ and ~ containment operators are removed. (confidence medium, judge supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~ for built-in geometric data types"
  - ⚠ The text does not state the exact version number of the release that removed the operators beyond the introduction in release 14.
- **[alternative] api_usage** `present` `"@"`: The application or database uses the @ containment operator. (confidence high, judge supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~"
- **[alternative] api_usage** `present` `"~"`: The application or database uses the ~ containment operator. (confidence high, judge supported)
  - pg_release_notes@14: "Remove deprecated containment operators @ and ~"
- **[required] api_usage** `contains` `"geometric data types"`: The operator is used on built-in geometric data types. (confidence high, judge supported)
  - pg_release_notes@14: "for built-in geometric data types and contrib modules cube, hstore, intarray, and seg"
- **[alternative] dependency** `present` `"cube, hstore, intarray, seg"`: The application uses the contrib modules cube, hstore, intarray, or seg. (confidence medium, judge supported)
  - pg_release_notes@14: "contrib modules cube, hstore, intarray, and seg"
  - ⚠ The text does not say which functions or operator signatures in these contrib modules are affected beyond the @ and ~ operators.
- **[uncertain] behavior** `unknown` `""`: The application relies on the containment operators, which the text says have been replaced by <@ and @>. (confidence low, judge partially_supported)
  - pg_release_notes@14: "The more consistently named <@ and @> have been recommended for many years."
  - ⚠ The text does not state a direct mapping from @ to <@ or from ~ to @>, nor any behavior differences between them.

Actions:
- Find uses of the @ and ~ operators on geometric types and on cube, hstore, intarray, and seg, and rewrite them before upgrading.
- Replace the removed operators with the <@ and @> operators, which the text recommends.
- Verify the rewritten queries return the same results on a test instance running version 16.

### Manually created views using ON SELECT rules

`postgresql_d309fcf838` · high · confidence medium · introduced in 16 · fires at upgrade

PostgreSQL 16 removes the ability to create views manually with ON SELECT rules. Code or schema that creates views this way is affected by the upgrade. The text does not name a replacement.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which introduces the removal of manual ON SELECT rule view creation. (confidence high, judge supported)
  - pg_release_notes@16: "Remove the ability to create views manually with ON SELECT rules"
- **[required] api_usage** `present` `"ON SELECT rules"`: The application or schema creates views manually with ON SELECT rules. (confidence medium, judge supported)
  - pg_release_notes@16: "Remove the ability to create views manually with ON SELECT rules"
  - ⚠ The text does not state whether views created by other means are affected, or what replaces manual ON SELECT rules.

Actions:
- Search the codebase and schema for manually created ON SELECT rules before upgrading to 16.
- Recreate affected views by a method that is supported in PostgreSQL 16; the text does not name a replacement.

### Subscription owner lacks SELECT on replicated table for UPDATE/DELETE

`postgresql_0021c27ab7` · medium · confidence medium · introduced in 15 · fires at first_use

Logical replication UPDATE and DELETE operations on a table will be rejected when the subscription owner does not have SELECT permission on that table.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15 (from 13 to 16). (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Prevent UPDATE and DELETE logical replication operations on tables where the subscription owner does not have SELECT permission on the table"
- **[required] behavior** `present` `"logical replication subscription replicating UPDATE or DELETE"`: The application or deployment uses logical replication subscriptions that replicate UPDATE or DELETE operations. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "UPDATE and DELETE commands typically involve reading the table as well"
- **[required] database** `absent` `"SELECT permission for subscription owner on the replicated table"`: The subscription owner does not have SELECT permission on the table being replicated. (confidence high, judge supported)
  - pg_release_notes@15: "where the subscription owner does not have SELECT permission on the table"

Actions:
- Grant SELECT permission on each replicated table to the subscription owner before upgrading to version 16.

### pg_standby contrib program removed

`postgresql_01631e9f8c` · medium · confidence medium · introduced in 14 · fires at upgrade

The contrib program pg_standby was removed in release 14. Deployments that invoke pg_standby (for example in standby recovery scripts) are affected by the removal when upgrading from 13 to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where pg_standby was removed. (confidence high)
  - pg_release_notes@14: "Remove contrib program pg_standby (Justin Pryzby)"
- **[required] deployment** `present` `"pg_standby"`: The deployment uses the pg_standby program. (confidence medium, judge supported)
  - pg_release_notes@14: "Remove contrib program pg_standby"
  - ⚠ The text does not state how pg_standby is used or name a replacement program.

Actions:
- Search recovery configuration and scripts for pg_standby usage before upgrading.
- Replace any pg_standby invocation with a supported alternative; the text does not name one.

### password_encryption default changed to scram-sha-256

`postgresql_063d5aa8bb` · medium · confidence high · introduced in 14 · fires at first_use

The default of password_encryption changes from md5 to scram-sha-256, so new passwords are stored as SHA256 unless the setting is changed or the password is specified in MD5 format.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the password_encryption default changed to scram-sha-256. (confidence high, judge supported)
  - pg_release_notes@14: "Change the default of the password_encryption server parameter to scram-sha-256"
- **[required] configuration** `not_equals` `"md5"`: The deployment relies on the default password_encryption value (not explicitly set to md5). (confidence high, judge supported)
  - pg_release_notes@14: "All new passwords will be stored as SHA256 unless this server setting is changed"
- **[uncertain] behavior** `unknown` `""`: Client applications that authenticate with md5-stored passwords are affected by SCRAM-stored passwords. (confidence low, judge partially_supported)
  - pg_release_notes@14: "All new passwords will be stored as SHA256"
  - ⚠ The text does not state whether clients that only support md5 authentication will fail to connect after the change.

Actions:
- Check whether password_encryption is set explicitly and decide whether to keep md5 or accept scram-sha-256 for new passwords.
- Verify that client drivers support the password storage and authentication method in use before relying on the new default.
- Note that the item only changes how new passwords are stored; passwords set with MD5 format are not covered by the new default.

### to_tsquery() output change for text with discarded tokens

`postgresql_27194e765d` · medium · confidence medium · introduced in 14 · fires at first_use

to_tsquery() now produces different tsquery output for query text containing discarded tokens such as underscore. Applications that rely on the previous output may return different search results after upgrading to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the to_tsquery() change was introduced (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Fix to_tsquery() and websearch_to_tsquery() to properly parse query text containing discarded tokens"
- **[required] api_usage** `present` `"to_tsquery()"`: The application calls to_tsquery() (confidence high, judge supported)
  - pg_release_notes@14: "caused the output of these functions to produce incorrect tsquery output"
- **[required] behavior** `contains` `"underscore"`: The query text passed to to_tsquery() contains discarded tokens such as underscore (confidence high, judge supported)
  - pg_release_notes@14: "Certain discarded tokens, like underscore"
- **[required] behavior** `present` `"changed tsquery output"`: Output of the query now differs from the previous output (confidence high, judge supported)
  - pg_release_notes@14: "now both output 'pg' <-> 'class' <-> 'pg'"

Actions:
- Find calls to to_tsquery() and review whether query text contains discarded tokens such as underscore.
- Compare to_tsquery() output for those inputs before and after the upgrade and update any dependent search logic.

### psql --single-transaction final COMMIT without ON_ERROR_STOP

`postgresql_2a4f5f5ead` · medium · confidence medium · introduced in 15 · fires at first_use

After an error in psql's --single-transaction mode, the final COMMIT is changed to ROLLBACK only if ON_ERROR_STOP is set, so scripts run with --single-transaction and without ON_ERROR_STOP may end differently after an error.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the final COMMIT is changed to ROLLBACK only if ON_ERROR_STOP is set. (confidence medium, judge supported)
  - pg_release_notes@15: "change the final COMMIT command to ROLLBACK only if ON_ERROR_STOP is set"
  - ⚠ The text does not state the exact prior behavior of the final COMMIT after an error.
- **[required] api_usage** `present` `"--single-transaction"`: The application or script runs psql in --single-transaction mode. (confidence high, judge supported)
  - pg_release_notes@15: "psql's --single-transaction mode"
- **[required] configuration** `absent` `"ON_ERROR_STOP"`: ON_ERROR_STOP is not set for the psql session. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "ON_ERROR_STOP is set"
  - ⚠ The text does not state what the final COMMIT does when ON_ERROR_STOP is not set, beyond not changing it to ROLLBACK.

Actions:
- Review scripts that run psql with --single-transaction and check whether they depend on the final COMMIT after an error.
- Set ON_ERROR_STOP in scripts where a rollback after an error is required.

### REINDEX DATABASE and reindexdb no longer process system catalog indexes

`postgresql_55fa40f078` · medium · confidence medium · introduced in 16 · fires at upgrade

REINDEX DATABASE and reindexdb no longer process indexes on system catalogs in release 16. Processing such indexes is still possible using REINDEX SYSTEM and reindexdb --system.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which introduced the change to REINDEX DATABASE and reindexdb. (confidence high, judge supported)
  - pg_release_notes@16: "Version 16 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"REINDEX DATABASE"`: The application or deployment uses REINDEX DATABASE or reindexdb to reindex system catalog indexes. (confidence medium, judge supported)
  - pg_release_notes@16: "Change REINDEX DATABASE and reindexdb to not process indexes on system catalogs"
  - ⚠ The text does not state how often or in what contexts REINDEX DATABASE or reindexdb is used to reindex system catalogs.
- **[disqualifying] api_usage** `present` `"REINDEX SYSTEM"`: The application or deployment already runs REINDEX SYSTEM or reindexdb --system to process system catalog indexes. (confidence high, judge supported)
  - pg_release_notes@16: "Processing such indexes is still possible using REINDEX SYSTEM and reindexdb --system."

Actions:
- Where system catalog indexes must be reindexed, run REINDEX SYSTEM or reindexdb --system separately, since REINDEX DATABASE and reindexdb no longer process them.

### login-role-self-membership-management

`postgresql_5e13cfd71d` · medium · confidence medium · introduced in 15 · fires at first_use

A login role that previously added or removed members of its own role without ADMIN OPTION will no longer have that default privilege in release 15 and later.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the change takes effect. (confidence high, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"login role self-membership management without ADMIN OPTION"`: The application or deployment has a login role that adds or removes members of its own role without holding ADMIN OPTION on that role. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "a login role could add/remove members of its own role"

Actions:
- Review scripts and applications where a login role grants or revokes membership in its own role.
- Grant ADMIN OPTION on the role to the login role where self-management of membership is still required.

### CREATEROLE role modification restricted

`postgresql_5f2b8ce7c3` · medium · confidence medium · introduced in 16 · fires at first_use

Roles with CREATEROLE can no longer change many aspects of non-superuser roles unless they also hold ADMIN OPTION permission, so role-management operations by such roles may fail after upgrade.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which introduced the restriction of CREATEROLE privileges. (confidence high, judge supported)
  - pg_release_notes@16: "Restrict the privileges of CREATEROLE and its ability to modify other roles"
- **[required] behavior** `present` `"CREATEROLE"`: The database uses non-superuser roles that hold CREATEROLE and modify other non-superuser roles. (confidence medium, judge supported)
  - pg_release_notes@16: "Previously roles with CREATEROLE privileges could change many aspects of any non-superuser role."
  - ⚠ The text does not state which target roles the ADMIN OPTION permission must apply to.
- **[disqualifying] behavior** `present` `"ADMIN OPTION"`: The role performing the change holds ADMIN OPTION permission, which avoids the new restriction. (confidence medium, judge supported)
  - pg_release_notes@16: "Such changes, including adding members, now require the role requesting the change to have ADMIN OPTION permission."
  - ⚠ The text does not state how ADMIN OPTION permission is checked or granted for each target role.

Actions:
- Review role-management scripts and tooling that rely on CREATEROLE to change other roles.
- Grant ADMIN OPTION permission to roles that need to add members or change properties of other roles, or grant the specific permissions such as CREATEDB, REPLICATION, or BYPASSRLS that the role requires.
- Test role administration workflows on a 16 instance before production upgrade.

### promote_trigger_file server variable removed in 16

`postgresql_614faa535b` · medium · confidence medium · introduced in 16 · fires at upgrade

The server variable promote_trigger_file was removed in release 16. Its use to promote a standby to primary is replaced by pg_ctl promote or pg_promote().

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which removes the server variable promote_trigger_file. (confidence high, judge supported)
  - pg_release_notes@16: "Remove server variable promote_trigger_file (Simon Riggs)"
- **[required] configuration** `present` `"promote_trigger_file"`: The application or deployment sets the server variable promote_trigger_file. (confidence medium, judge supported)
  - pg_release_notes@16: "Remove server variable promote_trigger_file (Simon Riggs)"
  - pg_release_notes@16: "This was used to promote a standby to primary"
  - ⚠ The text does not state whether a configuration that still sets promote_trigger_file fails at startup or is silently ignored after the upgrade.

Actions:
- Remove promote_trigger_file from postgresql.conf, ALTER SYSTEM settings, and deployment templates before upgrading to 16.
- To promote a standby, use pg_ctl promote or pg_promote() instead, as the release notes state.

### EXTRACT(date) errors on units not in the date type

`postgresql_724a97cbad` · medium · confidence medium · introduced in 14 · fires at first_use

EXTRACT(date) now throws an error for units that are not part of the date data type.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where EXTRACT(date) began raising an error for units not part of the date type. (confidence high, judge supported)
  - pg_release_notes@14: "Also, EXTRACT(date) now throws an error for units that are not part of the date data type."
- **[required] api_usage** `present` `"EXTRACT("`: The application calls EXTRACT() on date values with a unit that is not part of the date data type. (confidence medium, judge supported)
  - pg_release_notes@14: "EXTRACT(date) now throws an error for units that are not part of the date data type"
  - ⚠ The text does not list which units are not part of the date data type.

Actions:
- Search application code for EXTRACT() calls on date values and check the units used.
- Ensure units used with EXTRACT() on date values are ones that belong to the date data type.

### array_to_tsvector empty-string array element error

`postgresql_72e0855f91` · medium · confidence medium · introduced in 15 · fires at first_use

array_to_tsvector() now raises an error when passed an empty-string array element, because lexemes should never be empty. Applications passing such elements will fail at call time. Stored empty lexemes can also cause dump/restore failures and inconsistent results.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the array_to_tsvector() empty-string element error was introduced (source version is below 15). (confidence high)
  - pg_release_notes@15: "Generate an error if array_to_tsvector() is passed an empty-string array element"
- **[required] api_usage** `present` `"array_to_tsvector()"`: The application calls array_to_tsvector() with an empty-string array element. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "passed an empty-string array element"
- **[optional] database** `present` `"empty lexemes stored"`: The database stores tsvector values containing empty lexemes. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Users of previous Postgres releases should verify that no empty lexemes are stored"

Actions:
- Verify that no empty lexemes are stored before upgrading.
- Change application code so array_to_tsvector() is not passed empty-string array elements.
- Check for empty lexemes before running a dump/restore or pg_upgrade migration.

### logical_replication_rls_target_tables

`postgresql_7ac0a4c348` · medium · confidence medium · introduced in 15 · fires at first_use

Logical replication can run as the subscription owner. Because row-level security policies are not checked, replication into tables with row-level security policies is limited to superusers, roles with bypassrls, and table owners.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The change is introduced in release 15 and the upgrade crosses release 15. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Allow logical replication to run as the owner of the subscription"
- **[required] behavior** `present` `"row-level security policies"`: The deployment uses logical replication to replicate into tables that have row-level security policies. (confidence high, judge supported)
  - pg_release_notes@15: "replicate into tables with row-level security policies"
- **[uncertain] configuration** `unknown` `"run as owner"`: The subscription runs as the subscription owner. (confidence low, judge supported)
  - pg_release_notes@15: "Allow logical replication to run as the owner of the subscription"
  - ⚠ The text does not state the setting name or whether running as the owner is the default or an opt-in choice.
- **[disqualifying] behavior** `equals` `"superuser, bypassrls role, or table owner"`: The subscription owner is not a superuser, does not have bypassrls, and does not own the target table. (confidence high, judge supported)
  - pg_release_notes@15: "only superusers, roles with bypassrls, and table owners can replicate into tables with row-level security policies"

Actions:
- Identify logical replication subscriptions that replicate into tables with row-level security policies.
- Confirm that the subscription owner is a superuser, has bypassrls, or owns each target table before relying on replication after the upgrade.

### tablefunc normal_rand() negative input

`postgresql_85602454ed` · medium · confidence medium · introduced in 14 · fires at first_use

The tablefunc function normal_rand() no longer accepts negative values after the upgrade. Application code that passes negative values to it may behave differently.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses PostgreSQL release 14 (from a version below 14). (confidence high)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"normal_rand()"`: The application or database calls tablefunc's normal_rand() with negative values. (confidence medium, judge supported)
  - pg_release_notes@14: "Prevent tablefunc's function normal_rand() from accepting negative values"
  - ⚠ The text does not state what happens to negative inputs after the change, such as an error or a different result.

Actions:
- Find calls to normal_rand() and check whether any pass negative values before upgrading.
- Change calls that pass negative values so they use non-negative arguments.
- Test normal_rand() calls after the upgrade to confirm expected results.

### EXTRACT() return type changed from float8 to numeric

`postgresql_86d8236c5c` · medium · confidence medium · introduced in 14 · fires at first_use

EXTRACT() now returns numeric instead of float8. The text says the old behavior can still be obtained by using the old underlying function date_part().

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where EXTRACT() changed its return type. (confidence high, judge supported)
  - pg_release_notes@14: "Change EXTRACT() to return type numeric instead of float8"
- **[required] api_usage** `present` `"EXTRACT("`: The application calls EXTRACT() and depends on its float8 return type. (confidence medium, judge supported)
  - pg_release_notes@14: "Change EXTRACT() to return type numeric instead of float8"
  - ⚠ The text says the change avoids loss-of-precision issues in some usages but does not state which usages or result types are affected.

Actions:
- Search application code for EXTRACT() calls and check whether the results depend on float8 return values.
- Where the previous float8 behavior is required, use date_part() instead of EXTRACT().

### force_parallel_mode server variable renamed to debug_parallel_query

`postgresql_892ed5d374` · medium · confidence medium · introduced in 16 · fires at upgrade

The server variable force_parallel_mode was renamed to debug_parallel_query in release 16, so deployments that set or reference the old name must use the new name.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which introduced the rename of force_parallel_mode. (confidence medium, judge partially_supported)
  - pg_release_notes@16: "Rename server variable force_parallel_mode to debug_parallel_query"
- **[required] configuration** `present` `"force_parallel_mode"`: The application or deployment sets or references the server variable force_parallel_mode. (confidence medium, judge supported)
  - pg_release_notes@16: "Rename server variable force_parallel_mode to debug_parallel_query"
  - ⚠ The text does not state what happens when the old name is still set after the upgrade (for example whether startup fails or the setting is ignored).

Actions:
- Search configuration files, deployment manifests and scripts for force_parallel_mode and replace it with debug_parallel_query.
- Verify the server accepts the configuration after the upgrade.

### websearch_to_tsquery() output change for quoted text with discarded tokens

`postgresql_9623a24b4c` · medium · confidence medium · introduced in 14 · fires at first_use

websearch_to_tsquery() now produces different tsquery output for quoted query text containing discarded tokens such as underscore. Applications that rely on the previous output may return different search results after upgrading to 16.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the websearch_to_tsquery() change was introduced (confidence high, judge supported)
  - pg_release_notes@14: "Fix to_tsquery() and websearch_to_tsquery() to properly parse query text containing discarded tokens"
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"websearch_to_tsquery()"`: The application calls websearch_to_tsquery() (confidence medium, judge supported)
  - pg_release_notes@14: "caused the output of these functions to produce incorrect tsquery output"
  - pg_release_notes@14: "Fix websearch_to_tsquery() to properly parse multiple adjacent discarded tokens in quotes"
  - ⚠ The text does not state how the function is invoked by applications; only the function name is given.
- **[required] behavior** `contains` `"underscore"`: The query text passed to websearch_to_tsquery() contains discarded tokens such as underscore (confidence medium, judge supported)
  - pg_release_notes@14: "Certain discarded tokens, like underscore"
  - pg_release_notes@14: "Previously, quoted text that contained multiple adjacent discarded tokens was treated as multiple tokens"
  - ⚠ The text does not state which inputs the application passes to the function.
- **[required] behavior** `present` `"changed tsquery output"`: Output of the query now differs from the previous output (confidence high, judge supported)
  - pg_release_notes@14: "now both output 'pg' <-> 'class' <-> 'pg'"

Actions:
- Find calls to websearch_to_tsquery() and review whether quoted query text contains discarded tokens such as underscore.
- Compare websearch_to_tsquery() output for those inputs before and after the upgrade and update any dependent search logic.
- Search the codebase for websearch_to_tsquery calls and identify any that receive quoted text with multiple adjacent discarded tokens.
- Re-run affected queries or tests on PostgreSQL 16 and compare the tsquery output and search results with the previous release.

### chr() negative argument now raises an error

`postgresql_9a56057ff7` · medium · confidence medium · introduced in 15 · fires at first_use

In PostgreSQL 16, chr() supplied with a negative argument generates an error instead of the prior behavior. Application code or SQL that passes a negative value to chr() may fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the chr() negative argument change was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
  - ⚠ The text names the change as introduced in release 15 but the item itself does not restate the version number.
- **[required] api_usage** `present` `"chr() called with a negative argument"`: The application or database calls chr() with a negative argument. (confidence medium, judge supported)
  - pg_release_notes@15: "when chr() is supplied with a negative argument"
  - ⚠ The text does not state the exact error message or how chr() behaved for negative arguments before the change.

Actions:
- Search application code and database objects for chr() calls and check whether any can receive a negative argument.
- Handle negative inputs to chr() before upgrading to PostgreSQL 16.

### Numeric literals with non-numeric trailing characters

`postgresql_9c0dce9d59` · medium · confidence medium · introduced in 15 · fires at first_use

Query text that places non-numeric characters directly after a numeric literal, such as 123abc, was previously parsed as the number followed by a separate token. The change prevents numeric literals from having such trailing characters, so affected query text behaves differently after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the numeric literal change was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Prevent numeric literals from having non-numeric trailing characters"
- **[required] behavior** `present` `"numeric literal followed by non-numeric characters"`: Application query text contains a numeric literal immediately followed by non-numeric characters. (confidence medium, judge supported)
  - pg_release_notes@15: "Previously, query text like 123abc would be interpreted as 123 followed by a separate token abc."
  - ⚠ The text does not state whether the behavior change produces an error or a different result for every affected query form.

Actions:
- Search application SQL and query text for numeric literals directly followed by letters or underscores and review each match.
- Test the affected queries against PostgreSQL 16 after the upgrade.

### Mixed generated and non-generated columns in inherited or partitioned tables

`postgresql_9d3f729496` · medium · confidence medium · introduced in 16 · fires at first_use

PostgreSQL 16 tightens GENERATED expression restrictions on inherited and partitioned tables, so parent/child or partitioned/partition column sets whose generation status differs are no longer accepted.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The change is introduced in release 16, so the upgrade crosses release 16. (confidence high, judge supported)
  - pg_release_notes@16: "Version 16 contains a number of changes that may affect compatibility with previous releases."
- **[required] database** `not_equals` `"same generation status"`: The application or database has inherited or partitioned tables in which parent/partitioned and child/partition columns differ in generation status. (confidence medium, judge supported)
  - pg_release_notes@16: "Columns of parent/partitioned and child/partition tables must all have the same generation status"
  - ⚠ The text does not state whether the failure occurs at CREATE TABLE, ALTER TABLE, dump/restore, or pg_upgrade time.
- **[disqualifying] behavior** `equals` `"same generation status"`: Generation expressions may differ between parent and child columns as long as generation status is the same. (confidence high, judge supported)
  - pg_release_notes@16: "though now the actual generation expressions can be different"

Actions:
- Search the schema for inherited or partitioned tables that mix generated and non-generated columns between parent and child.
- Make generation status consistent across each parent/child or partitioned/partition hierarchy before upgrading to 16.

### Regex \D and \W shorthands in newline-sensitive mode

`postgresql_b9a4dfaa79` · medium · confidence high · introduced in 14 · fires at first_use

In regular expression newline-sensitive mode, the \D and \W shorthands now match newlines. Previously they did not match newlines in this mode. The text says [^[:digit:]] or [^[:word:]] can be used to get the old behavior.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Upgrade crosses release 14 from a source version below 14 (confidence high)
  - pg_release_notes@14: "Allow \D and \W shorthands to match newlines in regular expression newline-sensitive mode"
- **[required] api_usage** `present` `"\\D or \\W"`: Application uses the \D or \W regex shorthand (confidence high, judge supported)
  - pg_release_notes@14: "Allow \D and \W shorthands to match newlines"
- **[uncertain] configuration** `present` `"newline-sensitive mode"`: Regular expression runs in newline-sensitive mode (confidence low, judge partially_supported)
  - pg_release_notes@14: "regular expression newline-sensitive mode"
  - ⚠ The text does not state how newline-sensitive mode is enabled or which regex operations use it.
- **[disqualifying] api_usage** `absent` `"[^[:digit:]] or [^[:word:]] in place of \\D or \\W"`: Application does not already use the replacement classes instead of \D or \W (confidence high, judge supported)
  - pg_release_notes@14: "[^[:digit:]] or [^[:word:]] can be used to get the old behavior"

Actions:
- Search regex patterns for \D and \W used in newline-sensitive mode.
- Where the old behavior is needed, replace \D with [^[:digit:]] and \W with [^[:word:]].
- Test regex matching on input containing newlines after upgrading.

### plpgsql_bound_cursor_portal_name

`postgresql_b9ad526348` · medium · confidence medium · introduced in 16 · fires at first_use

In PostgreSQL 16, the string value of PL/pgSQL bound cursor variables is assigned during OPEN and no longer matches the variable name. Code that relies on the previous name-matching behavior may break. A workaround is to assign the desired portal name to the cursor variable before OPEN.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses into release 16, so the source release is before 16. (confidence medium, judge partially_supported)
  - pg_release_notes@16: "Version 16 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"PL/pgSQL bound cursor variable"`: The application uses PL/pgSQL bound cursor variables. (confidence high, judge supported)
  - pg_release_notes@16: "Change assignment rules for PL/pgSQL bound cursor variables"
- **[required] behavior** `present` `"cursor variable string value relied upon"`: The application code depends on the string value of the bound cursor variable matching the variable name. (confidence medium, judge supported)
  - pg_release_notes@16: "Previously, the string value of such variables was set to match the variable name during cursor assignment"
  - ⚠ The text does not describe how application code would use the cursor string value.
- **[disqualifying] behavior** `present` `"portal name assigned to cursor variable before OPEN"`: The application does not already assign the desired portal name to the cursor variable before OPEN. (confidence high, judge supported)
  - pg_release_notes@16: "To restore the previous behavior, assign the desired portal name to the cursor variable before OPEN."

Actions:
- Review PL/pgSQL code that uses bound cursor variables and check whether it depends on the cursor variable's string value.
- Before OPEN, assign the desired portal name to the cursor variable to restore the previous behavior.

### Single-quoted language name in CREATE/DROP LANGUAGE

`postgresql_bc249e57a2` · medium · confidence medium · introduced in 14 · fires at first_use

Scripts or migrations that single-quote the language name in CREATE LANGUAGE or DROP LANGUAGE statements are no longer accepted in version 14 and later.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the single-quoting of the language name in CREATE/DROP LANGUAGE is disallowed. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow single-quoting of the language name in the CREATE/DROP LANGUAGE command"
- **[required] api_usage** `present` `"single-quoted language name in CREATE LANGUAGE or DROP LANGUAGE"`: The application or deployment scripts use CREATE LANGUAGE or DROP LANGUAGE with a single-quoted language name. (confidence medium, judge supported)
  - pg_release_notes@14: "single-quoting of the language name in the CREATE/DROP LANGUAGE command"
  - ⚠ The text does not give an example of the single-quoted syntax or the error produced when it is used.

Actions:
- Search SQL scripts, migrations and deployment code for CREATE LANGUAGE or DROP LANGUAGE statements that single-quote the language name.
- Remove the single quotes around the language name in those CREATE LANGUAGE and DROP LANGUAGE statements before upgrading.

### public schema CREATE permission removed by default in new databases

`postgresql_bc7ea5414c` · medium · confidence medium · introduced in 15 · fires at first_use

The default for PUBLIC creation permission on the public schema is removed. This applies to new database clusters and to newly-created databases in existing clusters, so applications that create objects in the public schema as a non-owner role may fail in those databases. Upgrading a cluster or restoring a database dump preserves existing permissions.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the removal of PUBLIC creation permission on the public schema. (confidence high, judge supported)
  - pg_release_notes@15: "Remove PUBLIC creation permission on the public schema (Noah Misch)"
- **[required] database** `present` `"newly-created database"`: The database is newly created after the upgrade in a cluster, so the new default applies to it. (confidence medium, judge supported)
  - pg_release_notes@15: "The change applies to new database clusters and to newly-created databases in existing clusters."
  - ⚠ The text does not state whether databases existing before the upgrade are affected at upgrade time; it says upgrading preserves existing permissions.
- **[required] behavior** `present` `"CREATE on public schema"`: The application relies on non-owner roles having CREATE permission on the public schema. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "granting CREATE permission will yield the behavior of prior releases"
  - ⚠ The text does not state how the application uses the public schema; whether it depends on this permission must be checked in the codebase.

Actions:
- For existing databases, especially those having multiple users, revoke CREATE permission on the public schema to adopt the new default.
- For new databases with no need to defend against insider threats, grant CREATE permission on the public schema to keep the behavior of prior releases.

### custom_scan_provider_projection_support

`postgresql_c3d0f02569` · medium · confidence medium · introduced in 15 · fires at upgrade

The default for custom scan providers changed so they are assumed not to support projections. Custom scan providers that do support projections need to be updated for release 15.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the custom scan provider projection default changed. (confidence high, judge supported)
  - pg_release_notes@15: "The default is now that custom scan providers are assumed to not support projections; those that do will need to be updated for this release."
- **[required] api_usage** `present` `"custom scan provider"`: The application uses custom scan providers. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Allow custom scan providers to indicate if they support projections"
- **[uncertain] behavior** `present` `"projection support"`: A custom scan provider in use supports projections. (confidence low, judge not_supported)
  - pg_release_notes@15: "those that do will need to be updated for this release"
  - ⚠ The text does not state how a custom scan provider indicates projection support, so the check for this condition is not specified.
  - ⚠ Judge: evidence does not support this claim. The quote says only that providers that do support projections need updating; it does not state that any custom scan provider in use supports projections.

Actions:
- Identify custom scan providers in the codebase or installed extensions.
- Update custom scan providers that support projections so they indicate this for release 15 and later.

### Upgrade from 13 to 16 requires a dump/restore, pg_upgrade or logical replication to migrate data

`postgresql_c9d93d5231` · medium · confidence medium · introduced in 15 · fires at upgrade

The release notes state that a dump/restore using pg_dumpall, use of pg_upgrade, or logical replication is required to migrate data from any previous release. Upgrading from 13 to 16 therefore needs one of these migration methods.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which contains compatibility-affecting changes. (confidence medium, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
  - pg_release_notes@14: "A dump/restore using pg_dumpall or use of pg_upgrade or logical replication is required for those wishing to migrate data from any previous release."
  - ⚠ History: in 14, 'PostgreSQL 14 data migration requirement for upgrade from earlier releases' applied to the same symbol (pg_dumpall); superseded by the 15 change (R2).
- **[required] deployment** `present` `"pg_dumpall or pg_upgrade or logical replication"`: The deployment migrates existing data from the previous release using pg_dumpall, pg_upgrade or logical replication. (confidence medium, judge supported)
  - pg_release_notes@15: "A dump/restore using pg_dumpall or use of pg_upgrade or logical replication is required for those wishing to migrate data from any previous release."
  - ⚠ The text does not state which of these methods is used for the upgrade, so the migration method must be determined per deployment.

Actions:
- Choose a migration method (dump/restore with pg_dumpall, pg_upgrade, or logical replication) for migrating data from release 13 to 16.
- Review the release 15 incompatibilities listed in the release notes before performing the migration.

### Removed server variables lc_collate and lc_ctype

`postgresql_cc8d8091c1` · medium · confidence medium · introduced in 16 · fires at upgrade

Server variables lc_collate and lc_ctype were removed in release 16. Applications or scripts that read or depend on these server variables will no longer find them.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses PostgreSQL release 16, in which the server variables lc_collate and lc_ctype are removed. (confidence high, judge supported)
  - pg_release_notes@16: "Remove read-only server variables lc_collate and lc_ctype"
  - pg_release_notes@16: "Version 16 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"lc_collate"`: The application or deployment references the server variable lc_collate or lc_ctype (for example by reading it with SHOW or querying it). (confidence medium, judge supported)
  - pg_release_notes@16: "Remove read-only server variables lc_collate and lc_ctype"
  - ⚠ The text does not state how the application would read these variables, so the search patterns are a starting point.

Actions:
- Search application code, scripts, and monitoring for references to lc_collate and lc_ctype and remove or change them before upgrading to release 16.
- The text states that collations and locales can vary between databases; determine the collation and locale settings per database. The text does not name a specific replacement method.

### Role membership inheritance default changed by GRANT

`postgresql_f01d943d69` · medium · confidence medium · introduced in 16 · fires at first_use

The default inheritance status of member roles added during GRANT is now controlled at GRANT time rather than by the role's inheritance status. Applications or deployments that grant role membership and rely on the previous inheritance behavior may see different privilege results.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses into release 16, where the role inheritance default for GRANT membership changed. (confidence medium, judge partially_supported)
  - pg_release_notes@16: "Version 16 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"GRANT"`: The application or deployment adds member roles using GRANT. (confidence high, judge supported)
  - pg_release_notes@16: "members' inheritance status is set at GRANT time"
- **[uncertain] behavior** `unknown` `"member roles rely on role-level inheritance default"`: The application or deployment depends on member roles inheriting privileges according to the role's own inheritance status. (confidence low, judge partially_supported)
  - pg_release_notes@16: "Previously the inheritance status of member roles was controlled only by the role's inheritance status"
  - ⚠ The text does not state whether applications or deployments depend on the previous inheritance behavior.
- **[uncertain] api_usage** `present` `"WITH INHERIT"`: Every GRANT of role membership explicitly sets the inheritance status using the WITH INHERIT clause. (confidence low, judge not_supported)
  - pg_release_notes@16: "The role's default inheritance behavior can be overridden with the new"
  - ⚠ The text does not state that the explicit clause removes all effect of the default change for every existing grant.
  - ⚠ Judge: evidence does not support this claim. The quote says the default can be overridden with a new clause, which implies the clause is optional rather than required on every GRANT; nothing states that every GRANT explicitly sets WITH INHERIT.

Actions:
- Identify GRANT statements that add role memberships and review whether they depend on the previous inheritance behavior.
- Where inheritance must be controlled per membership, specify the GRANT ... WITH INHERIT clause explicitly.

### vacuum_cleanup_index_scale_factor server parameter removed

`postgresql_01f92d8bc8` · low · confidence medium · introduced in 14 · fires at upgrade

The server parameter vacuum_cleanup_index_scale_factor is removed in release 14. Deployments that set this parameter in server configuration are affected. The text states the setting was already ignored from PostgreSQL 13.3 onward but does not state what happens when the parameter is still present in configuration after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which removes the parameter. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] configuration** `present` `"vacuum_cleanup_index_scale_factor"`: The server configuration sets vacuum_cleanup_index_scale_factor. (confidence high, judge supported)
  - pg_release_notes@14: "Remove server parameter vacuum_cleanup_index_scale_factor"
- **[uncertain] behavior** `unknown` `""`: Behavior of a removed parameter that is still present in configuration is not stated. (confidence low, judge not_supported)
  - pg_release_notes@14: "This setting was ignored starting in PostgreSQL version 13.3."
  - ⚠ The text does not state whether PostgreSQL 16 rejects or silently ignores a configuration entry for the removed parameter.
  - ⚠ Judge: evidence does not support this claim. The claim says the behavior is not stated, but the quote states that the setting was ignored starting in PostgreSQL 13.3, which contradicts it.

Actions:
- Remove vacuum_cleanup_index_scale_factor from postgresql.conf, ALTER SYSTEM settings, and any startup options before upgrading to release 16.
- Verify with pg_settings after the upgrade that no configuration entry for vacuum_cleanup_index_scale_factor remains.

### Zero-length Unicode identifiers (U&"") in SQL

`postgresql_076d7c8e08` · low · confidence medium · introduced in 15 · fires at first_use

Zero-length Unicode identifiers such as U&"" are disallowed in release 15 and later. Application SQL, scripts or migrations that use them may fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the disallowing of zero-length Unicode identifiers. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Disallow zero-length Unicode identifiers, e.g., U&"""
- **[required] api_usage** `present` `"U&\"\""`: The application uses zero-length Unicode identifiers such as U&"" in SQL. (confidence medium, judge supported)
  - pg_release_notes@15: "Disallow zero-length Unicode identifiers, e.g., U&"""
  - ⚠ The text does not state the error produced when such an identifier is used.

Actions:
- Search SQL, scripts and migrations for zero-length Unicode identifiers and replace them with non-empty identifiers before upgrading to version 16.

### factorial() with negative input

`postgresql_0e147761ab` · low · confidence medium · introduced in 14 · fires at first_use

factorial() no longer accepts negative numbers in release 14 and later; previously such cases returned 1.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where factorial() of negative numbers was disallowed. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Disallow factorial() of negative numbers"
- **[required] api_usage** `present` `"factorial()"`: The application calls factorial() with negative numbers. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow factorial() of negative numbers"

Actions:
- Find application code and SQL that calls factorial() and check whether any call can receive a negative argument.
- Handle negative inputs to factorial() in application code before upgrading to 16.

### has_column_privilege attribute-number checks on non-existent or dropped columns

`postgresql_167726bd25` · low · confidence low · introduced in 14 · fires at upgrade

has_column_privilege() called with attribute numbers now returns false for non-existent or dropped columns instead of raising an invalid-column error. Application code that depends on that error will see different results.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where this change was introduced. (confidence high, judge supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"has_column_privilege()"`: The application calls has_column_privilege() with attribute numbers. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "when using attribute numbers"
- **[required] behavior** `present` `"invalid-column error"`: The application relies on has_column_privilege() raising an error for non-existent or dropped columns when given attribute numbers. (confidence low, judge partially_supported)
  - pg_release_notes@14: "Previously such attribute numbers returned an invalid-column error."
  - ⚠ The text states the previous behavior but does not state whether any application code depends on it.

Actions:
- Search the codebase and SQL functions for has_column_privilege() calls that pass attribute numbers.
- Review any such call that expects an error for non-existent or dropped columns and change it to handle a false result.
- Test privilege-check code paths against the upgraded server.

### Removed server variable vacuum_defer_cleanup_age

`postgresql_1f2cea1199` · low · confidence medium · introduced in 16 · fires at upgrade

The server variable vacuum_defer_cleanup_age was removed in release 16. The text states it has been unnecessary since hot_standby_feedback and replication slots were added. The text does not state what happens when a deployment still sets this variable.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade crosses release 16, which removed the server variable vacuum_defer_cleanup_age. (confidence high, judge supported)
  - pg_release_notes@16: "Remove the server variable vacuum_defer_cleanup_age"
- **[required] configuration** `present` `"vacuum_defer_cleanup_age"`: The deployment sets the server variable vacuum_defer_cleanup_age in its configuration. (confidence medium, judge supported)
  - pg_release_notes@16: "Remove the server variable vacuum_defer_cleanup_age"
  - ⚠ The text does not state the effect on server startup or operation when a removed variable is still configured.

Actions:
- Search server configuration files and settings for vacuum_defer_cleanup_age and remove it before upgrading.
- Rely on hot_standby_feedback and replication slots, which the text states made this variable unnecessary.

### CREATE OR REPLACE VIEW output column collation

`postgresql_24f3172f15` · low · confidence medium · introduced in 15 · fires at first_use

CREATE OR REPLACE VIEW no longer changes the collation of an output column of an existing view, so code that replaces a view to change that collation will behave differently after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the change was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "Prevent CREATE OR REPLACE VIEW from changing the collation of an output column"
- **[required] api_usage** `present` `"CREATE OR REPLACE VIEW"`: The application or deployment uses CREATE OR REPLACE VIEW to change the collation of an output column of a view. (confidence medium, judge supported)
  - pg_release_notes@15: "CREATE OR REPLACE VIEW from changing the collation of an output column"
  - ⚠ The text does not describe the error or exact server behavior when the collation change is prevented.

Actions:
- Search migration and deployment scripts for CREATE OR REPLACE VIEW statements that change the collation of a view output column, and test those statements on PostgreSQL 16 before upgrading.

### Custom options matching installed extension names

`postgresql_3346e4d810` · low · confidence medium · introduced in 15 · fires at first_use

Setting custom options whose names match an installed extension but are not declared variables of that extension is disallowed starting in release 15. Pre-existing variables of this kind are deleted during extension load, and new ones cannot be created later in the session.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The change applies to PostgreSQL releases from 15 onward, so the upgrade from 13 to 16 crosses this change. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Disallow setting custom options that match the name of an installed extension"
- **[required] configuration** `present` `"custom option matching an installed extension name that is not a declared extension variable"`: The deployment has custom options set whose names match the name of an installed extension and are not declared variables of that extension. (confidence medium, judge supported)
  - pg_release_notes@15: "Disallow setting custom options that match the name of an installed extension, but are not one of the extension's declared variables"
  - ⚠ The text does not state where these custom options are set, so the scope of configuration checked is not specified.

Actions:
- Check configuration for custom options whose names match installed extensions and are not declared variables of those extensions.
- Verify that any variables set for an extension are declared by that extension, since undeclared ones are deleted during extension load.

### postmaster binary symbolic link removal

`postgresql_39a2bc1f2e` · low · confidence high · introduced in 16 · fires at upgrade

Symbolic links for the postmaster binary are removed in release 16. The text does not state which link paths were removed or what breaks when they are missing, so any impact on scripts or deployments is unconfirmed.

- **[required] version** `in_range` `{"current_version": "< 16", "target_version": ">= 16"}`: The upgrade from PostgreSQL 13 crosses into release 16. (confidence high, judge supported)
  - pg_release_notes@16: "Remove symbolic links for the postmaster binary"
- **[uncertain] runtime** `present` `"postmaster symbolic link"`: The deployment invokes the postmaster binary through a symbolic link that this release removes. (confidence low, judge partially_supported)
  - pg_release_notes@16: "Remove symbolic links for the postmaster binary"
  - ⚠ The text does not name the symbolic link paths that were removed or which invocations depended on them.

Actions:
- Search scripts, service files and deployment tooling for references to postmaster and check whether any rely on a symbolic link.
- Point any affected references at the postmaster binary path that remains after the upgrade.

### Interval justification functions now detect integer overflow

`postgresql_6642146d25` · low · confidence high · introduced in 15 · fires at first_use

In release 15, interval justification functions began detecting integer overflow. Applications that call justify_interval(), justify_hours(), or justify_days() may see different behavior when inputs overflow.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the overflow detection change was introduced. (confidence high, judge supported)
  - pg_release_notes@15: "Detect integer overflow in interval justification functions"
- **[required] api_usage** `present` `"justify_interval|justify_hours|justify_days"`: The application calls justify_interval(), justify_hours(), or justify_days(). (confidence high, judge supported)
  - pg_release_notes@15: "The affected functions are justify_interval(), justify_hours(), and justify_days()."
- **[uncertain] behavior** `present` `"integer overflow in justification input"`: The call receives interval inputs that overflow the function's integer range. (confidence low, judge supported)
  - pg_release_notes@15: "Detect integer overflow in interval justification functions"
  - ⚠ The text does not state what happens when overflow is detected, such as an error or a different result, nor what the function returned before this change.

Actions:
- Search the codebase for calls to justify_interval, justify_hours, or justify_days.
- Test those calls on PostgreSQL 16 with large interval values to confirm the resulting behavior.
- Add error handling where application logic depends on these functions with extreme interval inputs.

### random() output changes for a given seed

`postgresql_755a05d0ae` · low · confidence high · introduced in 15 · fires at upgrade

The algorithm used by random() was changed, so its results can differ from prior versions even for the same seed value. Code or tests that depend on exact random() output for a given seed may produce different results after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the change to random(). (confidence high, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
  - pg_release_notes@15: "Improve the algorithm used to compute random()"
- **[required] api_usage** `present` `"random()"`: The application calls random(). (confidence high, judge supported)
  - pg_release_notes@15: "Improve the algorithm used to compute random()"
- **[uncertain] behavior** `present` `"seeded random() output"`: The application depends on random() results being reproducible for a given seed. (confidence low, judge supported)
  - pg_release_notes@15: "even for the same seed value"
  - ⚠ The text does not state how a seed is set for random() or which operations are affected by differing results.

Actions:
- Search the codebase and SQL for random() and setseed usage.
- Review tests and logic that assume exact random() output for a given seed and update expected values if needed.

### Trailing junk after JSON numeric literals now rejected

`postgresql_90c31fa6ac` · low · confidence medium · introduced in 15 · fires at first_use

Numeric literal processing was changed to match the SQL/JSON standard. Literals with trailing junk such as 1.type() are no longer accepted, so application SQL or SQL/JSON expressions that rely on them may fail after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which introduced the numeric literal change. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases"
- **[required] api_usage** `present` `"1.type()"`: The application uses numeric literals followed directly by trailing text, such as 1.type(), in SQL or SQL/JSON expressions. (confidence medium, judge supported)
  - pg_release_notes@15: "disallows trailing junk after numeric literals, like 1.type()"
  - ⚠ The text does not state which SQL or SQL/JSON contexts are affected.

Actions:
- Search application SQL and SQL/JSON expressions for numeric literals followed by trailing identifiers and test them against PostgreSQL 16.

### Clients using wire protocol version 2 after upgrade

`postgresql_99cd4201b9` · low · confidence high · introduced in 14 · fires at upgrade

Server and libpq support for the version 2 wire protocol was removed in release 14, so clients that still negotiate protocol version 2 may fail to connect after crossing release 14.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 to 16 crosses release 14, which removed server and libpq support for the version 2 wire protocol. (confidence high, judge supported)
  - pg_release_notes@14: "Remove server and libpq support for the version 2 wire protocol"
- **[uncertain] dependency** `equals` `"version 2 wire protocol"`: The application or client connects to the server using the version 2 wire protocol. (confidence low, judge not_supported)
  - pg_release_notes@14: "This was last used as the default in PostgreSQL 7.3 (released in 2002)."
  - ⚠ The text does not state the exact error clients will see or which client library versions use protocol version 2.
  - ⚠ Judge: evidence does not support this claim. The quote only says the version 2 protocol was last the default in PostgreSQL 7.3; it does not state that any application or client currently connects using it, nor that such connections exist in the deployment.

Actions:
- Verify that all client libraries and drivers connecting to the server support the version 2 wire protocol removal, and upgrade any very old libpq-based clients before crossing release 14.

### postfix_operator_removal

`postgresql_a5a16adb33` · low · confidence medium · introduced in 14 · fires at upgrade

Support for postfix (right-unary) operators was removed in release 14. pg_dump and pg_upgrade warn when postfix operators are being dumped.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14 (source version is before 14, target is 16). (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"postfix operators"`: The database has user-defined postfix (right-unary) operators that would be dumped. (confidence medium, judge supported)
  - pg_release_notes@14: "pg_dump and pg_upgrade will warn if postfix operators are being dumped."
  - ⚠ The text does not state whether a warning means the upgrade fails or that dependent objects stop working.

Actions:
- Run pg_dump or pg_upgrade check and review any warnings about postfix operators before upgrading.
- Identify postfix operators in the database and plan how to handle them, since the text names no replacement.

### operator_precedence_warning server parameter removed in 16

`postgresql_a7d566002e` · low · confidence high · introduced in 14 · fires at upgrade

The server parameter operator_precedence_warning was removed in release 14. The text states it was used for warning applications about PostgreSQL 9.5 changes. The text does not state what happens if a configuration still sets it.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, which removed the server parameter operator_precedence_warning. (confidence high, judge supported)
  - pg_release_notes@14: "Remove server parameter operator_precedence_warning"
- **[uncertain] configuration** `present` `"operator_precedence_warning"`: The server configuration sets the parameter operator_precedence_warning. (confidence low, judge not_supported)
  - pg_release_notes@14: "This setting was used for warning applications about PostgreSQL 9.5 changes."
  - ⚠ The text does not state whether setting a removed parameter causes a startup error or is ignored.
  - ⚠ Judge: evidence does not support this claim. The quote only describes what the removed setting was used for; it does not state that the server configuration sets operator_precedence_warning. The claim is a deployment-specific hypothesis, and the evidence does not establish that deployments setting this parameter are affected beyond the parameter being a removed setting.

Actions:
- Search server configuration files and deployment manifests for operator_precedence_warning and remove it before upgrading to 16.

### intarray containment operators no longer use GiST indexes

`postgresql_c26657934e` · low · confidence medium · introduced in 14 · fires at first_use

Queries using the intarray containment operators <@ and @> no longer use GiST indexes. The text says indexes created for this purpose should be removed.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where the intarray containment operator change was introduced. (confidence high, judge supported)
  - pg_release_notes@14: "Prevent the containment operators (<@ and @>) for intarray from using GiST indexes"
- **[required] api_usage** `present` `"<@ or @>"`: The application uses the intarray containment operators <@ or @>. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Prevent the containment operators (<@ and @>) for intarray from using GiST indexes"
- **[required] database** `present` `"GiST index"`: The database has GiST indexes that were created for intarray containment queries. (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Indexes created for this purpose should be removed."
  - ⚠ The text does not state the exact index definitions or columns to check.

Actions:
- Remove indexes created for the intarray containment operators <@ and @>, as the item states they should be removed.
- Verify queries using <@ or @> on intarray columns perform as expected after upgrade, since they now scan the heap instead of using GiST indexes.

### hash_mem_multiplier default change to 2.0

`postgresql_c49690050a` · low · confidence medium · introduced in 15 · fires at first_use

The default of hash_mem_multiplier changes to 2.0, which allows query hash operations to use more work_mem memory than other operations. Deployments relying on the default may see higher memory use by hash operations.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, the release that introduced the hash_mem_multiplier default change. (confidence high, judge supported)
  - pg_release_notes@15: "Increase hash_mem_multiplier default to 2.0"
- **[required] configuration** `absent` `"hash_mem_multiplier"`: The deployment does not explicitly set hash_mem_multiplier, so the new default of 2.0 applies. (confidence medium, judge supported)
  - pg_release_notes@15: "Increase hash_mem_multiplier default to 2.0"
  - ⚠ The text does not state the previous default value of hash_mem_multiplier.
- **[optional] behavior** `present` `"hash operations using more work_mem memory"`: Query hash operations are permitted to use more work_mem memory than other operations. (confidence high, judge supported)
  - pg_release_notes@15: "This allows query hash operations to use more work_mem memory than other operations."

Actions:
- Review memory limits and work_mem usage for workloads that run hash joins or hash aggregations after the upgrade.
- If prior memory behavior is required, set hash_mem_multiplier explicitly; the text does not state the previous default value.

### Regex back-references ignore anchor and other constraints

`postgresql_c62dd64ad1` · low · confidence medium · introduced in 14 · fires at upgrade

Regular expressions that use back-references may match differently in version 14 and later because constraints are no longer applied when matching a back-reference.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade from 13 crosses release 14, where this change was introduced. (confidence high, judge supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"\\1"`: The application uses a regular expression that contains a back-reference combined with a constraint such as ^. (confidence medium, judge supported)
  - pg_release_notes@14: "For example, in (^\d+).*\1, the ^ constraint should be applied at the start of the string, but not when matching \1."
  - ⚠ The text gives one example pattern and does not list the built-in functions or operators affected.

Actions:
- Search SQL and application code for regular expressions containing back-references such as \1 and review whether any use a constraint like ^ that must apply to the whole match.
- Test those regular expressions on version 16 and compare results with version 13 before upgrading.

### public schema owner changes to pg_database_owner in newly created databases

`postgresql_cfb6c3d3ce` · low · confidence medium · introduced in 15 · fires at first_use

The default owner of the public schema changes to the pg_database_owner role. This applies to new database clusters and to newly-created databases in existing clusters, so database owners gain ownership privileges on public in those databases. Upgraded clusters keep the existing public ownership.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The public schema owner default changed to pg_database_owner in release 15. (confidence high, judge supported)
  - pg_release_notes@15: "Change the owner of the public schema to be the new pg_database_owner role (Noah Misch)"
- **[required] database** `equals` `"newly-created database"`: The application or deployment creates new databases and depends on the public schema owner being the bootstrap superuser. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "This change applies to new database clusters and to newly-created databases in existing clusters."
  - ⚠ The text does not state what specific application behavior breaks; it only says non-superuser database owners previously could not do anything with the public schema.
- **[disqualifying] database** `equals` `"existing ownership preserved"`: The database was preserved from an existing cluster upgrade or dump restore, so existing public ownership is kept. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Upgrading a cluster or restoring a database dump will preserve public's existing ownership specification."

Actions:
- For newly-created databases, check whether applications depend on the public schema being owned by the bootstrap superuser.
- Review and adjust privileges on the public schema in new databases if database owners need different access.

### Home directory lookup via HOME on non-Windows platforms

`postgresql_d48cf30f17` · low · confidence medium · introduced in 15 · fires at first_use

On non-Windows platforms, libpq and client programs now consult the HOME environment variable to find the user's home directory, which affects lookups such as ~/.pgpass. If HOME is empty or unset, the previous passwd-based method is used.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where this change was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
- **[required] runtime** `equals` `"non-Windows"`: The client or application runs on a non-Windows platform. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "On non-Windows platforms, consult the HOME environment variable to find the user's home directory"
- **[required] configuration** `present` `"~/.pgpass"`: The application or client relies on the home directory lookup, such as through ~/.pgpass. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "This change affects libpq (for example, while looking up ~/.pgpass) as well as various client application programs."
- **[uncertain] runtime** `present` `"HOME"`: The HOME environment variable is set to a value that differs from the home directory recorded in the passwd database. (confidence low, judge not_supported)
  - pg_release_notes@15: "If HOME is empty or unset, fall back to the previous method of checking the <pwd.h> database."
  - ⚠ The text does not state the consequence when HOME is set to a non-empty value that differs from the passwd home directory; the change is only described as consulting HOME first.
  - ⚠ Judge: evidence does not support this claim. The quote only describes fallback behavior when HOME is empty or unset; it says nothing about HOME being set to a value that differs from the passwd database home directory.

Actions:
- Check that HOME is set to the intended home directory for processes and service accounts that use ~/.pgpass or other home-directory lookups.
- Test client connections on non-Windows platforms after the upgrade where password files are used.

### interval-fractional-input-rounding

`postgresql_d490291822` · low · confidence medium · introduced in 15 · fires at first_use

Interval input with a fractional value for a unit greater than months is now rounded to the nearest month instead of being carried into months and smaller units as before, so the same interval literal can yield a different stored or computed value after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, where the interval input rounding change was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"fractional interval input with a unit greater than months"`: The application passes interval input containing a fractional value for a unit greater than months. (confidence high, judge supported)
  - pg_release_notes@15: "When interval input provides a fractional value for a unit greater than months"
- **[required] behavior** `present` `"round to the nearest month"`: The interval input is rounded to the nearest month rather than handled as before. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "round to the nearest month"

Actions:
- Search application code, SQL and migrations for interval literals or casts with fractional values in units greater than months and review the results.
- Run the affected queries on the upgraded server and compare results with the previous release.

### var_samp_stddev_samp_single_nan_null

`postgresql_dc64bb7d33` · low · confidence medium · introduced in 14 · fires at first_use

var_samp() and stddev_samp() with numeric parameters now return NULL instead of NaN when the input is a single NaN value. Application code that expects NaN from these functions for that input will see NULL.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: Version 14 is crossed by the upgrade from 13 to 16 (confidence medium, judge partially_supported)
  - pg_release_notes@14: "Version 14 contains a number of changes that may affect compatibility with previous releases."
- **[required] api_usage** `present` `"var_samp() or stddev_samp() with numeric parameters"`: The application calls var_samp() or stddev_samp() with numeric parameters (confidence medium, judge partially_supported)
  - pg_release_notes@14: "stddev_samp() with numeric parameters"
- **[required] behavior** `equals` `"single NaN value"`: The input to the function is a single NaN value (confidence medium, judge supported)
  - pg_release_notes@14: "when the input is a single NaN value"
  - ⚠ The text does not state how the result differs for multiple inputs that include NaN.

Actions:
- Review code that checks var_samp() or stddev_samp() results for NaN and handle NULL results instead.
- Test queries that pass NaN inputs to var_samp() or stddev_samp() with numeric parameters after the upgrade.

### char_type_non_ascii_output_format

`postgresql_de18b5aa7c` · low · confidence medium · introduced in 15 · fires at first_use

The I/O output format of type "char" changed for non-ASCII characters: bytes with the high bit set are now output as a backslash and three octal digits. Applications that read or parse text output of type "char" containing such bytes may see different values.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses PostgreSQL release 15, where the type "char" I/O format change was introduced. (confidence medium, judge partially_supported)
  - pg_release_notes@15: "Change the I/O format of type "char" for non-ASCII characters (Tom Lane)"
- **[required] behavior** `present` `"type \"char\" with non-ASCII bytes in text output"`: The application uses type "char" values that include non-ASCII bytes and relies on their text output. (confidence medium, judge supported)
  - pg_release_notes@15: "Bytes with the high bit set are now output as a backslash and three octal digits"
  - ⚠ The text does not state which applications, clients or query patterns are affected.

Actions:
- Search application code and SQL for uses of type "char" and review any parsing of its text output for non-ASCII values.
- Test affected queries on PostgreSQL 16 and compare output with the previous release.

### Regex character class with \w as range start or end

`postgresql_f1a6f3c268` · low · confidence medium · introduced in 14 · fires at first_use

Regular expressions that use \w as a range start or end inside a character class are no longer allowed in PostgreSQL 14 and later. The text states this previously was allowed but produced unexpected results.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where \w as a range start or end in regex character classes is disallowed. (confidence high, judge supported)
  - pg_release_notes@14: "Disallow \w as a range start or end in regular expression character classes"
- **[required] api_usage** `present` `"\\w used as range start or end in a regex character class"`: The application uses a regular expression with \w as a range start or end inside a character class. (confidence medium, judge supported)
  - pg_release_notes@14: "Disallow \w as a range start or end in regular expression character classes"
  - ⚠ The text does not state the exact error or result produced when such a pattern is used after the upgrade.

Actions:
- Search SQL and application code for regex patterns with \w as a range endpoint inside character classes and rewrite them, for example by listing the intended characters explicitly.
- Test affected regex queries against PostgreSQL 16 before upgrading.

### Custom server parameter names with characters invalid in unquoted SQL identifiers

`postgresql_5b9c633eb1` · unknown · confidence medium · introduced in 14 · fires at upgrade

Starting in release 14, custom server parameter names must use only characters valid in unquoted SQL identifiers. The text does not state what happens to existing names that do not comply.

- **[required] version** `in_range` `{"current_version": "< 14", "target_version": ">= 14"}`: The upgrade crosses release 14, where custom server parameter names were required to use only characters valid in unquoted SQL identifiers. (confidence high, judge supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters that are valid in unquoted SQL identifiers"
- **[required] configuration** `present` `"custom server parameter name with characters outside letters, digits, underscore, dollar sign or dot"`: The deployment uses custom server parameter names that contain characters not valid in unquoted SQL identifiers. (confidence medium, judge supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters"
  - ⚠ The text does not state which exact characters are invalid; the set of valid unquoted identifier characters is not listed in the provided text.
- **[uncertain] behavior** `unknown` `"unknown"`: The text does not state the effect on existing custom parameter names that violate the restriction after upgrading to release 16. (confidence low, judge partially_supported)
  - pg_release_notes@14: "Require custom server parameter names to use only characters"
  - ⚠ The provided text names the restriction but not whether non-compliant names are rejected, warned about, or ignored.

Actions:
- Identify custom server parameter names in configuration files, ALTER ROLE or ALTER DATABASE settings, and session SET statements that contain characters outside unquoted SQL identifier rules.
- Rename any non-compliant custom parameter names to use only characters valid in unquoted SQL identifiers, then test the upgrade.

### Removed server variable stats_temp_directory

`postgresql_a1802b44d1` · unknown · confidence high · introduced in 15 · fires at upgrade

The server variable stats_temp_directory is removed in release 15. The text does not state what happens to configurations or applications that still set it.

- **[required] version** `in_range` `{"current_version": "< 15", "target_version": ">= 15"}`: The upgrade crosses release 15, which removed stats_temp_directory. (confidence high, judge supported)
  - pg_release_notes@15: "Version 15 contains a number of changes that may affect compatibility with previous releases."
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
- **[required] configuration** `present` `"stats_temp_directory"`: The server configuration or application sets the server variable stats_temp_directory. (confidence high, judge supported)
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
- **[uncertain] behavior** `unknown` `""`: Whether setting stats_temp_directory causes an error or other failure after the upgrade. (confidence low, judge partially_supported)
  - pg_release_notes@15: "Remove obsolete server variable stats_temp_directory"
  - ⚠ The text states the variable is removed but does not state the consequence of setting it.

Actions:
- Check server configuration and application settings for stats_temp_directory before upgrading to 16.
- Remove any stats_temp_directory setting from configuration files.

## Review checklist

### Low confidence or disputed

- [ ] postgresql_0690043907: pg_hba.conf clientcert values 1, 0, no-verify
- [ ] postgresql_1cdbf7dda4: pg_hba.conf clientcert verify-ca with cert authentication
- [ ] postgresql_c3d0f02569: custom_scan_provider_projection_support
- [ ] postgresql_f01d943d69: Role membership inheritance default changed by GRANT
- [ ] postgresql_01f92d8bc8: vacuum_cleanup_index_scale_factor server parameter removed
- [ ] postgresql_167726bd25: has_column_privilege attribute-number checks on non-existent or dropped columns
- [ ] postgresql_99cd4201b9: Clients using wire protocol version 2 after upgrade
- [ ] postgresql_a7d566002e: operator_precedence_warning server parameter removed in 16
- [ ] postgresql_d48cf30f17: Home directory lookup via HOME on non-Windows platforms

### Inferred conditions

- [ ] postgresql_f01d943d69: The application or deployment depends on member roles inheriting privileges according to the role's own inheritance status.
- [ ] postgresql_167726bd25: The application relies on has_column_privilege() raising an error for non-existent or dropped columns when given attribute numbers.
- [ ] postgresql_6642146d25: The call receives interval inputs that overflow the function's integer range.
- [ ] postgresql_755a05d0ae: The application depends on random() results being reproducible for a given seed.
- [ ] postgresql_d48cf30f17: The HOME environment variable is set to a value that differs from the home directory recorded in the passwd database.

### Source disagreements


### Open questions

- Extensions (PostGIS, TimescaleDB, pg_partman, etc.) must have builds for the target major; their compatibility is not in core release notes.
- Backup and HA tooling (pgBackRest, Barman, Patroni, logical replication tools) and client drivers have their own version support.
- Managed services (RDS, Cloud SQL, Azure) control the upgrade method and some defaults.
- Minor-release notes (14.x, 15.x, 16.x) were intentionally excluded; they can contain post-release behavior fixes.
- [postgresql_0690043907] Unconfirmed: pg_hba.conf sets clientcert to 1, 0, or no-verify. (The text does not state the exact pg_hba.conf line syntax; the search regex assumes key=value form.)
- [postgresql_1cdbf7dda4] Unconfirmed: pg_hba.conf sets clientcert to verify-ca while cert authentication is enabled. (The text does not state how cert authentication is enabled in pg_hba.conf.)
- [postgresql_7bfe01bbb4] Unconfirmed: Whether the database could be affected through plpython3u is not stated in the text. (The text does not state whether plpython3u is available or affected after the upgrade.)
- [postgresql_d00aff3b01] Unconfirmed: The application relies on the containment operators, which the text says have been replaced by <@ and @>. (The text does not state a direct mapping from @ to <@ or from ~ to @>, nor any behavior differences between them.)
- [postgresql_063d5aa8bb] Unconfirmed: Client applications that authenticate with md5-stored passwords are affected by SCRAM-stored passwords. (The text does not state whether clients that only support md5 authentication will fail to connect after the change.)
- [postgresql_7ac0a4c348] Unconfirmed: The subscription runs as the subscription owner. (The text does not state the setting name or whether running as the owner is the default or an opt-in choice.)
- [postgresql_b9a4dfaa79] Unconfirmed: Regular expression runs in newline-sensitive mode (The text does not state how newline-sensitive mode is enabled or which regex operations use it.)
- [postgresql_c3d0f02569] Unconfirmed: A custom scan provider in use supports projections. (The text does not state how a custom scan provider indicates projection support, so the check for this condition is not specified.)
- [postgresql_f01d943d69] Unconfirmed: The application or deployment depends on member roles inheriting privileges according to the role's own inheritance status. (The text does not state whether applications or deployments depend on the previous inheritance behavior.)
- [postgresql_f01d943d69] Unconfirmed: Every GRANT of role membership explicitly sets the inheritance status using the WITH INHERIT clause. (The text does not state that the explicit clause removes all effect of the default change for every existing grant.)
- [postgresql_01f92d8bc8] Unconfirmed: Behavior of a removed parameter that is still present in configuration is not stated. (The text does not state whether PostgreSQL 16 rejects or silently ignores a configuration entry for the removed parameter.)
- [postgresql_39a2bc1f2e] Unconfirmed: The deployment invokes the postmaster binary through a symbolic link that this release removes. (The text does not name the symbolic link paths that were removed or which invocations depended on them.)
- [postgresql_6642146d25] Unconfirmed: The call receives interval inputs that overflow the function's integer range. (The text does not state what happens when overflow is detected, such as an error or a different result, nor what the function returned before this change.)
- [postgresql_755a05d0ae] Unconfirmed: The application depends on random() results being reproducible for a given seed. (The text does not state how a seed is set for random() or which operations are affected by differing results.)
- [postgresql_99cd4201b9] Unconfirmed: The application or client connects to the server using the version 2 wire protocol. (The text does not state the exact error clients will see or which client library versions use protocol version 2.)
- [postgresql_a7d566002e] Unconfirmed: The server configuration sets the parameter operator_precedence_warning. (The text does not state whether setting a removed parameter causes a startup error or is ignored.)
- [postgresql_d48cf30f17] Unconfirmed: The HOME environment variable is set to a value that differs from the home directory recorded in the passwd database. (The text does not state the consequence when HOME is set to a non-empty value that differs from the passwd home directory; the change is only described as consulting HOME first.)
- [postgresql_5b9c633eb1] Unconfirmed: The text does not state the effect on existing custom parameter names that violate the restriction after upgrading to release 16. (The provided text names the restriction but not whether non-compliant names are rejected, warned about, or ignored.)
- [postgresql_a1802b44d1] Unconfirmed: Whether setting stats_temp_directory causes an error or other failure after the upgrade. (The text states the variable is removed but does not state the consequence of setting it.)

## Context facts (not risks)

- (14) Fix handling of infinite window function ranges (Tom Lane) Previously window frame clauses like 'inf' PRECEDING AND 'inf' FOLLOWING returned incorrect results. — _This is a bug fix in PostgreSQL 14. The text says that previously window frame clauses like 'inf' PRECEDING AND 'inf' FOLLOWING returned incorrect results, which describes the old incorrect behavior being corrected. It does not describe a removed API, changed default, or new requirement, and it states no action needed at upgrade to 16._
- (14) Remove support for SSL compression (Daniel Gustafsson, Michael Paquier) This was already disabled by default in previous PostgreSQL releases, and most modern OpenSSL and TLS versions no longer support it. — _The item states that SSL compression support was removed in release 14, but it also states that compression was already disabled by default in previous releases and that most modern OpenSSL and TLS versions no longer support it. The text names no user action, configuration setting, or API that must change at upgrade, so no application or deployment risk condition can be stated from the text alone._
- (14) Remove the composite types that were formerly created for sequences and toast tables (Tom Lane) — _The item states only that composite types formerly created for sequences and toast tables were removed (Tom Lane). It names no user-facing API, setting, or required action, and the text does not state any effect on applications or deployments, so no upgrade risk path can be supported from the text provided._
- (14) Process doubled quote marks in ecpg SQL command strings correctly (Tom Lane) Previously 'abc''def' was passed to the server as 'abc'def', and "abc""def" was passed as "abc"def", causing syntax errors. — _The item is a bug fix in ecpg. Previously doubled quote marks in SQL command strings were passed to the server incorrectly and caused syntax errors. The text describes correct processing now and states no user action or migration step is required._
- (15) Improve consistency of interval parsing with trailing periods (Tom Lane) Numbers with trailing periods were rejected on some platforms. — _The item describes a consistency fix in interval parsing. It states that numbers with trailing periods were rejected on some platforms, and it names no removed API, changed default, or required action. The text does not describe any breakage for applications at upgrade to 16, so no risk path is produced._
- (15) Avoid unnecessary casting of constants in queries sent by postgres_fdw (Dian Fay) When column types are intentionally different between local and remote databases, such casts could cause errors. — _The item describes a fix in postgres_fdw that avoids unnecessary casting of constants in queries sent to the remote server. The text says such casts could cause errors when column types are intentionally different, so the change removes a failure mode rather than introducing a new requirement. The text states no user action is required when upgrading to 16._
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
