# Django 3.2 → 4.2: upgrade risk report

> Documentation-derived risk conditions; not a migration plan.

Django 3.2 -> 4.2 crosses 3 release(s) (4.0, 4.1, 4.2). 151 risk paths: 7 critical, 47 high, 53 medium, 44 low. Main risk types: removed_api (60), changed_behavior (60), dependency_requirement (20). Critical: Python runtime older than 3.8 unsupported by Django 4.2; PostgreSQL 9.6 no longer supported; MariaDB 10.2 no longer supported; PostgreSQL 11 database no longer supported in Django 4.2; SQLite minimum version raised to 3.21.0. 126 context facts and 1 disqualified candidates are listed separately. Documentation-derived risk conditions; not a migration plan.

Overall confidence: **medium**. Validation: `{"errors": 0, "warnings": 7, "by_code": {"W4_no_search_queries": 7}}`

## Risk paths

| Level | Confidence | Type | Surface | Release | Path |
|---|---|---|---|---|---|
| critical | high | runtime_requirement | runtime | 4.2 | `django_11d22d1a94` Python runtime older than 3.8 unsupported by Django 4.2 |
| critical | medium | dependency_requirement | database | 4.0 | `django_55eaba35a3` PostgreSQL 9.6 no longer supported |
| critical | medium | dependency_requirement | database | 4.1 | `django_594eb9c388` MariaDB 10.2 no longer supported |
| critical | medium | dependency_requirement | database | 4.2 | `django_66bc7c0863` PostgreSQL 11 database no longer supported in Django 4.2 |
| critical | medium | dependency_requirement | database | 4.2 | `django_6f48543a64` SQLite minimum version raised to 3.21.0 |
| critical | medium | dependency_requirement | database | 4.2 | `django_bd48e50291` MySQL 5.7 database no longer supported |
| critical | medium | dependency_requirement | database | 4.2 | `django_da674827bd` MariaDB 10.3 database no longer supported |
| high | high | removed_api | application_code | 4.0 | `django_0509683299` Removed django.utils.translation ugettext/ungettext family |
| high | high | removed_api | application_code | 4.0 | `django_0757526eed` HttpRequest.is_ajax() removed in 4.0 |
| high | high | removed_api | application_code | 4.0 | `django_07eb37a61f` Removal of {% ifequal %} and {% ifnotequal %} template tags |
| high | low | changed_behavior | application_code | 4.0 | `django_0bf0a41371` Expression.get_group_by_cols() subclasses must accept alias=None |
| high | high | removed_api | application_code | 4.0 | `django_122b44b57e` NullBooleanField removed in 4.0 |
| high | high | removed_api | application_code | 4.0 | `django_1c0cf6becb` unescape_entities removed in Django 4.0 |
| high | high | configuration_change | configuration | 4.0 | `django_1e0a921fcb` CSRF_TRUSTED_ORIGINS values must include scheme and wildcard format |
| high | medium | dependency_requirement | database | 4.1 | `django_28bd4abe69` PostGIS 2.4 support removed |
| high | medium | removed_api | application_code | 4.1 | `django_2da27e16b5` Third-party database backend overrides date/time DatabaseOperations methods with old field_name signatures |
| high | high | removed_api | application_code | 4.0 | `django_373bc7ec5b` django.conf.urls.url() removed in 4.0 |
| high | high | removed_api | configuration | 4.1 | `django_44c2815817` MemcachedCache backend removed in 4.1 |
| high | medium | removed_api | application_code | 4.2 | `django_451f31202b` Removed django.http.multipartparser.parse_header() function |
| high | high | removed_api | application_code | 4.0 | `django_484b5127fa` HttpRequest.get_raw_uri() removed |
| high | high | removed_api | application_code | 4.0 | `django_48bd5222f5` Removed django.contrib.postgres.fields.JSONField model field |
| high | high | removed_api | application_code | 4.0 | `django_48bd5222f5_486f` django.contrib.postgres.forms.JSONField form field removed in 4.0 |
| high | medium | dependency_requirement | database | 4.0 | `django_4fb042cc41` Oracle 12.2 or 18c database no longer officially supported |
| high | high | removed_api | application_code | 4.0 | `django_4fceb7f197` get_random_string() called without length argument |
| high | high | removed_api | application_code | 4.0 | `django_529e399225` Removed django.utils.http urlquote/urlunquote helpers |
| high | high | removed_api | application_code | 4.1 | `django_52f030f24e` DatabaseOperations.insert_statement() ignore_conflicts argument replaced by on_conflict |
| high | medium | dependency_requirement | dependencies | 4.2 | `django_6b77e6a855` PROJ < 5 support removed (GeoDjango) |
| high | high | removed_api | application_code | 4.1 | `django_7a421fde8d` BaseCommand.requires_system_checks boolean value removed |
| high | medium | dependency_requirement | dependencies | 4.1 | `django_7e17fe7b65` GDAL 2.1 support removed in django.contrib.gis |
| high | medium | removed_api | application_code | 4.1 | `django_7e959d67c1` SuccessURLAllowedHostsMixin replaced by RedirectURLMixin |
| high | medium | removed_api | application_code | 4.1 | `django_86e7176033` Third-party database backend uses removed DatabaseOperations._convert_field_to_tz() |
| high | medium | dependency_requirement | dependencies | 4.2 | `django_991aa1d9db` mysqlclient minimum version raised to 1.4.3 |
| high | medium | removed_api | application_code | 4.0 | `django_9b90619b94` MiddlewareMixin.__init__ get_response now required and non-None |
| high | medium | changed_behavior | configuration | 4.0 | `django_a0a165bd4b` CSRF_TRUSTED_ORIGINS may be required for subdomain requests with dot-prefixed cookie domain |
| high | high | removed_api | application_code | 4.0 | `django_a45385a040` Raw column aliases passed to QuerySet.order_by() no longer supported |
| high | medium | data_migration | database | 4.0 | `django_adab4c1b2a` Oracle table and column naming scheme change for names longer than 30 characters |
| high | high | removed_api | application_code | 4.0 | `django_b4c063edf8` django.utils.http.is_safe_url() removed in 4.0 |
| high | medium | dependency_requirement | dependencies | 4.0 | `django_b4c794e0cf` cx_Oracle < 7.0 support removed |
| high | medium | removed_api | application_code | 4.2 | `django_b5eb5cc228` Exists expression negated parameter removed |
| high | high | removed_api | application_code | 4.0 | `django_b921454a50` isnull lookup with non-boolean right-hand side |
| high | medium | dependency_requirement | database | 4.0 | `django_b9a44e805d` PostGIS 2.3 support removed in Django 4.0 |
| high | high | removed_api | application_code | 4.0 | `django_bbcad62967` Signal providing_args argument removed |
| high | high | removed_api | configuration | 4.0 | `django_bcd84f8d7d` PASSWORD_RESET_TIMEOUT_DAYS setting removed |
| high | high | removed_api | application_code | 4.0 | `django_bda96f577c` force_text and smart_text removed from django.utils.encoding |
| high | medium | removed_api | application_code | 4.2 | `django_bddad2ae28` Expression.get_group_by_cols alias argument removed |
| high | high | removed_api | application_code | 4.0 | `django_c3e27d1cef` Removal of django.contrib.postgres.fields.jsonb.KeyTextTransform |
| high | medium | dependency_requirement | dependencies | 4.0 | `django_c8a5898132` psycopg2 minimum version raised to 2.8.4 |
| high | medium | removed_api | deployment | 4.0 | `django_d7efdc3269` django-admin.py entry point removed |
| high | high | removed_api | application_code | 4.0 | `django_dfc647ada4` Removed django.contrib.postgres.fields.jsonb.KeyTransform and KeyTextTransform |
| high | low | changed_behavior | application_code | 4.0 | `django_e78cbd4ca0` MiddlewareMixin.__init__ get_response required |
| high | high | removed_api | application_code | 4.0 | `django_f1dbbd4617` InvalidQuery exception class removed |
| high | medium | removed_api | application_code | 4.1 | `django_f48d26d0fe` DatabaseIntrospection.get_key_columns() removed |
| high | medium | removed_api | application_code | 4.2 | `django_f9cd53a9aa` RawSQL aggregations on MySQL no longer supported |
| high | high | removed_api | application_code | 4.1 | `django_ffce931536` EmailValidator whitelist argument and domain_whitelist attribute removed |
| medium | medium | changed_behavior | application_code | 4.2 | `django_00ef9fd5ad` Custom save() methods modifying fields not added to update_fields under QuerySet.update_or_create |
| medium | medium | removed_api | application_code | 4.2 | `django_11fa2712b1` Third-party database backend relies on removed DatabaseFeatures.allows_group_by_pk |
| medium | high | removed_api | application_code | 4.1 | `django_1640c056a6` Third-party database backend overrides DatabaseOperations.ignore_conflicts_suffix_sql() |
| medium | medium | dependency_requirement | dependencies | 4.2 | `django_177f98da33` redis-py minimum version raised to 3.4.0 |
| medium | medium | changed_default | application_code | 4.1 | `django_17b16d25e5` has_case_insensitive_like default changed from True to False for third-party database backends |
| medium | medium | changed_behavior | application_code | 4.0 | `django_18e8b24987` DeleteView custom delete() logic must move to form_valid() |
| medium | medium | operational_risk | deployment | 4.1 | `django_19d2656132` CSRF cookie masking mismatch during multi-instance rollout to 4.1+ |
| medium | medium | changed_behavior | application_code | 4.1 | `django_1f6435a996` Custom BaseConstraint subclasses must implement validate() |
| medium | medium | changed_default | application_code | 4.0 | `django_21dcaab3e7` SecurityMiddleware now adds Cross-Origin-Opener-Policy: same-origin by default |
| medium | medium | changed_behavior | application_code | 4.1 | `django_21e9ff39c5` Admin multi-term search over multi-valued relationships now requires all terms to match the same related row |
| medium | medium | changed_behavior | tests | 4.1 | `django_2394866b35` assertQuerysetEqual no longer applies repr() to querysets compared with strings |
| medium | high | changed_behavior | application_code | 4.0 | `django_279f3f0fb3` RadioSelect and CheckboxSelectMultiple now render in <div> tags |
| medium | medium | removed_api | application_code | 4.1 | `django_28dea81c2d` LogoutView.get_next_page() renamed to get_success_url() |
| medium | medium | changed_behavior | tests | 4.0 | `django_2f3baa8123` assertHTMLEqual boolean-less attribute comparison change |
| medium | medium | dependency_requirement | dependencies | 4.2 | `django_350fba2684` jinja2 minimum version raised to 2.11.0 |
| medium | medium | dependency_requirement | dependencies | 4.2 | `django_38a3f575e2` asgiref minimum version raised to 3.6.0 |
| medium | high | changed_behavior | application_code | 4.1 | `django_3b5ed48e22` Meta.constraints now checked during model validation |
| medium | high | changed_behavior | tests | 4.1 | `django_3efaf434da` setUpTestData() class attributes that cannot be deep-copied |
| medium | high | changed_behavior | application_code | 4.2 | `django_448b2e13b9` blocktranslate asvar output now marked safe |
| medium | medium | changed_behavior | application_code | 4.0 | `django_48b5217f75` DatabaseSchemaEditor._unique_sql() and _create_unique_sql() second argument changed from columns to fields |
| medium | high | removed_api | application_code | 4.1 | `django_48c3fd8caa` default_app_config variable removed |
| medium | medium | changed_behavior | database | 4.1 | `django_4c5ef340ee` PostgreSQL auto fields created as identity columns instead of serial |
| medium | low | changed_behavior | application_code | 4.0 | `django_51eedd8b4d` Sliced queryset unsupported operations now raise TypeError instead of AssertionError |
| medium | medium | removed_api | application_code | 4.0 | `django_6a3932e55f` ModelAdmin log_addition/log_change/log_deletion argument renamed to obj |
| medium | medium | changed_behavior | application_code | 4.1 | `django_7414aaded0` Custom sitemap index templates need updating for adjusted context variables |
| medium | medium | changed_behavior | application_code | 4.0 | `django_764dcc1de2` Custom Node.render() returning non-string values |
| medium | medium | changed_behavior | deployment | 4.2 | `django_782bade359` makemigrations --check no longer creates migration files |
| medium | medium | changed_behavior | application_code | 4.1 | `django_7a4215cfe6` output_field no longer guessed for combined expressions and database functions with mixed types |
| medium | low | changed_default | configuration | 4.0 | `django_80d51ec58c` USE_L10N default changed from False to True |
| medium | high | removed_api | configuration | 4.0 | `django_8683c043db` DEFAULT_HASHING_ALGORITHM setting removed |
| medium | medium | removed_api | application_code | 4.0 | `django_86a937a5d8` Removed Query.where_class property |
| medium | high | removed_api | application_code | 4.1 | `django_8d968fb0a8` was_modified_since size argument removed |
| medium | medium | changed_behavior | application_code | 4.2 | `django_8f4e0280c3` EmailBackend now verifies hostname and certificates for TLS/SSL connections |
| medium | medium | changed_behavior | tests | 4.1 | `django_8fee78f055` Durable nested atomic in TestCase raises RuntimeError |
| medium | medium | changed_default | configuration | 4.1 | `django_8ffa5d85a3` Cached template loader enabled by default when DEBUG is True |
| medium | medium | changed_behavior | application_code | 4.0 | `django_905d3a6384` Custom database backend overrides year_lookup_bounds_for_date_field/year_lookup_bounds_for_datetime_field without iso_year argument |
| medium | medium | changed_behavior | tests | 4.1 | `django_ab11d5f38a` Test runner non-zero exit code for unexpected successes with unittest.expectedFailure |
| medium | medium | changed_behavior | application_code | 4.1 | `django_ab55437a82` Reverse foreign key related manager on unsaved instances raises ValueError |
| medium | medium | changed_behavior | application_code | 4.2 | `django_aeb030463f` Meta.index_together deprecated in favor of Meta.indexes |
| medium | medium | removed_api | application_code | 4.0 | `django_af4dde81fe` Removed where_class argument of get_extra_restriction() |
| medium | medium | removed_api | configuration | 4.0 | `django_b236d7b436` SECURE_BROWSER_XSS_FILTER setting removed and X-XSS-Protection header no longer set |
| medium | medium | dependency_requirement | dependencies | 4.2 | `django_b86ee766cf` argon2-cffi minimum version raised to 19.2.0 |
| medium | high | removed_api | runtime | 4.0 | `django_c1af6215cc` Pre-Django 3.1 session encoding format support removed in 4.0 |
| medium | low | changed_behavior | application_code | 4.2 | `django_d556e0f842` Manually instantiated WSGIRequest requires file-like wsgi.input |
| medium | high | changed_behavior | application_code | 4.2 | `django_d8509a5a51` UserCreationForm rejects case-insensitive duplicate usernames |
| medium | low | changed_behavior | application_code | 4.0 | `django_e8dd99cb1e` set_language() no longer stores user language in request.session |
| medium | medium | dependency_requirement | dependencies | 4.2 | `django_ecd275c5ed` Pillow minimum version raised to 6.2.1 |
| medium | low | removed_api | application_code | 4.2 | `django_f332589611` OpenLayers widget map_css block removed and inline CSS dropped |
| medium | medium | dependency_requirement | dependencies | 4.2 | `django_f751ebde09` sqlparse minimum version raised to 0.3.1 |
| medium | high | changed_behavior | application_code | 4.0 | `django_fc188b2194` pytz normalize()/localize() usage with non-UTC time zones under the zoneinfo default |
| medium | medium | changed_behavior | application_code | 4.1 | `django_fe4f42e3e7` Admin inline formset:added/formset:removed events no longer jQuery events |
| medium | high | changed_behavior | application_code | 4.0 | `django_ff4e75de71` floatformat filter always localizes output regardless of USE_L10N |
| medium | high | removed_api | application_code | 4.1 | `django_ffb36c7ea4` CookieStorage pre-3.2 message format support removed |
| low | high | changed_behavior | application_code | 4.2 | `django_0190ffdbe6` GZipMiddleware gzip response output now includes random bytes |
| low | medium | changed_behavior | application_code | 4.2 | `django_07f3f1dcee` inspectdb CharField uses display_size from get_table_description() |
| low | medium | changed_behavior | application_code | 4.1 | `django_0880a6fa66` Third-party database backend minimum_database_version requires get_database_version and super() call in init_connection_state |
| low | medium | removed_api | application_code | 4.1 | `django_0dc5985384` InlineAdminFormSet.non_form_errors property replaced by method |
| low | medium | changed_behavior | application_code | 4.2 | `django_0e37c20feb` JSON-encoded string literals passed via Value() to JSONField |
| low | medium | changed_behavior | deployment | 4.0 | `django_1163fb83c9` ManifestStaticFilesStorage rewrites JavaScript source map references |
| low | medium | removed_api | application_code | 4.1 | `django_1cb09fde64` ExclusionConstraint opclasses argument deprecated in favor of OpClass() |
| low | high | changed_behavior | application_code | 4.2 | `django_205678f117` ModelAdmin.list_editable edits now run in atomic transactions |
| low | high | removed_api | application_code | 4.0 | `django_4368ec5052` Query.add_filter() signature change (filter_clause replaced by filter_lhs and filter_rhs) |
| low | high | removed_api | application_code | 4.0 | `django_48318ce619` ModelMultipleChoiceField list message removed |
| low | high | removed_api | application_code | 4.0 | `django_4db2f08fa1` Pre-3.1 SHA-1 admin password reset tokens no longer accepted |
| low | low | changed_behavior | application_code | 4.1 | `django_50a921cea2` QuerySet.iterator() with prefetch_related and no chunk_size |
| low | medium | changed_behavior | application_code | 4.1 | `django_51841a4bc3` CSRF cookie no longer masked; request.META['CSRF_COOKIE'] holds unmasked secret |
| low | medium | changed_default | application_code | 4.2 | `django_5f49526547` PBKDF2 password hasher default iteration count increased |
| low | medium | changed_behavior | application_code | 4.2 | `django_6028e954a2` modelform_factory now respects Meta.formfield_callback |
| low | medium | removed_api | application_code | 4.0 | `django_646caddec9` CsrfViewMiddleware internal CSRF cookie tracking attributes replaced |
| low | medium | changed_behavior | application_code | 4.0 | `django_6578964c0b` No-op AlterField operations generated by makemigrations for ForeignKey/ManyToManyField |
| low | low | changed_default | application_code | 4.0 | `django_65b3b830af` InlineModelAdmin.verbose_name_plural fallback change |
| low | low | changed_behavior | application_code | 4.0 | `django_68ec37b26b` Email attach/attach_alternative exception type changed from AssertionError to ValueError |
| low | medium | changed_behavior | application_code | 4.0 | `django_6b02370c63` AdminSite index view no longer wrapped in never_cache when accessed directly |
| low | low | changed_behavior | application_code | 4.2 | `django_7019792cec` Session cookies hidden in error reports |
| low | high | removed_api | application_code | 4.2 | `django_793d3b8716` Query.add_annotation() is_summary argument removed |
| low | high | changed_behavior | application_code | 4.0 | `django_7efc1311fa` RssFeed/Atom1Feed empty elements now self-closing |
| low | medium | changed_behavior | application_code | 4.2 | `django_863b5fb220` JSON-encoded string default passed to JSONBAgg |
| low | high | removed_api | tests | 4.0 | `django_8abb4cc21d` django.test.runner.reorder_suite() renamed to reorder_tests() with changed argument and return types |
| low | low | changed_behavior | application_code | 4.1 | `django_910ce87d08` CSS form media link tags no longer include type="text/css" |
| low | medium | changed_behavior | application_code | 4.1 | `django_91802d0ff8` RemoteUserBackend.configure_user subclass without created argument |
| low | medium | changed_behavior | application_code | 4.0 | `django_9b38717bcc` FileSystemStorage.delete() empty name exception type changed |
| low | high | changed_behavior | application_code | 4.2 | `django_9f3db82e18` AlterIndexTogether not to be used in new migrations |
| low | high | changed_behavior | application_code | 4.2 | `django_a03bfcb268` GeoJSON serializer output now includes id key |
| low | high | changed_behavior | tests | 4.0 | `django_a34fcce24b` Tests that fail to load now always match test --tag |
| low | medium | removed_api | application_code | 4.1 | `django_af968f5ff7` Undocumented URL resolver internals moved to django.contrib.admindocs.utils |
| low | medium | removed_api | application_code | 4.0 | `django_b75c50a6ca` Renamed admin utility lookup_needs_distinct to lookup_spawns_duplicates |
| low | medium | changed_behavior | configuration | 4.2 | `django_b7d77765c8` django-db-logger logger now logs transaction queries at DEBUG |
| low | high | removed_api | application_code | 4.0 | `django_cad51ea34e` TRANSLATOR_COMMENT_MARK moved from django.template.base |
| low | medium | changed_behavior | application_code | 4.1 | `django_cd2220a8df` mark_safe lazy object preservation |
| low | medium | removed_api | application_code | 4.1 | `django_cd78591007` PickleSerializer deprecated in 4.1 |
| low | medium | removed_api | application_code | 4.1 | `django_d1c6eb373c` log_response exc_info argument replaced by exception |
| low | medium | changed_behavior | application_code | 4.1 | `django_e15fd536b5` Admin log out UI now uses POST requests |
| low | medium | changed_behavior | application_code | 4.0 | `django_e2d9e19604` ProjectState real_apps must be a set |
| low | medium | changed_behavior | application_code | 4.1 | `django_e6d7f4a0bb` Model.full_clean converts exclude to a set; callers and overrides should pass exclude as a set |
| low | medium | changed_behavior | application_code | 4.0 | `django_f019e59923` django.utils.timezone.utc now aliases datetime.timezone.utc |
| low | medium | changed_behavior | application_code | 4.2 | `django_ff6ba9a221` OpenLayersWidget upgraded to OpenLayers 7.2.2 |
| low | medium | changed_default | application_code | 4.1 | `django_ff918e477f` ModelAdmin.actions and inlines default changed from list to tuple |

### Python runtime older than 3.8 unsupported by Django 4.2

`django_11d22d1a94` · critical · confidence high · introduced in 4.2 · fires at upgrade

Django 4.2 supports Python 3.8 through 3.12 (as of 4.2.8), and package metadata sets requires_python to >=3.8. A project running on a Python version older than 3.8 is outside the supported range, so the Python runtime must be upgraded before or together with the move to Django 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade targets Django 4.2, which defines the supported Python versions. (confidence high, judge supported)
  - dj_notes@4.2: "Django 4.2 supports Python 3.8, 3.9, 3.10, 3.11, and 3.12"
  - dj_pypi@3.2: "info.requires_python = '>=3.6'"
  - dj_pypi@4.2: "info.requires_python = '>=3.8'"
  - dj_notes@4.0: "The Django 3.2.x series is the last to support Python 3.6 and 3.7."
  - dj_notes@4.0: "Django 4.0 supports Python 3.8, 3.9, and 3.10."
  - dj_notes@4.1: "Django 4.1 supports Python 3.8, 3.9, 3.10, and 3.11 (as of 4.1.3)."
  - ⚠ History: in 4.0, 'Python 3.6/3.7 no longer supported as of Django 4.0' applied to the same symbol (python); superseded by the 4.2 change (R2).
  - ⚠ History: in 4.1, 'Python runtime version compatibility for Django 4.1+' applied to the same symbol (python); superseded by the 4.2 change (R2).
- **[required] runtime** `less_than` `"3.8"`: The application or deployment runs on a Python version older than 3.8, which is not in the supported list. (confidence high, judge supported)
  - dj_notes@4.2: "Django 4.2 supports Python 3.8, 3.9, 3.10, 3.11, and 3.12"
  - dj_pypi@4.2: "info.requires_python = '>=3.8'"
  - ⚠ The text lists supported versions but does not explicitly say what happens on Python older than 3.8; the lower bound >=3.8 comes from package metadata.
- **[uncertain] runtime** `greater_than` `"3.12"`: The application runs on a Python version newer than 3.12, which is not in the listed supported versions. (confidence low, judge partially_supported)
  - dj_notes@4.2: "Django 4.2 supports Python 3.8, 3.9, 3.10, 3.11, and 3.12"
  - ⚠ The text does not say whether Python versions newer than 3.12 work or fail with Django 4.2.

Actions:
- Verify the Python version used in development, CI and production (including Docker base images and packaging metadata such as python_requires).
- If running Python older than 3.8, upgrade to a supported version (3.8 to 3.12) before or together with upgrading Django to 4.2.
- Prefer the latest release of a supported Python series, as the text recommends and only officially supports those.
- Check the deployed Python version against '>=3.8' before upgrading.

### PostgreSQL 9.6 no longer supported

`django_55eaba35a3` · critical · confidence medium · introduced in 4.0 · fires at upgrade

Django 4.0 dropped support for PostgreSQL 9.6 and supports PostgreSQL 10 and higher. Deployments that run Django against PostgreSQL 9.6 must upgrade the database server before moving to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which dropped PostgreSQL 9.6 support. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Django 4.0 supports PostgreSQL 10 and higher."
- **[required] database** `less_than` `"10"`: The deployment uses a PostgreSQL server older than version 10 (for example 9.6) as the Django database backend. (confidence high, judge supported)
  - dj_notes@4.0: "Django 4.0 supports PostgreSQL 10 and higher."
  - dj_notes@4.0: "Upstream support for PostgreSQL 9.6 ends in November 2021."

Actions:
- Upgrade the PostgreSQL server to version 10 or higher before upgrading Django to 4.2.
- Check the PostgreSQL server version in every environment (development, CI, staging, production).

### MariaDB 10.2 no longer supported

`django_594eb9c388` · critical · confidence medium · introduced in 4.1 · fires at upgrade

Django 4.1 dropped support for MariaDB 10.2 and supports MariaDB 10.3 and higher. Deployments using MariaDB 10.2 as the database backend must move to MariaDB 10.3 or newer to upgrade from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, which supports MariaDB 10.3 and higher and drops MariaDB 10.2. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "Django 4.1 supports MariaDB 10.3 and higher."
- **[uncertain] database** `less_than` `"10.3"`: The deployment uses a MariaDB database server at version 10.2 (less than 10.3) with Django. (confidence low, judge not_supported)
  - dj_notes@4.1: "Upstream support for MariaDB 10.2 ends in May 2022."
  - ⚠ The text does not state exactly how Django behaves on an unsupported MariaDB 10.2 server (e.g. error at startup vs. unsupported/untested).
  - ⚠ Judge: evidence does not support this claim. The quote says only that upstream support for MariaDB 10.2 ends in May 2022. It does not say Django 4.1 drops MariaDB 10.2 or requires 10.3+, and it does not establish that a deployment on 10.2 is affected by the Django upgrade.

Actions:
- Check the MariaDB server version used by each environment (e.g. SELECT VERSION();).
- Upgrade MariaDB 10.2 servers to 10.3 or higher before or together with upgrading Django to 4.1+/4.2.
- Update CI, docker images and deployment manifests that pin MariaDB 10.2.

### PostgreSQL 11 database no longer supported in Django 4.2

`django_66bc7c0863` · critical · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 supports PostgreSQL 12 and higher; support for PostgreSQL 11 is dropped. Deployments using Django with a PostgreSQL 11 database must move to PostgreSQL 12 or higher when upgrading to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which supports only PostgreSQL 12 and higher. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "Django 4.2 supports PostgreSQL 12 and higher."
  - dj_notes@4.1: "Django 4.1 supports PostgreSQL 11 and higher."
  - dj_notes@4.1: "Upstream support for PostgreSQL 10 ends in November 2022."
  - ⚠ History: in 4.1, 'PostgreSQL 10 unsupported in Django 4.1+' applied to the same symbol (postgresql); superseded by the 4.2 change (R2).
- **[required] database** `less_than` `"12"`: The deployment uses a PostgreSQL database server running a version lower than 12 (e.g. PostgreSQL 11). (confidence medium, judge supported)
  - dj_notes@4.2: "Upstream support for PostgreSQL 11 ends in November 2023."
  - dj_notes@4.2: "Django 4.2 supports PostgreSQL 12 and higher."
  - ⚠ The text does not state whether Django 4.2 actively fails on PostgreSQL 11 or merely no longer officially supports it.

Actions:
- Check the PostgreSQL server version used by each environment (SHOW server_version;).
- Upgrade PostgreSQL to version 12 or higher before or together with upgrading Django to 4.2.
- Update CI, docker-compose and deployment configs that pin PostgreSQL 11.

### SQLite minimum version raised to 3.21.0

`django_6f48543a64` · critical · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported SQLite version from 3.9.0 to 3.21.0. Deployments that use SQLite older than 3.21.0 are no longer supported at 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where the minimum supported SQLite version is raised. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of SQLite is increased from 3.9.0 to 3.21.0."
- **[required] database** `present` `"django.db.backends.sqlite3"`: The deployment uses SQLite as a database backend (django.db.backends.sqlite3). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The minimum supported version of SQLite is increased from 3.9.0 to 3.21.0."
- **[required] runtime** `less_than` `"3.21.0"`: The SQLite library version in the runtime environment is older than 3.21.0. (confidence medium, judge supported)
  - dj_notes@4.2: "The minimum supported version of SQLite is increased from 3.9.0 to 3.21.0."
  - ⚠ The text does not state the exact failure mode on unsupported SQLite versions.

Actions:
- Check the SQLite library version used by Python (sqlite3.sqlite_version) in every environment (development, CI, production).
- Upgrade SQLite to 3.21.0 or newer before upgrading to Django 4.2.
- If the SQLite version cannot be upgraded, do not upgrade to Django 4.2 on that environment or use a different database backend.

### MySQL 5.7 database no longer supported

`django_bd48e50291` · critical · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 supports MySQL 8 and higher. Deployments that use MySQL 5.7 as the database backend are on an unsupported database version after upgrading to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which supports MySQL 8 and higher and drops MySQL 5.7. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "Django 4.2 supports MySQL 8 and higher."
- **[uncertain] database** `equals` `"MySQL 5.7"`: The deployment uses a MySQL database server at version 5.7. (confidence low, judge not_supported)
  - dj_notes@4.2: "Upstream support for MySQL 5.7 ends in October 2023."
  - ⚠ The text does not say whether Django 4.2 actively fails on MySQL 5.7 or merely no longer supports it.
  - ⚠ Judge: evidence does not support this claim. The quote only says upstream support for MySQL 5.7 ends in October 2023. It does not establish any impact on deployments using MySQL 5.7, nor that Django 4.2 drops support for it. It is not evidence about what version a deployment uses.

Actions:
- Upgrade the MySQL server to version 8 or higher before or together with moving to Django 4.2.
- Verify the production, staging and CI database versions are MySQL 8 or higher.

### MariaDB 10.3 database no longer supported

`django_da674827bd` · critical · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 supports MariaDB 10.4 and higher; deployments using MariaDB 10.3 as the database backend are on an unsupported database version after upgrading.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which supports MariaDB 10.4 and higher. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "Django 4.2 supports MariaDB 10.4 and higher."
- **[uncertain] database** `less_than` `"10.4"`: The deployment uses a MariaDB database server older than 10.4 (e.g. 10.3). (confidence low, judge not_supported)
  - dj_notes@4.2: "Upstream support for MariaDB 10.3 ends in May 2023."
  - ⚠ The text does not state how Django 4.2 behaves on MariaDB 10.3 (e.g. error at startup or merely unsupported).
  - ⚠ Judge: evidence does not support this claim. The quote only says upstream support for MariaDB 10.3 ends in May 2023. It does not state that Django 4.2 drops support for versions older than 10.4, nor that deployments on MariaDB older than 10.4 are affected.

Actions:
- Upgrade MariaDB servers to version 10.4 or higher before or together with upgrading Django to 4.2.
- Check the MariaDB server version used in all environments (dev, CI, staging, production).

### Removed django.utils.translation ugettext/ungettext family

`django_0509683299` · high · confidence high · introduced in 4.0 · fires at upgrade

django.utils.translation.ugettext(), ugettext_lazy(), ugettext_noop(), ungettext(), and ungettext_lazy() are removed in Django 4.0. Code importing or calling them will fail with ImportError/AttributeError after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, in which these functions are removed (3.2 -> 4.2). (confidence high, judge supported)
  - dj_notes@4.0: "These features have reached the end of their deprecation cycle and are removed in Django 4.0."
  - dj_deprecation: "django.utils.translation.ugettext(), ugettext_lazy(), ugettext_noop(), ungettext(), and ungettext_lazy() will be removed."
- **[required] api_usage** `present` `"ugettext|ugettext_lazy|ugettext_noop|ungettext|ungettext_lazy"`: The application imports or calls any of ugettext, ugettext_lazy, ugettext_noop, ungettext, or ungettext_lazy from django.utils.translation. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.translation.ugettext(), ugettext_lazy(), ugettext_noop(), ungettext(), and ungettext_lazy() are removed."
  - dj_deprecation: "django.utils.translation.ugettext(), ugettext_lazy(), ugettext_noop(), ungettext(), and ungettext_lazy() will be removed."

Actions:
- The text refers to deprecated-features-3.0 for how to remove usage; replace the removed functions with their non-u-prefixed equivalents (gettext, gettext_lazy, gettext_noop, ngettext, ngettext_lazy) where the replacement is described there.
- Search the codebase and third-party dependencies for usages of the removed functions and update them before upgrading.
- Run the test suite on Django 4.0+ to catch remaining ImportError/AttributeError.
- The text does not name replacements, so check the Django 3.0 release notes referenced in the timeline for the replacement functions.
- Search the codebase and third-party dependencies for ugettext, ugettext_lazy, ugettext_noop, ungettext and ungettext_lazy and update every usage before upgrading to 4.x.

### HttpRequest.is_ajax() removed in 4.0

`django_0757526eed` · high · confidence high · introduced in 4.0 · fires at upgrade

The HttpRequest.is_ajax() method is removed in Django 4.0 after its deprecation cycle. Code that calls request.is_ajax() will fail at runtime once upgraded past 4.0 (including 4.2).

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which HttpRequest.is_ajax() is removed. (confidence high, judge partially_supported)
  - dj_notes@4.0: "The HttpRequest.is_ajax() method is removed."
  - dj_deprecation: "The HttpRequest.is_ajax() method will be removed."
- **[required] api_usage** `present` `"is_ajax("`: The application code calls is_ajax() on an HttpRequest object (e.g. request.is_ajax()). (confidence high, judge supported)
  - dj_notes@4.0: "The HttpRequest.is_ajax() method is removed."
  - dj_deprecation: "The HttpRequest.is_ajax() method will be removed."

Actions:
- Search the codebase, templates and third-party integrations for is_ajax() calls and replace them with an alternative check before upgrading (see deprecated-features-3.1 for details on how to remove usage of this feature).
- Search the codebase and installed third-party packages for is_ajax() calls and remove or replace them before upgrading.
- Replace request.is_ajax() with an explicit check of request headers, for example the X-Requested-With header, if the same behavior is still needed.

### Removal of {% ifequal %} and {% ifnotequal %} template tags

`django_07eb37a61f` · high · confidence high · introduced in 4.0 · fires at upgrade

The {% ifequal %} and {% ifnotequal %} template tags are removed in Django 4.0. Templates that still use them will fail on the upgrade from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which the {% ifequal %} and {% ifnotequal %} template tags are removed. (confidence high, judge supported)
  - dj_notes@4.0: "The {% ifequal %} and {% ifnotequal %} template tags are removed."
  - dj_deprecation: "The {% ifequal %} and {% ifnotequal %} template tags will be removed."
- **[alternative] api_usage** `present` `"{% ifequal %}"`: Templates use the {% ifequal %} tag. (confidence high, judge supported)
  - dj_notes@4.0: "The {% ifequal %} and {% ifnotequal %} template tags are removed."
  - dj_deprecation: "The {% ifequal %} and {% ifnotequal %} template tags will be removed."
- **[alternative] api_usage** `present` `"{% ifnotequal %}"`: Templates use the {% ifnotequal %} tag. (confidence high, judge supported)
  - dj_notes@4.0: "The {% ifequal %} and {% ifnotequal %} template tags are removed."

Actions:
- Search all templates (including those in third-party apps and those loaded from the database) for {% ifequal %} and {% ifnotequal %} usage.
- Replace {% ifequal a b %} with {% if a == b %} and {% ifnotequal a b %} with {% if a != b %}, and replace the matching end tags with {% endif %}.
- See the Django 3.0 deprecation notes referenced in the release notes for details on removing usage.
- Search all templates (including third-party and admin overrides) for ifequal/ifnotequal tags.
- Replace {% ifequal a b %} and {% ifnotequal a b %} with the equivalent {% if a == b %} and {% if a != b %} before upgrading.

### Expression.get_group_by_cols() subclasses must accept alias=None

`django_0bf0a41371` · high · confidence low · introduced in 4.0 · fires at upgrade

As of 4.0, alias=None is required in the signature of django.db.models.Expression.get_group_by_cols() subclasses. Custom Expression subclasses that override get_group_by_cols() without an alias=None parameter in the signature no longer meet the required signature after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, in which alias=None becomes required in the get_group_by_cols() signature. (confidence high, judge supported)
  - dj_deprecation: "alias=None will be required in the signature of django.db.models.Expression.get_group_by_cols() subclasses."
  - dj_notes@4.0: "alias=None is required in the signature of django.db.models.Expression.get_group_by_cols() subclasses."
- **[required] api_usage** `present` `"get_group_by_cols"`: The application defines subclasses of django.db.models.Expression that override get_group_by_cols(). (confidence high, judge supported)
  - dj_deprecation: "alias=None will be required in the signature of django.db.models.Expression.get_group_by_cols() subclasses."
  - dj_notes@4.0: "alias=None is required in the signature of django.db.models.Expression.get_group_by_cols() subclasses."
  - ⚠ The text does not state the exact failure mode when alias=None is missing.
- **[required] api_usage** `absent` `"alias=None"`: The overriding get_group_by_cols() signature does not already include alias=None. (confidence low, judge supported)
  - dj_deprecation: "alias=None will be required in the signature of django.db.models.Expression.get_group_by_cols() subclasses."
  - ⚠ The text does not describe the exact failure mode (e.g. TypeError) when alias=None is missing from the signature.

Actions:
- Find all subclasses of django.db.models.Expression that override get_group_by_cols().
- Update each override's signature to include alias=None, i.e. get_group_by_cols(self, alias=None).
- Find all Expression subclasses that override get_group_by_cols().
- Update each override signature to include alias=None, e.g. def get_group_by_cols(self, alias=None).
- Run tests that exercise queries with aggregation or GROUP BY using these custom expressions.

### NullBooleanField removed in 4.0

`django_122b44b57e` · high · confidence high · introduced in 4.0 · fires at upgrade

The model NullBooleanField is removed in release 4.0. Only a stub field remains for compatibility with historical migrations, so application code or models that still define or reference NullBooleanField beyond migrations are affected when upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which the model NullBooleanField is removed. (confidence high, judge supported)
  - dj_deprecation: "The model NullBooleanField will be removed."
  - dj_notes@4.0: "The NullBooleanField model field is removed, except for support in historical migrations."
- **[required] api_usage** `present` `"NullBooleanField"`: The application uses NullBooleanField in model definitions or other code (outside historical migrations). (confidence high, judge supported)
  - dj_deprecation: "The model NullBooleanField will be removed."
  - dj_notes@4.0: "The NullBooleanField model field is removed, except for support in historical migrations."
  - ⚠ The text does not state a replacement field or the exact behavior of the stub field beyond its role for historical migrations.
- **[disqualifying] api_usage** `present` `"NullBooleanField only in migrations"`: Usage appears only in historical migrations, which are kept compatible by the stub field. (confidence medium, judge partially_supported)
  - dj_deprecation: "A stub field will remain for compatibility with historical migrations."

Actions:
- Find all uses of NullBooleanField outside historical migrations.
- Update the affected code before upgrading; the text names no replacement field.
- Leave historical migrations as they are, since a stub field remains for compatibility with them.
- The provided text does not name a replacement. See deprecated-features-3.0 for details on how to remove usage of NullBooleanField.
- Search non-migration code for NullBooleanField usage and update it before upgrading.
- Historical migrations may continue to reference NullBooleanField, as support for it there is retained.

### unescape_entities removed in Django 4.0

`django_1c0cf6becb` · high · confidence high · introduced in 4.0 · fires at upgrade

django.utils.text.unescape_entities() is removed in Django 4.0, so application code that still calls it will fail after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which unescape_entities() is removed. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.text.unescape_entities() is removed."
  - dj_deprecation: "django.utils.text.unescape_entities() will be removed."
- **[required] api_usage** `present` `"unescape_entities"`: The application code calls or imports django.utils.text.unescape_entities. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.text.unescape_entities() is removed."
  - dj_deprecation: "django.utils.text.unescape_entities() will be removed."

Actions:
- Search the codebase for unescape_entities and remove or replace usage before upgrading.
- Consult the Django 3.0 deprecation notes (deprecated-features-3.0) for how to remove usage of this function.
- Find all usages of django.utils.text.unescape_entities() and remove or replace them before upgrading to 4.x.
- The provided text does not name a replacement, so choose an alternative such as Python's standard library html.unescape only after verifying it fits your use case.

### CSRF_TRUSTED_ORIGINS values must include scheme and wildcard format

`django_1e0a921fcb` · high · confidence high · introduced in 4.0 · fires at upgrade

Starting in Django 4.0, values in CSRF_TRUSTED_ORIGINS must include the scheme (e.g. 'http://' or 'https://') rather than only the hostname, and values starting with a dot must now include an asterisk before the dot (e.g. '.example.com' becomes 'https://*.example.com'). Settings using the old hostname-only format need to be updated. A system check detects required changes.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the CSRF_TRUSTED_ORIGINS format requirement was introduced. (confidence high, judge supported)
  - dj_notes@4.0: "Values in the CSRF_TRUSTED_ORIGINS setting must include the scheme"
- **[required] configuration** `present` `"CSRF_TRUSTED_ORIGINS"`: The project defines the CSRF_TRUSTED_ORIGINS setting. (confidence high, judge supported)
  - dj_notes@4.0: "Values in the CSRF_TRUSTED_ORIGINS setting must include the scheme"
- **[alternative] configuration** `absent` `"http:// or https:// prefix on each CSRF_TRUSTED_ORIGINS value"`: CSRF_TRUSTED_ORIGINS contains entries that lack a scheme (hostname-only) such as 'example.com'. (confidence high, judge supported)
  - dj_notes@4.0: "must include the scheme (e.g. 'http://' or 'https://') instead of only the hostname"
- **[alternative] configuration** `contains` `"value starting with '.' such as '.example.com'"`: CSRF_TRUSTED_ORIGINS contains entries starting with a dot (e.g. '.example.com') without an asterisk before the dot. (confidence high, judge supported)
  - dj_notes@4.0: "values that started with a dot, must now also include an asterisk before the dot"

Actions:
- Update each CSRF_TRUSTED_ORIGINS value to include the scheme, e.g. 'https://example.com'.
- Change dot-prefixed values such as '.example.com' to 'https://*.example.com'.
- Run Django's system checks (manage.py check) to detect any required changes.

### PostGIS 2.4 support removed

`django_28bd4abe69` · high · confidence medium · introduced in 4.1 · fires at upgrade

Django 4.1 removes support for PostGIS 2.4. Deployments using django.contrib.gis with a PostGIS 2.4 database are no longer supported after the upgrade and need a newer PostGIS version.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where PostGIS 2.4 support was removed. (confidence high, judge supported)
  - dj_notes@4.1: "Support for PostGIS 2.4 is removed."
- **[required] database** `equals` `"2.4"`: The deployment uses a PostGIS 2.4 database with django.contrib.gis. (confidence medium, judge supported)
  - dj_notes@4.1: "Support for PostGIS 2.4 is removed."
  - ⚠ The text does not state whether PostGIS 2.4 fails outright or is merely unsupported.

Actions:
- Check the PostGIS version in use (SELECT PostGIS_Version();).
- Upgrade PostGIS to a version supported by Django 4.2 before upgrading Django if currently on 2.4.

### Third-party database backend overrides date/time DatabaseOperations methods with old field_name signatures

`django_2da27e16b5` · high · confidence medium · introduced in 4.1 · fires at first_use

In Django 4.1, several date and time methods on DatabaseOperations take sql and params arguments instead of field_name and return a 2-tuple of SQL and parameters. Third-party database backends (or custom code) that define or call these methods with the old signature or return a single SQL string need updating.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where these DatabaseOperations methods changed signature and return value. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "Several date and time methods on DatabaseOperations now take sql and params arguments instead of field_name"
- **[required] api_usage** `present` `"date_extract_sql|datetime_extract_sql|time_extract_sql|date_trunc_sql|datetime_trunc_sql|time_trunc_sql|datetime_cast_date_sql|datetime_cast_time_sql"`: The project contains or uses a custom or third-party database backend whose DatabaseOperations overrides or calls the changed date/time methods. (confidence medium, judge supported)
  - dj_notes@4.1: "This section describes changes that may be needed in third-party database backends."
  - dj_notes@4.1: "DatabaseOperations.date_extract_sql(lookup_type, sql, params)"
  - ⚠ The text does not state whether code outside a database backend that calls these methods directly is affected.
- **[uncertain] api_usage** `absent` `"date_extract_sql|datetime_extract_sql|time_extract_sql|date_trunc_sql|datetime_trunc_sql|time_trunc_sql|datetime_cast_date_sql|datetime_cast_time_sql"`: The project uses only Django's built-in database backends and does not override or call these methods. (confidence low, judge not_supported)
  - dj_notes@4.1: "This section describes changes that may be needed in third-party database backends."
  - ⚠ Judge: evidence does not support this claim. The quote only says the changes may be needed in third-party backends; it does not establish that projects using only built-in backends are unaffected or that they do not override or call these methods. The claim is about a project's own usage, which the quote does not address.

Actions:
- Update overridden methods to the new signatures: date_extract_sql(lookup_type, sql, params), datetime_extract_sql(lookup_type, sql, params, tzname), time_extract_sql(lookup_type, sql, params), date_trunc_sql(lookup_type, sql, params, tzname=None), datetime_trunc_sql(lookup_type, sql, params, tzname), time_trunc_sql(lookup_type, sql, params, tzname=None), datetime_cast_date_sql(sql, params, tzname), datetime_cast_time_sql(sql, params, tzname).
- Change the methods to return a 2-tuple of SQL and the parameters to be interpolated into that SQL.
- Update any callers of these methods to pass sql and params and to handle the tuple return value.
- Check that the third-party database backend in use supports Django 4.2.

### django.conf.urls.url() removed in 4.0

`django_373bc7ec5b` · high · confidence high · introduced in 4.0 · fires at upgrade

django.conf.urls.url() reached the end of its deprecation cycle and is removed in Django 4.0, so any code that imports or calls it (typically URLconf modules) will fail when running on 4.0 or later, including 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which django.conf.urls.url() is removed. (confidence high, judge partially_supported)
  - dj_notes@4.0: "django.conf.urls.url() is removed."
  - dj_deprecation: "django.conf.urls.url() will be removed."
- **[required] api_usage** `present` `"django.conf.urls.url"`: The application uses django.conf.urls.url(). (confidence high, judge supported)
  - dj_notes@4.0: "django.conf.urls.url() is removed."
  - dj_deprecation: "django.conf.urls.url() will be removed."

Actions:
- The text refers to deprecated-features-3.0 for details on removing usage of this feature; consult it for the replacement and migration steps.
- Find all usages of django.conf.urls.url() in the codebase and replace them before upgrading to 4.x.
- Replace django.conf.urls.url() usages in URLconfs with django.urls.re_path() (regex patterns) or django.urls.path() (simple patterns), keeping the same arguments where re_path() is used.

### MemcachedCache backend removed in 4.1

`django_44c2815817` · high · confidence high · introduced in 4.1 · fires at upgrade

The django.core.cache.backends.memcached.MemcachedCache backend is removed in Django 4.1. A project that still references it (for example in the CACHES setting) is affected when upgrading from 3.2 to 4.2, because the backend no longer exists.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, in which the MemcachedCache backend is removed. (confidence high, judge supported)
  - dj_notes@4.1: "These features have reached the end of their deprecation cycle and are removed in Django 4.1."
  - dj_notes@4.1: "The django.core.cache.backends.memcached.MemcachedCache backend is removed."
  - dj_deprecation: "django.core.cache.backends.memcached.MemcachedCache will be removed."
- **[required] api_usage** `present` `"django.core.cache.backends.memcached.MemcachedCache"`: The application or deployment configuration references the django.core.cache.backends.memcached.MemcachedCache backend, for example as a CACHES BACKEND value. (confidence high, judge supported)
  - dj_notes@4.1: "The django.core.cache.backends.memcached.MemcachedCache backend is removed."
  - dj_deprecation: "django.core.cache.backends.memcached.MemcachedCache will be removed."
  - ⚠ The text does not say where the backend is typically referenced, such as in the CACHES setting.

Actions:
- Search settings and configuration for references to django.core.cache.backends.memcached.MemcachedCache.
- Replace any such reference with a cache backend that still exists in Django 4.2 before upgrading. The text does not name a specific replacement; see deprecated-features-3.2 for details on how to remove usage of this feature.
- Search settings and code for references to django.core.cache.backends.memcached.MemcachedCache.
- Replace the removed backend with a supported Memcached backend before upgrading to 4.2.

### Removed django.http.multipartparser.parse_header() function

`django_451f31202b` · high · confidence medium · introduced in 4.2 · fires at upgrade

The undocumented django.http.multipartparser.parse_header() function is removed in Django 4.2. Code that imports or calls it will fail with an ImportError or AttributeError. The replacement is django.utils.http.parse_header_parameters().

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where parse_header() is removed. (confidence high, judge supported)
  - dj_notes@4.2: "The undocumented django.http.multipartparser.parse_header() function is removed."
- **[required] api_usage** `present` `"parse_header"`: The application imports or calls django.http.multipartparser.parse_header(). (confidence medium, judge supported)
  - dj_notes@4.2: "The undocumented django.http.multipartparser.parse_header() function is removed."
  - ⚠ The function is described as undocumented, so usage is likely rare and mostly in internal or third-party code.

Actions:
- Replace uses of django.http.multipartparser.parse_header() with django.utils.http.parse_header_parameters().
- Check third-party packages in the project for imports of the removed function and upgrade them if needed.

### HttpRequest.get_raw_uri() removed

`django_484b5127fa` · high · confidence high · introduced in 4.0 · fires at upgrade

The undocumented HttpRequest.get_raw_uri() method is removed in Django 4.0. Code that calls it will fail with AttributeError after upgrading from 3.2 to 4.2. HttpRequest.build_absolute_uri may be a suitable alternative.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, in which HttpRequest.get_raw_uri() is removed (3.2 -> 4.2). (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented HttpRequest.get_raw_uri() method is removed."
- **[required] api_usage** `present` `"get_raw_uri"`: The application code calls HttpRequest.get_raw_uri() (e.g. request.get_raw_uri()). (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented HttpRequest.get_raw_uri() method is removed."

Actions:
- Search the codebase and third-party/internal middleware for get_raw_uri() calls.
- Replace calls to get_raw_uri() with HttpRequest.build_absolute_uri() where suitable.
- Verify the output of build_absolute_uri() matches what the calling code expects, since it is only described as a 'may be suitable' alternative.

### Removed django.contrib.postgres.fields.JSONField model field

`django_48bd5222f5` · high · confidence high · introduced in 4.0 · fires at upgrade

The django.contrib.postgres.fields.JSONField model field is removed in Django 4.0, except for support in historical migrations. Application code (e.g. models) that still references this field will break when upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where the JSONField model field is removed. (confidence high, judge supported)
  - dj_notes@4.0: "The django.contrib.postgres.fields.JSONField model field is removed, except for support in historical migrations."
  - dj_deprecation: "The model django.contrib.postgres.fields.JSONField will be removed."
- **[required] api_usage** `present` `"django.contrib.postgres.fields.JSONField"`: The application references django.contrib.postgres.fields.JSONField in non-migration code (e.g. model definitions). (confidence high, judge supported)
  - dj_notes@4.0: "The django.contrib.postgres.fields.JSONField model field is removed"
  - dj_deprecation: "The model django.contrib.postgres.fields.JSONField will be removed."
  - dj_deprecation: "A stub field will remain for compatibility with historical migrations."
- **[disqualifying] api_usage** `absent` `"JSONField usage outside historical migrations"`: Usage only inside historical migrations remains supported and is not affected. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "except for support in historical migrations"

Actions:
- Search the codebase for django.contrib.postgres.fields.JSONField usage outside migrations.
- Replace usages in models with the JSONField model field available in Django's own model fields, not the postgres-specific one, and review any migrations accordingly.
- Search the codebase for django.contrib.postgres.fields.JSONField used outside historical migrations.
- The text does not name a replacement; verify the replacement field against the Django 4.0 release notes before changing models.

### django.contrib.postgres.forms.JSONField form field removed in 4.0

`django_48bd5222f5_486f` · high · confidence high · introduced in 4.0 · fires at upgrade

django.contrib.postgres.forms.JSONField is removed in Django 4.0. Code that imports or uses this form field will fail after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which django.contrib.postgres.forms.JSONField is removed. (confidence high, judge supported)
  - dj_notes@4.0: "django.contrib.postgres.forms.JSONField is removed."
  - dj_deprecation: "django.contrib.postgres.forms.JSONField, django.contrib.postgres.fields.jsonb.KeyTransform, and django.contrib.postgres.fields.jsonb.KeyTextTransform will be removed."
- **[required] api_usage** `present` `"django.contrib.postgres.forms.JSONField"`: The application imports or uses django.contrib.postgres.forms.JSONField. (confidence high, judge supported)
  - dj_notes@4.0: "django.contrib.postgres.forms.JSONField is removed."
  - dj_deprecation: "django.contrib.postgres.forms.JSONField, django.contrib.postgres.fields.jsonb.KeyTransform, and django.contrib.postgres.fields.jsonb.KeyTextTransform will be removed."

Actions:
- Find all uses of django.contrib.postgres.forms.JSONField and replace them with a supported alternative form field.
- Verify forms using the removed field still import and validate correctly after the upgrade.
- Find all usages of django.contrib.postgres.forms.JSONField and remove or replace them before upgrading to 4.0 or later.
- Run the test suite and any form-related code paths after the change.

### Oracle 12.2 or 18c database no longer officially supported

`django_4fb042cc41` · high · confidence medium · introduced in 4.0 · fires at upgrade

Django 4.0 dropped support for Oracle 12.2 and 18c. Deployments using the Oracle database backend against those versions are not officially supported after upgrading past 4.0 (including 4.2), which officially supports Oracle 19c per the 4.0 notes. The text does not state that the backend will fail outright.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which dropped support for Oracle 12.2 and 18c. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Django 4.0 officially supports Oracle 19c."
- **[required] database** `in_range` `"Oracle 12.2 or 18c"`: The deployment uses an Oracle database at version 12.2 or 18c. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Upstream support for Oracle 12.2 ends in March 2022 and for Oracle 18c it ends in June 2021."
  - ⚠ The text does not say whether Django 4.0+ actively fails on Oracle 12.2 or 18c, only that 4.0 officially supports 19c.
- **[disqualifying] database** `equals` `"Oracle 19c"`: The deployment uses Oracle 19c, which is officially supported by Django 4.0; the risk does not apply. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Django 4.0 officially supports Oracle 19c."

Actions:
- Check the Oracle database version used by the Django deployment.
- Upgrade Oracle to 19c, the version Django 4.0 officially supports, before or together with upgrading Django to 4.2.
- Alternatively, stay on Django 3.2, which the notes say is supported until April 2024.

### get_random_string() called without length argument

`django_4fceb7f197` · high · confidence high · introduced in 4.0 · fires at upgrade

Starting in Django 4.0, the length argument for django.utils.crypto.get_random_string() is required. Calls that omit length will no longer work when upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django release 4.0, where the length argument becomes required (3.2 -> 4.2). (confidence high, judge partially_supported)
  - dj_deprecation: "The length argument for django.utils.crypto.get_random_string() will be required."
  - dj_notes@4.0: "The length argument for django.utils.crypto.get_random_string() is required."
- **[required] api_usage** `present` `"get_random_string("`: The application calls django.utils.crypto.get_random_string() without passing the length argument. (confidence high, judge supported)
  - dj_deprecation: "The length argument for django.utils.crypto.get_random_string() will be required."
  - dj_notes@4.0: "The length argument for django.utils.crypto.get_random_string() is required."
  - ⚠ The text does not state what happens when length is omitted (e.g. the exact exception raised).
- **[uncertain] api_usage** `present` `"get_random_string(length"`: All get_random_string() calls already pass an explicit length, so the risk does not apply. (confidence low, judge not_supported)
  - dj_deprecation: "The length argument for django.utils.crypto.get_random_string() will be required."
  - ⚠ Judge: evidence does not support this claim. The quote only says length will be required; it does not establish that all calls already pass an explicit length or that the risk does not apply. The claim is a hypothesis about the application, and the quote only implies the risk would not apply for such apps, not that it is the case.

Actions:
- Search the codebase and third-party code for get_random_string() calls and pass an explicit length argument in each.
- Add tests covering code paths that generate random strings (tokens, passwords, secrets) before upgrading.
- Find all calls to get_random_string() and pass an explicit length argument.
- Add tests covering code paths that generate random strings before upgrading.

### Removed django.utils.http urlquote/urlunquote helpers

`django_529e399225` · high · confidence high · introduced in 4.0 · fires at upgrade

django.utils.http.urlquote(), urlquote_plus(), urlunquote(), and urlunquote_plus() are removed in Django 4.0. Application code that imports or calls them will fail (ImportError/AttributeError) after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where these functions are removed (3.2 -> 4.2). (confidence high, judge supported)
  - dj_notes@4.0: "are removed in Django 4.0"
  - dj_deprecation: "django.utils.http.urlquote(), urlquote_plus(), urlunquote(), and urlunquote_plus() will be removed."
- **[required] api_usage** `present` `"urlquote|urlquote_plus|urlunquote|urlunquote_plus"`: The application code uses any of django.utils.http.urlquote, urlquote_plus, urlunquote or urlunquote_plus. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.http.urlquote(), urlquote_plus(), urlunquote(), and urlunquote_plus() are removed."
  - dj_deprecation: "django.utils.http.urlquote(), urlquote_plus(), urlunquote(), and urlunquote_plus() will be removed."

Actions:
- Replace usages of django.utils.http.urlquote(), urlquote_plus(), urlunquote(), and urlunquote_plus() before upgrading; see deprecated-features-3.0 in the Django release notes for how to remove usage of these features.
- Search the codebase and third-party packages for imports of these functions and verify they do not rely on them.
- Search the codebase and third-party dependencies for urlquote, urlquote_plus, urlunquote and urlunquote_plus usage.
- The provided text does not name replacements; consult the Django 3.0 release notes referenced in the section for the recommended replacement APIs before upgrading.

### DatabaseOperations.insert_statement() ignore_conflicts argument replaced by on_conflict

`django_52f030f24e` · high · confidence high · introduced in 4.1 · fires at upgrade

In Django 4.1 the ignore_conflicts argument of DatabaseOperations.insert_statement() is replaced by on_conflict, which accepts django.db.models.constants.OnConflict. Third-party database backends that override or call insert_statement() with ignore_conflicts will need changes when upgrading across 4.1 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where the ignore_conflicts argument of insert_statement() was replaced by on_conflict. (confidence high, judge supported)
  - dj_notes@4.1: "The ignore_conflicts argument of the DatabaseOperations.insert_statement() method is replaced by on_conflict"
- **[required] api_usage** `present` `"insert_statement"`: The project contains a custom or third-party database backend that overrides or calls DatabaseOperations.insert_statement() using the ignore_conflicts argument. (confidence high, judge supported)
  - dj_notes@4.1: "The ignore_conflicts argument of the DatabaseOperations.insert_statement() method is replaced by on_conflict"
- **[optional] api_usage** `present` `"DatabaseOperations"`: The codebase includes a custom database backend (a DatabaseOperations subclass), as the section describes changes that may be needed in third-party database backends. (confidence high, judge supported)
  - dj_notes@4.1: "This section describes changes that may be needed in third-party database backends."

Actions:
- Update the insert_statement() override or callers to use on_conflict instead of ignore_conflicts.
- Use django.db.models.constants.OnConflict values for the on_conflict argument.
- Also update the backend for the related change replacing ignore_conflicts_suffix_sql() with on_conflict_suffix_sql() that accepts the fields, on_conflict, update_fields, and unique_fields arguments.

### PROJ < 5 support removed (GeoDjango)

`django_6b77e6a855` · high · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 removes support for PROJ versions older than 5. A deployment that uses PROJ < 5 will no longer be supported after the upgrade and needs PROJ upgraded. The text does not name GeoDjango explicitly or the exact failure mode.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where support for PROJ < 5 is removed. (confidence high, judge supported)
  - dj_notes@4.2: "Support for PROJ < 5 is removed."
- **[required] dependency** `less_than` `"5"`: The deployment uses a PROJ library version older than 5. (confidence medium, judge supported)
  - dj_notes@4.2: "Support for PROJ < 5 is removed."
  - ⚠ The text does not say which Django component (e.g. GeoDjango) uses PROJ or what failure occurs with PROJ < 5.

Actions:
- Check the installed PROJ version in the deployment and upgrade it to version 5 or newer before upgrading to Django 4.2.

### BaseCommand.requires_system_checks boolean value removed

`django_7a421fde8d` · high · confidence high · introduced in 4.1 · fires at upgrade

Support for using a boolean value in BaseCommand.requires_system_checks is removed in Django 4.1. Custom management commands that set requires_system_checks to a boolean are affected when upgrading from 3.2 to 4.2, which crosses 4.1. The text points to the 3.2 deprecation notes for how to remove usage but does not itself name the replacement value.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where support for a boolean value in BaseCommand.requires_system_checks is removed. (confidence high, judge supported)
  - dj_notes@4.1: "Support for using a boolean value in BaseCommand.requires_system_checks is removed."
  - dj_deprecation: "BaseCommand.requires_system_checks won't support boolean values."
- **[required] api_usage** `present` `"requires_system_checks"`: The application defines a custom management command (a BaseCommand subclass) that sets requires_system_checks to a boolean value (True or False). (confidence high, judge supported)
  - dj_notes@4.1: "Support for using a boolean value in BaseCommand.requires_system_checks is removed."
  - dj_deprecation: "BaseCommand.requires_system_checks won't support boolean values."
  - ⚠ The text does not state exactly what happens at runtime when a boolean is still used after removal.
  - ⚠ The text does not name the replacement value type (e.g. a list or tuple of tags or '__all__'), so the required migration form is not stated.
- **[uncertain] api_usage** `absent` `"requires_system_checks"`: The application has no custom commands that set requires_system_checks to a boolean value. (confidence low, judge not_supported)
  - dj_notes@4.1: "Support for using a boolean value in BaseCommand.requires_system_checks is removed."
  - ⚠ Judge: evidence does not support this claim. The quote only says boolean support is removed in 4.1; it says nothing about applications lacking such custom commands. The claim describes an unaffected scenario, which the evidence does not establish.

Actions:
- Search for custom management commands that set requires_system_checks to True or False and stop using boolean values.
- See the Django 3.2 deprecated-features notes (deprecated-features-3.2) for how to remove usage of this feature.
- Search management commands for requires_system_checks assigned to True or False and replace boolean values with a non-boolean value as described in the Django 3.2 release notes.
- Review the Django 3.2 release notes referenced by the deprecation timeline for the supported values.
- Run the custom management commands after upgrading to confirm they still work.

### GDAL 2.1 support removed in django.contrib.gis

`django_7e17fe7b65` · high · confidence medium · introduced in 4.1 · fires at upgrade

Django 4.1 removed support for GDAL 2.1 in django.contrib.gis. Deployments that use django.contrib.gis with GDAL 2.1 are no longer supported after the upgrade to 4.2 and need a newer GDAL version.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where support for GDAL 2.1 was removed. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "Support for GDAL 2.1 is removed."
  - dj_notes@4.0: "Support for GDAL 2.0 and GEOS 3.5 is removed."
  - ⚠ History: in 4.0, 'GDAL 2.0 and GEOS 3.5 support removed in django.contrib.gis' applied to the same symbol (gdal); superseded by the 4.1 change (R2).
- **[required] dependency** `equals` `"GDAL 2.1"`: The deployment uses django.contrib.gis with GDAL version 2.1 installed. (confidence medium, judge supported)
  - dj_notes@4.1: "Support for GDAL 2.1 is removed."
  - ⚠ The text does not say whether GDAL 2.1 fails outright or is merely unsupported, and it does not name the minimum supported GDAL version.

Actions:
- Check the GDAL version installed in each environment that uses django.contrib.gis.
- If GDAL 2.1 is in use, upgrade GDAL to a version supported by Django 4.2 before upgrading Django.
- Consult the Django 4.2 GIS installation documentation for the supported GDAL versions.

### SuccessURLAllowedHostsMixin replaced by RedirectURLMixin

`django_7e959d67c1` · high · confidence medium · introduced in 4.1 · fires at upgrade

The undocumented django.contrib.auth.views.SuccessURLAllowedHostsMixin mixin is replaced by RedirectURLMixin in 4.1. Code that imports or subclasses SuccessURLAllowedHostsMixin will need to switch to RedirectURLMixin.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where the mixin was replaced. (confidence high, judge supported)
  - dj_notes@4.1: "The undocumented django.contrib.auth.views.SuccessURLAllowedHostsMixin mixin is replaced by RedirectURLMixin."
- **[required] api_usage** `present` `"SuccessURLAllowedHostsMixin"`: The application imports or uses django.contrib.auth.views.SuccessURLAllowedHostsMixin (e.g. as a base class of custom views). (confidence medium, judge supported)
  - dj_notes@4.1: "The undocumented django.contrib.auth.views.SuccessURLAllowedHostsMixin mixin is replaced by RedirectURLMixin."
  - ⚠ The text does not state whether the old name remains importable as an alias after replacement.

Actions:
- Replace SuccessURLAllowedHostsMixin with RedirectURLMixin in imports and base classes of custom views.
- Test login/logout and other redirect flows that use the mixin.

### Third-party database backend uses removed DatabaseOperations._convert_field_to_tz()

`django_86e7176033` · high · confidence medium · introduced in 4.1 · fires at upgrade

DatabaseOperations._convert_field_to_tz() is replaced by DatabaseOperations._convert_sql_to_tz(), which accepts sql, params, and tzname arguments. Third-party or custom database backends that define, override or call _convert_field_to_tz() need to move to the new method and signature.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where _convert_field_to_tz() was replaced by _convert_sql_to_tz(). (confidence high, judge supported)
  - dj_notes@4.1: "DatabaseOperations._convert_field_to_tz() is replaced by DatabaseOperations._convert_sql_to_tz() that accepts the sql, params, and tzname arguments."
- **[required] api_usage** `present` `"_convert_field_to_tz"`: A custom or third-party database backend defines, overrides or calls DatabaseOperations._convert_field_to_tz(). (confidence medium, judge supported)
  - dj_notes@4.1: "DatabaseOperations._convert_field_to_tz() is replaced by DatabaseOperations._convert_sql_to_tz()"
  - dj_notes@4.1: "This section describes changes that may be needed in third-party database backends."
  - ⚠ The text does not say whether the replaced method is called outside database backends.

Actions:
- Replace _convert_field_to_tz() with _convert_sql_to_tz(), which accepts sql, params, and tzname arguments.
- Update any overrides or callers in custom or third-party database backends to the new signature.

### mysqlclient minimum version raised to 1.4.3

`django_991aa1d9db` · high · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of mysqlclient from 1.4.0 to 1.4.3. Deployments using mysqlclient older than 1.4.3 (e.g. 1.4.0 to 1.4.2) are below the supported minimum and need the dependency upgraded.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raises the minimum supported mysqlclient version. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of mysqlclient is increased from 1.4.0 to 1.4.3."
- **[required] dependency** `less_than` `"1.4.3"`: The project depends on mysqlclient (the MySQL driver) at a version below 1.4.3. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The minimum supported version of mysqlclient is increased from 1.4.0 to 1.4.3."
  - ⚠ The text does not state what happens with unsupported versions (e.g. whether Django fails at startup or only lacks support).

Actions:
- Upgrade mysqlclient to 1.4.3 or newer before or together with upgrading Django to 4.2.
- Check requirements files, lock files and base images for the pinned mysqlclient version.

### MiddlewareMixin.__init__ get_response now required and non-None

`django_9b90619b94` · high · confidence medium · introduced in 4.0 · fires at upgrade

As of Django 4.0, the get_response argument for django.utils.deprecation.MiddlewareMixin.__init__() is required and no longer accepts None. Custom middleware subclassing MiddlewareMixin that is instantiated without get_response, or with get_response=None, will break after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where this behavior change was made as the end of a deprecation cycle. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The get_response argument for django.utils.deprecation.MiddlewareMixin.init() is required and doesn't accept None."
- **[required] api_usage** `present` `"MiddlewareMixin"`: The application uses django.utils.deprecation.MiddlewareMixin, e.g. by subclassing it for custom middleware. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.deprecation.MiddlewareMixin.init()"
- **[required] api_usage** `present` `"get_response=None or missing get_response"`: The application instantiates a MiddlewareMixin subclass without get_response or with get_response=None. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "is required and doesn't accept None."
  - ⚠ The text does not state the exact exception raised when get_response is omitted or None.

Actions:
- Search for MiddlewareMixin subclasses and any direct instantiations of them, including in tests.
- Pass a valid get_response callable when instantiating MiddlewareMixin subclasses, and remove any get_response=None usage.

### CSRF_TRUSTED_ORIGINS may be required for subdomain requests with dot-prefixed cookie domain

`django_a0a165bd4b` · high · confidence medium · introduced in 4.0 · fires at first_use

Since CSRF protection now consults the Origin header, deployments that allow requests from subdomains by setting CSRF_COOKIE_DOMAIN (or SESSION_COOKIE_DOMAIN when CSRF_USE_SESSIONS is enabled) to a value starting with a dot may need to configure CSRF_TRUSTED_ORIGINS.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where CSRF protection began consulting the Origin header. (confidence high, judge supported)
  - dj_notes@4.0: "As CSRF protection now consults the Origin header"
  - dj_notes@4.0: "CSRF protection now consults the Origin header, if present."
- **[alternative] configuration** `present` `"CSRF_COOKIE_DOMAIN starting with '.'"`: CSRF_COOKIE_DOMAIN is set to a value starting with a dot to allow requests from subdomains. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "particularly if you allow requests from subdomains by setting CSRF_COOKIE_DOMAIN"
  - dj_notes@4.0: "some changes to the CSRF_TRUSTED_ORIGINS setting are required"
  - ⚠ The text does not state exactly which Origin values are rejected without CSRF_TRUSTED_ORIGINS.
  - ⚠ The text does not specify what changes to CSRF_TRUSTED_ORIGINS are required.
- **[alternative] configuration** `present` `"CSRF_USE_SESSIONS = True and SESSION_COOKIE_DOMAIN starting with '.'"`: CSRF_USE_SESSIONS is enabled and SESSION_COOKIE_DOMAIN is set to a value starting with a dot. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "(or SESSION_COOKIE_DOMAIN if CSRF_USE_SESSIONS is enabled)"
- **[uncertain] configuration** `absent` `"CSRF_TRUSTED_ORIGINS"`: CSRF_TRUSTED_ORIGINS is not already configured to cover the subdomain origins. (confidence low, judge partially_supported)
  - dj_notes@4.0: "you may need to set CSRF_TRUSTED_ORIGINS"
  - ⚠ The text says only that setting it 'may' be needed and does not give the required format or values.
- **[required] behavior** `present` `"Origin"`: Requests reaching the application include an Origin header, so the new Origin check applies. (confidence high, judge supported)
  - dj_notes@4.0: "CSRF protection now consults the Origin header, if present."

Actions:
- Review CSRF_COOKIE_DOMAIN (or SESSION_COOKIE_DOMAIN when CSRF_USE_SESSIONS is enabled) for values starting with a dot.
- Set CSRF_TRUSTED_ORIGINS to include the subdomain origins that submit requests, if applicable.
- Test cross-subdomain POST requests after the upgrade.
- Review the CSRF_TRUSTED_ORIGINS setting in all settings modules and update it as required by the Django 4.0 release notes.
- Test CSRF-protected requests, such as POST form submissions, that carry an Origin header against the updated configuration.

### Raw column aliases passed to QuerySet.order_by() no longer supported

`django_a45385a040` · high · confidence high · introduced in 4.0 · fires at first_use

Support for passing raw column aliases to QuerySet.order_by() was removed in Django 4.0 at the end of its deprecation cycle. Code that still passes raw column aliases to order_by() will break when upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where support for raw column aliases in order_by() was removed. (confidence high, judge supported)
  - dj_notes@4.0: "Support for passing raw column aliases to QuerySet.order_by() is removed."
  - dj_deprecation: "Support for passing raw column aliases to QuerySet.order_by() will be removed."
- **[required] api_usage** `present` `"order_by("`: The application calls QuerySet.order_by() passing raw column aliases. (confidence high, judge supported)
  - dj_notes@4.0: "Support for passing raw column aliases to QuerySet.order_by() is removed."
  - dj_deprecation: "Support for passing raw column aliases to QuerySet.order_by() will be removed."
  - ⚠ The text does not define what counts as a raw column alias or show how to detect one; the linked deprecation notes (deprecated-features-3.0) are not provided.
  - ⚠ The text does not define what counts as a raw column alias or how to detect it, so each order_by() call must be reviewed manually.

Actions:
- Find all order_by() calls and identify any that pass raw column aliases.
- Replace raw column aliases in order_by() as described in the Django deprecated-features-3.0 notes referenced by the release notes.
- Run the test suite covering ordered querysets on Django 4.2 to confirm they work.
- Review every QuerySet.order_by() call and stop passing raw column aliases.
- Test ordering queries on 4.2 to confirm they still work.

### Oracle table and column naming scheme change for names longer than 30 characters

`django_adab4c1b2a` · high · confidence medium · introduced in 4.0 · fires at upgrade

Django 4.0 inadvertently changed the table and column naming scheme on Oracle, causing errors for models and fields with names longer than 30 characters. Some Oracle tables and columns must be renamed, using the upgrade script in #33789 to generate RENAME statements.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which introduced the Oracle naming scheme change. (confidence high, judge supported)
  - dj_notes@4.0: "Django 4.0 inadvertently changed the table and column naming scheme on Oracle."
- **[required] database** `present` `"django.db.backends.oracle"`: The deployment uses Oracle as the database backend. (confidence high, judge supported)
  - dj_notes@4.0: "changed the table and column naming scheme on Oracle"
- **[required] api_usage** `greater_than` `"30 characters"`: The application has models or fields whose names are longer than 30 characters. (confidence medium, judge supported)
  - dj_notes@4.0: "errors for models and fields with names longer than 30 characters"
  - ⚠ The text does not state exactly which tables and columns need renaming; the upgrade script in #33789 generates the RENAME statements.

Actions:
- Use the upgrade script in #33789 to generate RENAME statements that change the naming scheme.
- Apply the generated RENAME statements to the affected Oracle tables and columns.
- Identify models and fields with names longer than 30 characters before upgrading.

### django.utils.http.is_safe_url() removed in 4.0

`django_b4c063edf8` · high · confidence high · introduced in 4.0 · fires at upgrade

django.utils.http.is_safe_url() was removed in Django 4.0 after completing its deprecation cycle. Application code that still calls or imports it will fail with an ImportError or AttributeError when upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which is_safe_url() was removed. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.http.is_safe_url() is removed."
  - dj_deprecation: "django.utils.http.is_safe_url() will be removed."
- **[required] api_usage** `present` `"is_safe_url"`: The application imports or calls django.utils.http.is_safe_url. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.http.is_safe_url() is removed."
  - dj_deprecation: "django.utils.http.is_safe_url() will be removed."

Actions:
- Search the codebase and third-party code for is_safe_url usage and remove it before upgrading.
- See deprecated-features-3.1 in the Django documentation for details on how to remove usage of this feature.
- Search the codebase and third-party dependencies for is_safe_url usage.
- Replace usages with the supported replacement for is_safe_url() before upgrading past 4.0; the provided text does not name the replacement, so consult the Django 3.0 and 3.1 release notes.

### cx_Oracle < 7.0 support removed

`django_b4c794e0cf` · high · confidence medium · introduced in 4.0 · fires at upgrade

Django 4.0 removed support for cx_Oracle versions older than 7.0. Deployments using Oracle with an older cx_Oracle driver are no longer supported on 4.2 and need a newer driver.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, which removed support for cx_Oracle < 7.0. (confidence high, judge supported)
  - dj_notes@4.0: "Support for cx_Oracle < 7.0 is removed."
- **[required] dependency** `less_than` `"7.0"`: The deployment uses the cx_Oracle driver at a version lower than 7.0. (confidence medium, judge supported)
  - dj_notes@4.0: "Support for cx_Oracle < 7.0 is removed."
  - ⚠ The text does not state the exact failure mode when an unsupported cx_Oracle version is used.

Actions:
- Upgrade cx_Oracle to version 7.0 or newer before upgrading Django.
- Verify the pinned cx_Oracle version in requirements files, lockfiles and deployment images.

### Exists expression negated parameter removed

`django_b5eb5cc228` · high · confidence medium · introduced in 4.2 · fires at first_use

The undocumented negated parameter of the Exists expression is removed in Django 4.2. Code that passes negated to Exists will break after upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which removes the negated parameter of Exists. (confidence high, judge supported)
  - dj_notes@4.2: "The undocumented negated parameter of the Exists expression is removed."
- **[required] api_usage** `present` `"Exists(..., negated=...)"`: The application passes the negated parameter to the Exists expression. (confidence medium, judge supported)
  - dj_notes@4.2: "The undocumented negated parameter of the Exists expression is removed."
  - ⚠ The text does not state what error occurs when the removed parameter is passed.

Actions:
- Search the codebase for Exists(...) calls that pass negated and remove that argument.
- Use the documented negation operator (~Exists(...)) instead, if negation is needed. This is not stated in the source text, so verify against the Django 4.2 documentation.

### isnull lookup with non-boolean right-hand side

`django_b921454a50` · high · confidence high · introduced in 4.0 · fires at first_use

As of Django 4.0 the isnull lookup no longer accepts non-boolean values as its right-hand side. Queries that pass truthy/falsy non-boolean values to __isnull will no longer work after the upgrade and must be changed to use True or False.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the isnull non-boolean right-hand side support was removed. (confidence high, judge supported)
  - dj_notes@4.0: "The isnull lookup no longer allows using non-boolean values as the right-hand side."
  - dj_deprecation: "The undocumented usage of the isnull lookup with non-boolean values as the right-hand side will no longer be allowed."
- **[required] api_usage** `present` `"__isnull with a non-boolean value"`: The application uses the isnull lookup with a non-boolean value (e.g. an integer or string) as the right-hand side. (confidence high, judge supported)
  - dj_notes@4.0: "The isnull lookup no longer allows using non-boolean values as the right-hand side."
  - dj_deprecation: "The undocumented usage of the isnull lookup with non-boolean values as the right-hand side will no longer be allowed."
  - ⚠ The text does not state what error is raised when a non-boolean value is used.
  - ⚠ The text does not state the exact failure mode (e.g., which exception is raised) when a non-boolean value is used.

Actions:
- Find all uses of the isnull lookup (e.g. filter(field__isnull=...), exclude(...), Q(...), and custom lookups) and make sure the right-hand side is a real boolean (True or False).
- Replace non-boolean values such as 0, 1, or strings with True or False before upgrading.
- Search the codebase for isnull lookups (e.g. __isnull=...) and the IsNull lookup class.
- Change any non-boolean right-hand side values to explicit True or False before upgrading.

### PostGIS 2.3 support removed in Django 4.0

`django_b9a44e805d` · high · confidence medium · introduced in 4.0 · fires at upgrade

Django 4.0 removed support for PostGIS 2.3. Deployments using django.contrib.gis with a PostGIS 2.3 spatial database are no longer supported on Django 4.0 and later, including 4.2, and need a newer PostGIS version.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which PostGIS 2.3 support was removed. (confidence high, judge supported)
  - dj_notes@4.0: "Support for PostGIS 2.3 is removed."
- **[required] database** `equals` `"PostGIS 2.3"`: The deployment uses a PostGIS 2.3 database as the spatial backend for django.contrib.gis. (confidence medium, judge supported)
  - dj_notes@4.0: "Support for PostGIS 2.3 is removed."
  - ⚠ The text does not say whether PostGIS 2.3 stops working or is merely no longer supported/tested.

Actions:
- Check the installed PostGIS version with SELECT PostGIS_Version(); on the spatial database.
- If it is PostGIS 2.3, upgrade PostGIS to a version supported by Django 4.2 before or as part of the Django upgrade.
- Consult the Django 4.2 documentation for the supported PostGIS versions.

### Signal providing_args argument removed

`django_bbcad62967` · high · confidence high · introduced in 4.0 · fires at upgrade

The providing_args argument for django.dispatch.Signal is removed in Django 4.0. Code that still passes providing_args when constructing a Signal will break after upgrading from 3.2 to 4.2, since the removal happened in 4.0.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where the providing_args argument was removed. (confidence high, judge supported)
  - dj_notes@4.0: "The providing_args argument for django.dispatch.Signal is removed."
  - dj_deprecation: "The providing_args argument for django.dispatch.Signal will be removed."
- **[required] api_usage** `present` `"providing_args"`: The application passes the providing_args argument when creating django.dispatch.Signal instances. (confidence high, judge supported)
  - dj_notes@4.0: "The providing_args argument for django.dispatch.Signal is removed."
  - dj_deprecation: "The providing_args argument for django.dispatch.Signal will be removed."

Actions:
- Remove the providing_args argument from all django.dispatch.Signal() constructions, including in third-party or internal code.
- Optionally document the arguments the signal sends in comments or docstrings instead.
- See deprecated-features-3.0 for details on how to remove usage of this argument.
- Remove the providing_args argument from all django.dispatch.Signal() constructions, including in third-party or internal packages that define signals.
- Document the arguments the signal sends in comments or docstrings instead.

### PASSWORD_RESET_TIMEOUT_DAYS setting removed

`django_bcd84f8d7d` · high · confidence high · introduced in 4.0 · fires at upgrade

The PASSWORD_RESET_TIMEOUT_DAYS setting is removed in Django 4.0 after its deprecation cycle. Projects that still define it in settings no longer get the configured password reset timeout from it, and any code reading it will break.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the PASSWORD_RESET_TIMEOUT_DAYS setting is removed. (confidence high, judge supported)
  - dj_notes@4.0: "The PASSWORD_RESET_TIMEOUT_DAYS setting is removed."
  - dj_deprecation: "The PASSWORD_RESET_TIMEOUT_DAYS setting will be removed."
- **[required] configuration** `present` `"PASSWORD_RESET_TIMEOUT_DAYS"`: The project settings or code reference the PASSWORD_RESET_TIMEOUT_DAYS setting. (confidence high, judge supported)
  - dj_notes@4.0: "The PASSWORD_RESET_TIMEOUT_DAYS setting is removed."
  - dj_deprecation: "The PASSWORD_RESET_TIMEOUT_DAYS setting will be removed."
  - ⚠ The text does not name the replacement setting; it only refers to deprecated-features-3.1 for details.
  - ⚠ The text does not state what replaces the setting or what happens at runtime if it is still defined.

Actions:
- Search settings modules, environment-specific settings and code for PASSWORD_RESET_TIMEOUT_DAYS and remove its usage.
- Consult the deprecated-features-3.1 notes referenced by the release notes for how to remove usage of this setting.
- Search settings modules and environment configuration for PASSWORD_RESET_TIMEOUT_DAYS and remove it.
- The text names no replacement setting; consult the Django release notes for the replacement and the equivalent timeout configuration.

### force_text and smart_text removed from django.utils.encoding

`django_bda96f577c` · high · confidence high · introduced in 4.0 · fires at upgrade

django.utils.encoding.force_text() and smart_text() are removed in Django 4.0. Code that imports or calls them will fail (ImportError/AttributeError) after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where force_text() and smart_text() are removed. (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.encoding.force_text() and smart_text() are removed."
  - dj_deprecation: "django.utils.encoding.force_text() and smart_text() will be removed."
- **[alternative] api_usage** `present` `"force_text"`: The application code uses django.utils.encoding.force_text(). (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.encoding.force_text() and smart_text() are removed."
  - dj_deprecation: "django.utils.encoding.force_text() and smart_text() will be removed."
- **[alternative] api_usage** `present` `"smart_text"`: The application code uses django.utils.encoding.smart_text(). (confidence high, judge supported)
  - dj_notes@4.0: "django.utils.encoding.force_text() and smart_text() are removed."

Actions:
- Find all usages of force_text() and smart_text() in application code and third-party code that you maintain.
- Consult the Django 3.0 deprecation notes (deprecated-features-3.0) for how to remove usage of these functions, as the release notes direct.
- Check third-party dependencies for use of these removed functions and upgrade them if needed.
- The text names no replacement. Remove or replace all uses of force_text() and smart_text() before upgrading to 4.0 or later.
- Check third-party packages for imports of force_text and smart_text and upgrade them if they use these functions.

### Expression.get_group_by_cols alias argument removed

`django_bddad2ae28` · high · confidence medium · introduced in 4.2 · fires at upgrade

The alias argument for Expression.get_group_by_cols is removed in Django 4.2. Custom expressions that override get_group_by_cols with an alias parameter, or code that calls it passing alias, will break.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where the alias argument of Expression.get_group_by_cols is removed. (confidence high, judge supported)
  - dj_notes@4.2: "The alias argument for Expression.get_group_by_cols is removed."
- **[required] api_usage** `present` `"get_group_by_cols"`: The application calls or overrides Expression.get_group_by_cols, passing or accepting the alias argument. (confidence medium, judge supported)
  - dj_notes@4.2: "The alias argument for Expression.get_group_by_cols is removed."
  - ⚠ The text does not say whether custom expression subclasses that override get_group_by_cols are affected, only that the alias argument is removed.

Actions:
- Search for custom Expression subclasses or code that defines or calls get_group_by_cols and remove the alias argument from signatures and calls.
- Run the test suite for queries using aggregation or annotation with custom expressions after upgrading.

### Removal of django.contrib.postgres.fields.jsonb.KeyTextTransform

`django_c3e27d1cef` · high · confidence high · introduced in 4.0 · fires at upgrade

django.contrib.postgres.fields.jsonb.KeyTextTransform is listed in the 4.0 deprecation timeline as removed. Code that still uses it will break when the project upgrades from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where this removal is listed in the deprecation timeline. (confidence high, judge supported)
  - dj_deprecation: "django.contrib.postgres.forms.JSONField, django.contrib.postgres.fields.jsonb.KeyTransform, and django.contrib.postgres.fields.jsonb.KeyTextTransform will be removed."
- **[required] api_usage** `present` `"django.contrib.postgres.fields.jsonb.KeyTextTransform"`: The application imports or uses django.contrib.postgres.fields.jsonb.KeyTextTransform. (confidence high, judge supported)
  - dj_deprecation: "django.contrib.postgres.forms.JSONField, django.contrib.postgres.fields.jsonb.KeyTransform, and django.contrib.postgres.fields.jsonb.KeyTextTransform will be removed."

Actions:
- Find all usages of django.contrib.postgres.fields.jsonb.KeyTextTransform and remove or replace them before upgrading to 4.0 or later.
- Run the test suite and any queries that use JSON key text transforms after the change.

### psycopg2 minimum version raised to 2.8.4

`django_c8a5898132` · high · confidence medium · introduced in 4.0 · fires at upgrade

The minimum supported psycopg2 version is increased from 2.5.4 to 2.8.4 in Django 4.0. Deployments that pin or install an older psycopg2 must upgrade it.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which raised the minimum supported psycopg2 version. (confidence high, judge supported)
  - dj_notes@4.0: "the minimum supported version of psycopg2 is increased from 2.5.4 to 2.8.4"
- **[required] dependency** `less_than` `"2.8.4"`: The project installs psycopg2 at a version older than 2.8.4. (confidence medium, judge supported)
  - dj_notes@4.0: "the minimum supported version of psycopg2 is increased from 2.5.4 to 2.8.4"
  - ⚠ The text says the minimum is raised but does not state what failure occurs with an older psycopg2.

Actions:
- Upgrade psycopg2 (or psycopg2-binary) to 2.8.4 or newer in requirements files and lock files.

### django-admin.py entry point removed

`django_d7efdc3269` · high · confidence medium · introduced in 4.0 · fires at upgrade

The django-admin.py entry point is removed in Django 4.0. Scripts, deployment tooling, or documentation that invoke django-admin.py will break after upgrading past 4.0 and must be updated. The text does not name the replacement.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the django-admin.py entry point is removed. (confidence high, judge supported)
  - dj_notes@4.0: "The django-admin.py entry point is removed."
  - dj_deprecation: "The django-admin.py entry point will be removed."
- **[required] deployment** `present` `"django-admin.py"`: Scripts, Dockerfiles, CI configs, Makefiles, or docs invoke django-admin.py. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The django-admin.py entry point is removed."
  - dj_deprecation: "The django-admin.py entry point will be removed."
  - ⚠ The text does not state where django-admin.py might be invoked (scripts, CI, deployment tooling); this is inferred from how entry points are typically used.
  - ⚠ The text does not name the replacement entry point (e.g. django-admin) or say where invocations might occur.

Actions:
- Search scripts, deployment files, CI configuration, and docs for django-admin.py and update invocations to use an entry point that remains available in 4.x.
- See deprecated-features-3.0 for details on how to remove usage of this feature, as referenced in the release notes.
- Search shell scripts, Dockerfiles, Makefiles, CI configs, systemd units and docs for django-admin.py and replace those invocations with an alternative that is not django-admin.py before upgrading.
- Run management commands in a staging environment on 4.2 to confirm they still start.

### Removed django.contrib.postgres.fields.jsonb.KeyTransform and KeyTextTransform

`django_dfc647ada4` · high · confidence high · introduced in 4.0 · fires at upgrade

django.contrib.postgres.fields.jsonb.KeyTransform and django.contrib.postgres.fields.jsonb.KeyTextTransform are removed in Django 4.0. Code importing or using them from that module will break after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where these features reached the end of their deprecation cycle and were removed. (confidence high, judge supported)
  - dj_notes@4.0: "These features have reached the end of their deprecation cycle and are removed in Django 4.0."
  - dj_deprecation: "django.contrib.postgres.forms.JSONField, django.contrib.postgres.fields.jsonb.KeyTransform, and django.contrib.postgres.fields.jsonb.KeyTextTransform will be removed."
- **[alternative] api_usage** `present` `"KeyTransform"`: The application uses django.contrib.postgres.fields.jsonb.KeyTransform. (confidence high, judge supported)
  - dj_notes@4.0: "django.contrib.postgres.fields.jsonb.KeyTransform and django.contrib.postgres.fields.jsonb.KeyTextTransform are removed."
  - dj_deprecation: "django.contrib.postgres.forms.JSONField, django.contrib.postgres.fields.jsonb.KeyTransform, and django.contrib.postgres.fields.jsonb.KeyTextTransform will be removed."
- **[alternative] api_usage** `present` `"KeyTextTransform"`: The application uses django.contrib.postgres.fields.jsonb.KeyTextTransform. (confidence high, judge supported)
  - dj_notes@4.0: "django.contrib.postgres.fields.jsonb.KeyTransform and django.contrib.postgres.fields.jsonb.KeyTextTransform are removed."

Actions:
- Search the codebase and migrations for imports of KeyTransform and KeyTextTransform from django.contrib.postgres.fields.jsonb.
- Replace these usages as described in the Django 3.1 deprecation notes, since the text refers to deprecated-features-3.1 for details on removing usage; the replacement is not named in the provided text.
- Find all usages of django.contrib.postgres.fields.jsonb.KeyTransform and remove or replace them before upgrading to 4.0 or later.
- Run the test suite and any queries that use JSON key transforms after the change.

### MiddlewareMixin.__init__ get_response required

`django_e78cbd4ca0` · high · confidence low · introduced in 4.0 · fires at upgrade

As of release 4.0, the get_response argument for django.utils.deprecation.MiddlewareMixin.__init__() is required and no longer accepts None. Custom middleware subclassing MiddlewareMixin that is instantiated without get_response or with None will break.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where get_response became required for MiddlewareMixin.__init__(). (confidence high, judge supported)
  - dj_deprecation: "The get_response argument for django.utils.deprecation.MiddlewareMixin.init() will be required and won't accept None."
- **[required] api_usage** `present` `"MiddlewareMixin"`: The application uses django.utils.deprecation.MiddlewareMixin, for example by subclassing it for custom middleware. (confidence high, judge supported)
  - dj_deprecation: "The get_response argument for django.utils.deprecation.MiddlewareMixin.init() will be required and won't accept None."
- **[required] api_usage** `present` `"get_response=None"`: The application instantiates a MiddlewareMixin subclass directly, or calls its __init__, without get_response or with get_response=None. (confidence low, judge partially_supported)
  - dj_deprecation: "will be required and won't accept None."
  - ⚠ The text does not say how to detect direct instantiation without get_response; the usual path is Django's middleware loader, which passes get_response.

Actions:
- Find all MiddlewareMixin subclasses and any direct instantiations or __init__ overrides.
- Ensure get_response is always passed as a non-None callable to MiddlewareMixin.__init__().
- Remove default None values for get_response in custom middleware that call MiddlewareMixin.__init__().

### InvalidQuery exception class removed

`django_f1dbbd4617` · high · confidence high · introduced in 4.0 · fires at upgrade

The django.db.models.query_utils.InvalidQuery exception class is removed in Django 4.0. Application code that imports, raises or catches InvalidQuery will fail (e.g. ImportError) after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, in which InvalidQuery is removed. (confidence high, judge partially_supported)
  - dj_notes@4.0: "The django.db.models.query_utils.InvalidQuery exception class is removed."
  - dj_deprecation: "The django.db.models.query_utils.InvalidQuery exception class will be removed."
- **[required] api_usage** `present` `"InvalidQuery"`: The application references django.db.models.query_utils.InvalidQuery (imports, raises or catches it). (confidence high, judge supported)
  - dj_notes@4.0: "The django.db.models.query_utils.InvalidQuery exception class is removed."
  - dj_deprecation: "The django.db.models.query_utils.InvalidQuery exception class will be removed."
  - ⚠ The text does not state a replacement exception or which operations previously raised InvalidQuery.

Actions:
- Search the codebase and third-party dependencies for InvalidQuery references and remove them.
- The text does not name a replacement; consult deprecated-features-3.0 as referenced in the release notes for how to remove usage.
- Search the codebase and third-party dependencies for InvalidQuery and remove or replace its imports and except clauses.
- Consult the Django 3.0 release notes referenced in the parent context for details on the replacement behavior.

### DatabaseIntrospection.get_key_columns() removed

`django_f48d26d0fe` · high · confidence medium · introduced in 4.1 · fires at upgrade

DatabaseIntrospection.get_key_columns() is removed in Django 4.1. Third-party database backends or code that define or call this method will break and must use DatabaseIntrospection.get_relations() instead.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where DatabaseIntrospection.get_key_columns() is removed. (confidence high, judge supported)
  - dj_notes@4.1: "DatabaseIntrospection.get_key_columns() is removed."
- **[required] api_usage** `present` `"get_key_columns"`: The project, or a third-party database backend it uses, defines or calls DatabaseIntrospection.get_key_columns(). (confidence medium, judge supported)
  - dj_notes@4.1: "DatabaseIntrospection.get_key_columns() is removed."
  - ⚠ The text says the section covers changes that may be needed in third-party database backends, but does not say whether application code calling the method is also affected.

Actions:
- Replace calls to and overrides of DatabaseIntrospection.get_key_columns() with DatabaseIntrospection.get_relations().
- If a third-party database backend is used, upgrade it to a version compatible with Django 4.1 or later.

### RawSQL aggregations on MySQL no longer supported

`django_f9cd53a9aa` · high · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 removes the pre-4.2 workaround of grouping by primary keys of the main table on MySQL 8+. As a consequence, RawSQL() aggregations are no longer supported on MySQL, because Django cannot determine whether such aggregations are needed or valid in the GROUP BY clause. Applications using RawSQL() in aggregations on MySQL must switch to aggregation functions.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where the GROUP BY primary-key workaround is removed and RawSQL() aggregations stop being supported on MySQL. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "the pre-Django 4.2 workaround of grouping by primary keys of the main table is removed"
- **[required] api_usage** `present` `"RawSQL"`: The application uses RawSQL() in aggregations. (confidence high, judge supported)
  - dj_notes@4.2: "using RawSQL() aggregations is no longer supported on MySQL"
- **[required] database** `contains` `"django.db.backends.mysql"`: The application runs against a MySQL database backend. (confidence medium, judge supported)
  - dj_notes@4.2: "RawSQL() aggregations is no longer supported on MySQL"
  - ⚠ The text discusses MySQL 8+ functional dependencies but states the RawSQL() restriction for MySQL generally, without a version bound.

Actions:
- Search the codebase for RawSQL() used in aggregations (annotate/aggregate) on MySQL-backed databases.
- Replace RawSQL() aggregations with Django aggregation functions.
- Test affected queries on MySQL after the upgrade.

### EmailValidator whitelist argument and domain_whitelist attribute removed

`django_ffce931536` · high · confidence high · introduced in 4.1 · fires at upgrade

The whitelist argument and domain_whitelist attribute of django.core.validators.EmailValidator were removed in Django 4.1. Code that passes whitelist to EmailValidator or reads/sets domain_whitelist will break after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, in which the EmailValidator whitelist argument and domain_whitelist attribute were removed. (confidence high, judge partially_supported)
  - dj_notes@4.1: "The whitelist argument and domain_whitelist attribute of django.core.validators.EmailValidator are removed."
  - dj_deprecation: "The whitelist argument and domain_whitelist attribute of django.core.validators.EmailValidator will be removed."
- **[alternative] api_usage** `present` `"EmailValidator(whitelist="`: The application passes the whitelist argument to django.core.validators.EmailValidator. (confidence high, judge supported)
  - dj_notes@4.1: "The whitelist argument and domain_whitelist attribute of django.core.validators.EmailValidator are removed."
  - dj_deprecation: "The whitelist argument and domain_whitelist attribute of django.core.validators.EmailValidator will be removed."
- **[alternative] api_usage** `present` `"domain_whitelist"`: The application reads or sets the domain_whitelist attribute on an EmailValidator instance or subclass. (confidence high, judge supported)
  - dj_notes@4.1: "The whitelist argument and domain_whitelist attribute of django.core.validators.EmailValidator are removed."

Actions:
- Search the codebase for EmailValidator usages passing whitelist or referencing domain_whitelist.
- Follow the deprecated-features-3.2 notes referenced by the release notes to replace usage of these removed features.
- Search the codebase for EmailValidator usages that pass whitelist or access domain_whitelist.
- Replace usage of the removed whitelist argument and domain_whitelist attribute before upgrading to 4.2; the provided text does not name the replacement, so consult the Django 3.2 release notes it references.

### Custom save() methods modifying fields not added to update_fields under QuerySet.update_or_create

`django_00ef9fd5ad` · medium · confidence medium · introduced in 4.2 · fires at first_use

Starting in 4.2, QuerySet.update_or_create passes update_fields to Model.save(). Any fields modified inside a custom save() method that are not added to update_fields before calling super() will not be persisted by update_or_create calls.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where update_or_create began passing update_fields to Model.save(). (confidence high, judge supported)
  - dj_notes@4.2: "QuerySet.update_or_create now passes update_fields to the Model.save() calls"
- **[required] api_usage** `present` `"def save("`: The application defines a custom save() method on a model that modifies fields within save(). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "any fields modified in the custom save() methods should be added to the update_fields keyword argument before calling super()"
- **[required] api_usage** `present` `"update_or_create"`: The application calls QuerySet.update_or_create (or related manager update_or_create) on models whose custom save() modifies fields. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "QuerySet.update_or_create now passes update_fields to the Model.save() calls"
- **[disqualifying] behavior** `contains` `"update_fields"`: The custom save() already adds the modified fields to update_fields before calling super(), so the risk does not apply. (confidence low, judge partially_supported)
  - dj_notes@4.2: "should be added to the update_fields keyword argument before calling super()"

Actions:
- Review every custom save() method on models used with update_or_create.
- In each custom save(), add any fields modified in the method to the update_fields keyword argument before calling super().save().
- See the 'overriding model methods' documentation for details.
- Add tests covering update_or_create with models that have custom save() methods.

### Third-party database backend relies on removed DatabaseFeatures.allows_group_by_pk

`django_11fa2712b1` · medium · confidence medium · introduced in 4.2 · fires at upgrade

DatabaseFeatures.allows_group_by_pk is removed in Django 4.2. Third-party database backends that define or rely on it must be updated; allows_group_by_selected_pks remains supported and should be enabled if the backend supports functional dependency detection in GROUP BY clauses per SQL:1999.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, in which DatabaseFeatures.allows_group_by_pk is removed. (confidence high, judge supported)
  - dj_notes@4.2: "DatabaseFeatures.allows_group_by_pk is removed"
- **[required] api_usage** `present` `"allows_group_by_pk"`: A custom or third-party database backend defines or references DatabaseFeatures.allows_group_by_pk. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "DatabaseFeatures.allows_group_by_pk is removed"
  - dj_notes@4.2: "This section describes changes that may be needed in third-party database backends."
  - ⚠ The text does not state what happens if a backend still sets the removed attribute.
- **[optional] api_usage** `absent` `"allows_group_by_selected_pks"`: The backend supports functional dependency detection in GROUP BY clauses as specified by SQL:1999 but does not enable allows_group_by_selected_pks. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "should be enabled if your backend supports functional dependency detection in GROUP BY clauses as specified by the SQL:1999 standard"

Actions:
- Remove allows_group_by_pk from the backend's DatabaseFeatures.
- Enable DatabaseFeatures.allows_group_by_selected_pks if the backend supports functional dependency detection in GROUP BY clauses as specified by the SQL:1999 standard.

### Third-party database backend overrides DatabaseOperations.ignore_conflicts_suffix_sql()

`django_1640c056a6` · medium · confidence high · introduced in 4.1 · fires at first_use

In Django 4.1, DatabaseOperations.ignore_conflicts_suffix_sql() is replaced by DatabaseOperations.on_conflict_suffix_sql(), which accepts the fields, on_conflict, update_fields, and unique_fields arguments. Third-party or custom database backends that define or call ignore_conflicts_suffix_sql() need to be updated to the new method.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where ignore_conflicts_suffix_sql() was replaced. (confidence high, judge supported)
  - dj_notes@4.1: "DatabaseOperations.ignore_conflicts_suffix_sql() method is replaced by DatabaseOperations.on_conflict_suffix_sql()"
- **[required] api_usage** `present` `"ignore_conflicts_suffix_sql"`: The project contains a custom or third-party database backend that defines or calls DatabaseOperations.ignore_conflicts_suffix_sql(). (confidence high, judge supported)
  - dj_notes@4.1: "DatabaseOperations.ignore_conflicts_suffix_sql() method is replaced by DatabaseOperations.on_conflict_suffix_sql()"
  - dj_notes@4.1: "This section describes changes that may be needed in third-party database backends."

Actions:
- Replace overrides or calls of ignore_conflicts_suffix_sql() with on_conflict_suffix_sql(fields, on_conflict, update_fields, unique_fields).
- If using a third-party database backend, upgrade it to a version that supports Django 4.1+.

### redis-py minimum version raised to 3.4.0

`django_177f98da33` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of redis-py from 3.0.0 to 3.4.0. Deployments with redis-py older than 3.4.0 (for example, when using Django's Redis cache backend) are below the supported minimum and need redis-py upgraded.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raises the minimum supported redis-py version. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of redis-py is increased from 3.0.0 to 3.4.0."
- **[required] dependency** `less_than` `"3.4.0"`: The deployment has the redis-py package installed at a version older than 3.4.0. (confidence medium, judge supported)
  - dj_notes@4.2: "The minimum supported version of redis-py is increased from 3.0.0 to 3.4.0."
  - ⚠ The text does not state which Django features use redis-py or what failure occurs with an unsupported version.

Actions:
- Upgrade redis-py to version 3.4.0 or newer before or together with the Django 4.2 upgrade.
- Update pinned redis-py versions in requirements files, lock files and container images.

### has_case_insensitive_like default changed from True to False for third-party database backends

`django_17b16d25e5` · medium · confidence medium · introduced in 4.1 · fires at upgrade

In Django 4.1 the BaseDatabaseFeatures.has_case_insensitive_like default changed from True to False. Third-party database backends that subclass BaseDatabaseFeatures and relied on the inherited True default will now get False, which may change behavior (e.g. in tests that are skipped or run depending on this feature flag). The section states this may need changes in third-party database backends.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where has_case_insensitive_like default changed from True to False. (confidence high, judge supported)
  - dj_notes@4.1: "BaseDatabaseFeatures.has_case_insensitive_like is changed from True to False"
- **[required] api_usage** `present` `"has_case_insensitive_like"`: The project ships or uses a custom/third-party database backend with a features class subclassing BaseDatabaseFeatures that relies on the inherited has_case_insensitive_like value. (confidence medium, judge supported)
  - dj_notes@4.1: "This section describes changes that may be needed in third-party database backends."
  - dj_notes@4.1: "BaseDatabaseFeatures.has_case_insensitive_like is changed from True to False"
  - ⚠ The text does not state the specific behavioral consequence of the changed flag for backends or applications.
- **[uncertain] api_usage** `present` `"has_case_insensitive_like ="`: The backend's DatabaseFeatures explicitly sets has_case_insensitive_like, so the new default does not apply. (confidence low, judge not_supported)
  - dj_notes@4.1: "BaseDatabaseFeatures.has_case_insensitive_like is changed from True to False"
  - ⚠ The text does not explicitly discuss overrides; this follows from the change being to the base class default.
  - ⚠ Judge: evidence does not support this claim. The quote only states the base default changed; it says nothing about a backend explicitly setting has_case_insensitive_like or that an explicit setting means the new default does not apply.

Actions:
- For custom/third-party database backends, check whether the backend's DatabaseFeatures relies on the inherited has_case_insensitive_like value and set it explicitly to the value that matches the database's actual behavior.
- Review any behavior or tests that depend on has_case_insensitive_like after the upgrade.

### DeleteView custom delete() logic must move to form_valid()

`django_18e8b24987` · medium · confidence medium · introduced in 4.0 · fires at first_use

DeleteView now uses FormMixin, so object deletion for POST requests is handled in form_valid() instead of delete(). Custom delete logic in delete() handlers on DeleteView subclasses should be moved to form_valid() or a shared helper method.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where DeleteView was changed to use FormMixin. (confidence high, judge supported)
  - dj_notes@4.0: "DeleteView now uses FormMixin"
  - dj_notes@4.0: "DeleteView now uses FormMixin to handle POST requests."
- **[required] api_usage** `present` `"DeleteView"`: The application defines DeleteView subclasses that override delete() with custom deletion logic. (confidence medium, judge supported)
  - dj_notes@4.0: "Custom delete logic in delete() handlers should be moved to form_valid(), or a shared helper method, as needed."
  - dj_notes@4.0: "any custom deletion logic in delete() handlers should be moved to form_valid()"
  - ⚠ The text does not state explicitly whether an overridden delete() is still called on POST requests, only that deletion is handled in form_valid() and that custom logic should be moved.
  - ⚠ The text does not state precisely how delete() is affected, for example whether it is no longer called on POST.
- **[uncertain] api_usage** `absent` `"def delete("`: The application's DeleteView subclasses already implement deletion in form_valid() or a shared helper, so no custom delete() logic remains. (confidence low, judge not_supported)
  - dj_notes@4.0: "object deletion for POST requests is handled in form_valid()"
  - ⚠ Judge: evidence does not support this claim. The quote only says that in 4.0 DeleteView handles POST deletion in form_valid(). It does not establish that the application's subclasses already implement deletion in form_valid() or a shared helper, nor that no custom delete() logic remains.

Actions:
- Find all DeleteView subclasses that override delete().
- Move custom delete logic from delete() into form_valid(), or into a shared helper method called from form_valid().
- Test POST deletion flows for those views after upgrading.
- Optionally provide a Form subclass (for example with a confirmation checkbox) or use SuccessMessageMixin now that DeleteView uses FormMixin.
- Find DeleteView subclasses that override delete() with custom deletion logic.
- Move that logic into form_valid(), or into a shared helper method called from form_valid().
- Test POST deletion flows for these views after upgrading.

### CSRF cookie masking mismatch during multi-instance rollout to 4.1+

`django_19d2656132` · medium · confidence medium · introduced in 4.1 · fires at rollout

From 4.1, CsrfViewMiddleware no longer masks the CSRF cookie. When multiple instances of the same project are upgraded, the transition should set CSRF_COOKIE_MASKED to True for compatibility with older Django versions. The setting is deprecated as of 4.1 and will be removed in Django 5.0, so the override should be dropped once the transition is complete.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where the CSRF cookie masking change and the CSRF_COOKIE_MASKED setting were introduced. (confidence high, judge supported)
  - dj_notes@4.1: "The new CSRF_COOKIE_MASKED transitional setting allows specifying whether to mask the CSRF cookie."
- **[required] api_usage** `present` `"CsrfViewMiddleware"`: The project uses CsrfViewMiddleware, which no longer masks the CSRF cookie. (confidence high, judge supported)
  - dj_notes@4.1: "CsrfViewMiddleware no longer masks the CSRF cookie like it does the CSRF token in the DOM"
- **[required] deployment** `greater_than` `"1 instance of the project running during the transition"`: Multiple instances of the same project are being upgraded to Django 4.1 or later, so instances on older and newer Django versions may run side by side during the transition. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "If you are upgrading multiple instances of the same project to Django 4.1"
  - ⚠ The text does not state the exact failure mode if instances on different versions interpret the CSRF cookie differently.
- **[disqualifying] configuration** `equals` `"True"`: CSRF_COOKIE_MASKED is already set to True during the transition, in which case the compatibility risk is mitigated. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "you should set CSRF_COOKIE_MASKED to True during the transition"

Actions:
- During the rollout of multiple instances, set CSRF_COOKIE_MASKED = True to stay compatible with older Django versions.
- Once all instances are on Django 4.1 or later, stop overriding CSRF_COOKIE_MASKED.
- Do not rely on CSRF_COOKIE_MASKED long term: it is deprecated as of 4.1 and will be removed in Django 5.0.

### Custom BaseConstraint subclasses must implement validate()

`django_1f6435a996` · medium · confidence medium · introduced in 4.1 · fires at first_use

As of Django 4.1, custom subclasses of BaseConstraint must implement a validate method for the constraint to be usable for validation. Custom constraints without validate() cannot be used for validation after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, which introduced this requirement. (confidence high, judge supported)
  - dj_notes@4.1: "BaseConstraint subclasses must implement validate method to allow those constraints to be used for validation."
- **[required] api_usage** `present` `"BaseConstraint"`: The application defines a custom subclass of BaseConstraint. (confidence high, judge supported)
  - dj_notes@4.1: "BaseConstraint subclasses must implement validate method"
- **[required] api_usage** `absent` `"def validate("`: The custom BaseConstraint subclass does not implement a validate method and is expected to be used for validation. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "to allow those constraints to be used for validation"
  - ⚠ The text does not state the exact failure mode (e.g. exception type) when validate is not implemented.

Actions:
- Find custom BaseConstraint subclasses and implement a validate() method on each one that should be used for validation.
- Run tests exercising model validation (e.g. full_clean/validate_constraints) for models using custom constraints.

### SecurityMiddleware now adds Cross-Origin-Opener-Policy: same-origin by default

`django_21dcaab3e7` · medium · confidence medium · introduced in 4.0 · fires at upgrade

Starting in Django 4.0, SecurityMiddleware adds the Cross-Origin Opener Policy header with value 'same-origin' by default, which prevents cross-origin popups from sharing the same browsing context. Apps relying on cross-origin popups sharing a browsing context may behave differently. The header can be disabled by setting SECURE_CROSS_ORIGIN_OPENER_POLICY to None.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where SecurityMiddleware began adding the Cross-Origin Opener Policy header. (confidence high, judge supported)
  - dj_notes@4.0: "The SecurityMiddleware now adds the Cross-Origin Opener Policy header with a value of 'same-origin'"
- **[required] configuration** `present` `"django.middleware.security.SecurityMiddleware"`: The application uses SecurityMiddleware (enabled in MIDDLEWARE). (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The SecurityMiddleware now adds the Cross-Origin Opener Policy header"
- **[required] configuration** `absent` `"SECURE_CROSS_ORIGIN_OPENER_POLICY"`: SECURE_CROSS_ORIGIN_OPENER_POLICY is not explicitly set (e.g. to None), so the new 'same-origin' default applies. (confidence high, judge supported)
  - dj_notes@4.0: "You can prevent this header from being added by setting the SECURE_CROSS_ORIGIN_OPENER_POLICY setting to None."
- **[optional] behavior** `present` `"cross-origin popups sharing browsing context"`: The application relies on cross-origin popups or windows sharing the same browsing context (e.g. OAuth/payment popups communicating via window.opener). (confidence low, judge partially_supported)
  - dj_notes@4.0: "to prevent cross-origin popups from sharing the same browsing context"
  - ⚠ The text does not state which specific application behaviors break, only the stated purpose of the header.

Actions:
- Set SECURE_CROSS_ORIGIN_OPENER_POLICY = None in settings to prevent the header from being added if the previous behavior is required.
- Test any flows using cross-origin popups against the new 'same-origin' header before upgrading.

### Admin multi-term search over multi-valued relationships now requires all terms to match the same related row

`django_21e9ff39c5` · medium · confidence medium · introduced in 4.1 · fires at first_use

Since Django 4.1, admin changelist searches with multiple search terms are applied in a single filter() call. For search_fields spanning multi-valued relationships, a single related row must now match all terms, so searches that previously returned parents matching terms via different related rows now return fewer results.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where admin multi-term search behavior changed (3.2 -> 4.2 includes 4.1). (confidence medium, judge partially_supported)
  - dj_notes@4.1: "Admin changelist searches using multiple search terms are now applied in a single call to filter(), rather than in sequential filter() calls."
- **[required] api_usage** `present` `"search_fields"`: A ModelAdmin defines search_fields that span a multi-valued relationship (e.g. reverse foreign key or many-to-many), such as ['childname', 'childage']. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "if search_fields is set to ['childname', 'childage']"
  - dj_notes@4.1: "For multi-valued relationships, this means that rows from the related model must match all terms rather than any term."
  - ⚠ The text does not state how to determine which search_fields entries span multi-valued relationships; this requires inspecting model relations.
- **[optional] api_usage** `present` `"get_search_results"`: The application overrides or calls get_search_results, which followed the old sequential-filter behavior in 4.0 and earlier. (confidence low, judge partially_supported)
  - dj_notes@4.1: "In Django 4.0 and earlier, get_search_results followed the second example query"
  - ⚠ The text does not say whether custom overrides of get_search_results are affected.
- **[uncertain] behavior** `unknown` `"search results differ after upgrade"`: Users or tests rely on multi-term admin searches returning parents whose different related rows each match different terms. (confidence low, judge partially_supported)
  - dj_notes@4.1: "parent rows will be returned only if there is a relationship to some 17-year-old child named Jamal"
  - ⚠ The text does not state whether any given application relies on the old matching behavior.

Actions:
- Review ModelAdmin.search_fields entries that span multi-valued relationships and confirm that requiring a single related row to match all search terms is acceptable.
- Review any get_search_results overrides and tests of admin search results for dependence on the previous behavior.
- See the spanning-multi-valued-relationships topic in the Django documentation for a discussion of the difference between the two query forms.

### assertQuerysetEqual no longer applies repr() to querysets compared with strings

`django_2394866b35` · medium · confidence medium · introduced in 4.1 · fires at upgrade

TransactionTestCase.assertQuerysetEqual() no longer calls repr() on a queryset when compared to string values. Tests that compare a queryset to repr()-style strings can behave differently or fail after the upgrade to 4.1 or later.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where this behavior change was made as part of the removal of deprecated features. (confidence high, judge partially_supported)
  - dj_notes@4.1: "TransactionTestCase.assertQuerysetEqual() no longer calls repr() on a queryset when compared to string values."
  - dj_deprecation: "TransactionTestCase.assertQuerysetEqual() will no longer automatically call repr() on a queryset when compared to string values."
- **[required] api_usage** `present` `"assertQuerysetEqual"`: Test code calls assertQuerysetEqual() on a TransactionTestCase (or subclass such as TestCase) and compares a queryset to string values. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "TransactionTestCase.assertQuerysetEqual() no longer calls repr() on a queryset when compared to string values."
  - dj_deprecation: "TransactionTestCase.assertQuerysetEqual() will no longer automatically call repr() on a queryset when compared to string values."
  - ⚠ The text names TransactionTestCase only; it does not say whether subclasses such as TestCase are affected.
- **[required] behavior** `present` `"string values compared against a queryset"`: The comparison values are strings, such as repr() output like '<Model: name>', rather than model instances or other non-string values. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "when compared to string values"
- **[required] test_coverage** `present` `"assertQuerysetEqual compared against string values"`: The queryset is compared to string values, which previously relied on the automatic repr() call. (confidence medium, judge partially_supported)
  - dj_deprecation: "when compared to string values"

Actions:
- Search the test suite for assertQuerysetEqual() calls that compare against strings, especially repr()-style strings.
- Update such assertions to compare against the actual objects, or otherwise adjust the expected values to match the new behavior in 4.1 and later.
- Run the test suite on 4.2 and fix any assertQuerysetEqual() failures.
- Search tests for assertQuerysetEqual() calls that compare querysets to string values.
- Update such assertions so they no longer depend on the automatic repr() of the queryset, for example by comparing against model instances or values explicitly.

### RadioSelect and CheckboxSelectMultiple now render in <div> tags

`django_279f3f0fb3` · medium · confidence high · introduced in 4.0 · fires at upgrade

Starting in Django 4.0, RadioSelect and CheckboxSelectMultiple widgets render in <div> tags instead of the previous markup. Custom CSS, JavaScript, or tests that depend on the old HTML structure may break. The previous behavior can be restored by overriding the widget template with the appropriate template from Django 3.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where the widget rendering changed (3.2 -> 4.2). (confidence high, judge supported)
  - dj_notes@4.0: "RadioSelect and CheckboxSelectMultiple widgets are now rendered in <div> tags"
- **[alternative] api_usage** `present` `"RadioSelect"`: The application uses the RadioSelect or CheckboxSelectMultiple widgets in forms. (confidence high, judge supported)
  - dj_notes@4.0: "RadioSelect and CheckboxSelectMultiple widgets are now rendered in <div> tags"
- **[uncertain] behavior** `unknown` `"dependence on previous widget markup"`: The application relies on the previous rendered HTML structure of these widgets, for example in CSS, JavaScript, or HTML assertions in tests. (confidence low, judge partially_supported)
  - dj_notes@4.0: "If you need the previous behavior, override the widget template with the appropriate template from Django 3.2."
  - ⚠ The text does not describe the previous markup, so which CSS selectors or tests are affected is not stated.
- **[optional] configuration** `present` `"custom widget template override"`: The application already overrides the widget templates for these widgets, so it may not see the new rendering. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "override the widget template with the appropriate template from Django 3.2"
  - ⚠ The text does not name the specific template files to override.

Actions:
- Search for RadioSelect and CheckboxSelectMultiple usage and review the rendered HTML, CSS, JavaScript and tests that depend on it.
- If the previous behavior is needed, override the widget template with the appropriate template from Django 3.2.

### LogoutView.get_next_page() renamed to get_success_url()

`django_28dea81c2d` · medium · confidence medium · introduced in 4.1 · fires at first_use

The undocumented LogoutView.get_next_page() method is renamed to get_success_url() in 4.1. Code that calls or overrides get_next_page() on LogoutView or a subclass must use the new name. The release notes do not say whether the old name keeps working.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where LogoutView.get_next_page() is renamed to get_success_url(). (confidence high, judge supported)
  - dj_notes@4.1: "LogoutView.get_next_page() method is renamed to get_success_url()"
- **[required] api_usage** `present` `"get_next_page"`: The application calls or overrides LogoutView.get_next_page(), for example in a LogoutView subclass. (confidence medium, judge supported)
  - dj_notes@4.1: "The undocumented LogoutView.get_next_page() method is renamed to get_success_url()."
  - ⚠ The text does not say whether get_next_page() remains as an alias or is removed immediately, or what happens to overrides of the old name.
  - ⚠ The method is described as undocumented, so usage is likely rare.

Actions:
- Search the codebase for get_next_page usage on LogoutView or its subclasses.
- Rename overrides and calls of get_next_page() to get_success_url().
- Test the logout flow, including the redirect target after logout.

### assertHTMLEqual boolean-less attribute comparison change

`django_2f3baa8123` · medium · confidence medium · introduced in 4.0 · fires at upgrade

Starting in Django 4.0, assertHTMLEqual no longer treats a non-boolean attribute without a value as equal to an attribute with the same name and value. Tests that relied on the old equality may now fail.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where the assertHTMLEqual behavior change was introduced (3.2 -> 4.2). (confidence medium, judge partially_supported)
  - dj_notes@4.0: "assertHTMLEqual no longer considers a non-boolean attribute without a value equal to an attribute with the same name and value."
- **[required] test_coverage** `present` `"assertHTMLEqual"`: The test suite calls assertHTMLEqual. (confidence high, judge supported)
  - dj_notes@4.0: "assertHTMLEqual no longer considers a non-boolean attribute without a value equal to an attribute with the same name and value."
- **[required] behavior** `present` `"non-boolean attribute without a value compared to same-named attribute with value"`: Expected or actual HTML in assertHTMLEqual comparisons contains a non-boolean attribute without a value (e.g. valueless attribute) compared against the same attribute with a value. (confidence medium, judge supported)
  - dj_notes@4.0: "a non-boolean attribute without a value equal to an attribute with the same name and value"
  - ⚠ The text does not give an example of which attributes are considered non-boolean.

Actions:
- Search the test suite for assertHTMLEqual usages and run the tests on 4.2.
- Fix expected HTML in failing tests so valueless non-boolean attributes match the actual attribute values explicitly.

### jinja2 minimum version raised to 2.11.0

`django_350fba2684` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of jinja2 from 2.9.2 to 2.11.0. Deployments using Django's Jinja2 template backend with an older jinja2 version fall below the supported minimum.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raises the minimum supported jinja2 version. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of jinja2 is increased from 2.9.2 to 2.11.0."
- **[required] dependency** `less_than` `"2.11.0"`: The project installs jinja2 at a version lower than 2.11.0. (confidence medium, judge supported)
  - dj_notes@4.2: "The minimum supported version of jinja2 is increased from 2.9.2 to 2.11.0."
  - ⚠ The text does not state what happens with unsupported jinja2 versions (e.g. whether Django fails or only loses support).

Actions:
- Upgrade jinja2 to 2.11.0 or newer before or together with upgrading Django to 4.2.
- Check requirements files, lockfiles and constraints for pinned jinja2 versions below 2.11.0.

### asgiref minimum version raised to 3.6.0

`django_38a3f575e2` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of asgiref from 3.5.2 to 3.6.0. Deployments that pin or resolve asgiref below 3.6.0 are outside the supported range after upgrading.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raises the minimum supported asgiref version. (confidence medium, judge supported)
  - dj_notes@4.2: "The minimum supported version of asgiref is increased from 3.5.2 to 3.6.0."
  - dj_notes@4.0: "The minimum supported version of asgiref is increased from 3.3.2 to 3.4.1."
  - dj_notes@4.1: "The minimum supported version of asgiref is increased from 3.4.1 to 3.5.2."
  - ⚠ History: in 4.0, 'asgiref minimum version raised to 3.4.1' applied to the same symbol (asgiref); superseded by the 4.2 change (R2).
  - ⚠ History: in 4.1, 'asgiref minimum version raised to 3.5.2' applied to the same symbol (asgiref); superseded by the 4.2 change (R2).
- **[required] dependency** `less_than` `"3.6.0"`: The deployment has asgiref installed or pinned at a version lower than 3.6.0. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The minimum supported version of asgiref is increased from 3.5.2 to 3.6.0."
  - ⚠ The text does not state what specifically fails with an older asgiref, only that the minimum supported version increased.

Actions:
- Upgrade asgiref to 3.6.0 or later before or together with the Django 4.2 upgrade.
- Update pinned versions of asgiref in requirements files, lock files, and constraints files to >=3.6.0.

### Meta.constraints now checked during model validation

`django_3b5ed48e22` · medium · confidence high · introduced in 4.1 · fires at first_use

Check, unique, and exclusion constraints defined in Meta.constraints are now checked during model validation. Models with such constraints may now reject data during validation (e.g. in forms or full_clean) that was previously accepted at the validation stage and only failed, if at all, at the database level.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, which introduced constraint checking during model validation. (confidence high, judge supported)
  - dj_notes@4.1: "Check, unique, and exclusion constraints defined in the Meta.constraints option are now checked during model validation."
- **[required] api_usage** `present` `"constraints"`: The application defines check, unique, or exclusion constraints in a model's Meta.constraints option. (confidence high, judge supported)
  - dj_notes@4.1: "defined in the Meta.constraints option"
- **[uncertain] behavior** `present` `"full_clean"`: The application validates models, for example via full_clean() or ModelForm/admin validation, so the new constraint checks can surface as validation errors. (confidence low, judge partially_supported)
  - dj_notes@4.1: "are now checked during model validation"
  - ⚠ The text does not name the specific validation entry points (full_clean, ModelForm, admin) or the resulting error behavior.

Actions:
- Review models that define Meta.constraints and identify forms, serializers, or code calling full_clean() that will now validate those constraints.
- Run the test suite and exercise form/validation paths to detect new ValidationErrors from constraints.

### setUpTestData() class attributes that cannot be deep-copied

`django_3efaf434da` · medium · confidence high · introduced in 4.1 · fires at upgrade

Django 4.1 removes support for assigning objects that cannot be copied with copy.deepcopy() to class attributes in TestCase.setUpTestData(). Test classes that assign such non-deepcopy-able objects will no longer be supported after the upgrade crosses 4.1.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where support for non-deepcopy-able objects in setUpTestData() is removed. (confidence high, judge partially_supported)
  - dj_deprecation: "Support for assigning objects which don't support creating deep copies with copy.deepcopy() to class attributes in TestCase.setUpTestData() will be removed."
  - dj_notes@4.1: "Support for assigning objects which don't support creating deep copies with copy.deepcopy() to class attributes in TestCase.setUpTestData() is removed."
- **[required] test_coverage** `present` `"setUpTestData"`: Test code defines TestCase.setUpTestData() and assigns objects to class attributes in it. (confidence high, judge supported)
  - dj_deprecation: "class attributes in TestCase.setUpTestData()"
- **[required] behavior** `present` `"objects that do not support copy.deepcopy()"`: Objects assigned to class attributes in setUpTestData() do not support copy.deepcopy(). (confidence high, judge supported)
  - dj_deprecation: "objects which don't support creating deep copies with copy.deepcopy()"
  - dj_notes@4.1: "objects which don't support creating deep copies with copy.deepcopy()"
  - ⚠ The text does not state how the failure manifests once support is removed.
  - ⚠ The text does not state what failure occurs for such objects at 4.1+ (e.g. an error or a changed behavior).
- **[required] api_usage** `present` `"setUpTestData"`: Test code defines TestCase.setUpTestData() and assigns objects to class attributes in it. (confidence high, judge supported)
  - dj_notes@4.1: "class attributes in TestCase.setUpTestData()"

Actions:
- Review every TestCase.setUpTestData() and identify class attributes assigned objects that cannot be copied with copy.deepcopy().
- Change those tests so they do not assign non-deepcopy-able objects to class attributes in setUpTestData(), for example by creating such objects in setUp() instead.
- Review TestCase.setUpTestData() implementations and identify class attributes assigned objects that cannot be deep-copied with copy.deepcopy().
- Consult the deprecated-features-3.2 documentation referenced by the release notes for how to remove usage of this feature.

### blocktranslate asvar output now marked safe

`django_448b2e13b9` · medium · confidence high · introduced in 4.2 · fires at first_use

The result of {% blocktranslate asvar ... %} is now marked as safe for HTML output purposes. Templates that use asvar with blocktranslate will no longer have the variable autoescaped on output, which can change rendered HTML (and potentially introduce unescaped content if the translated block contains unsafe values).

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which introduced the changed blocktranslate asvar behavior. (confidence high, judge supported)
  - dj_notes@4.2: "{% blocktranslate asvar ... %} result is now marked as safe for (HTML) output purposes."
- **[required] api_usage** `present` `"blocktranslate asvar"`: Templates use the {% blocktranslate %} tag with the asvar option. (confidence high, judge supported)
  - dj_notes@4.2: "{% blocktranslate asvar ... %} result is now marked as safe for (HTML) output purposes."
- **[uncertain] behavior** `unknown` `"asvar variable rendered in HTML output"`: The asvar variable is output in HTML templates, where the new safe marking changes escaping behavior. (confidence low, judge partially_supported)
  - dj_notes@4.2: "{% blocktranslate asvar ... %} result is now marked as safe for (HTML) output purposes."
  - ⚠ The text does not state the previous escaping behavior or specific impact on rendered output.

Actions:
- Search templates for {% blocktranslate ... asvar ... %} usages and review where the resulting variable is rendered.
- Verify that translated content containing user-supplied or untrusted values is not rendered unescaped unintentionally, and update templates or tests that depend on the previous escaping behavior.

### DatabaseSchemaEditor._unique_sql() and _create_unique_sql() second argument changed from columns to fields

`django_48b5217f75` · medium · confidence medium · introduced in 4.0 · fires at first_use

In Django 4.0 the second argument of DatabaseSchemaEditor._unique_sql() and _create_unique_sql() is now fields instead of columns. Third-party database backends or custom schema editors that override or call these private methods and pass or expect columns will need to be updated.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the second argument of these methods changed from columns to fields. (confidence high, judge supported)
  - dj_notes@4.0: "The second argument of DatabaseSchemaEditor._unique_sql() and _create_unique_sql() methods is now fields instead of columns."
- **[required] api_usage** `present` `"_unique_sql or _create_unique_sql"`: The codebase (for example a custom or third-party database backend) overrides or calls DatabaseSchemaEditor._unique_sql() or _create_unique_sql(). (confidence medium, judge supported)
  - dj_notes@4.0: "The second argument of DatabaseSchemaEditor._unique_sql() and _create_unique_sql() methods is now fields instead of columns."
  - ⚠ The text does not state how the methods behave if called with columns instead of fields, so the failure mode is unknown.
- **[optional] dependency** `present` `"third-party database backend"`: The code is part of a third-party database backend, which is the audience the section addresses. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "This section describes changes that may be needed in third-party database backends."

Actions:
- Search custom or third-party database backends and schema editor subclasses for overrides or calls of _unique_sql() and _create_unique_sql().
- Update the second argument handling from columns to fields to match the Django 4.0 signature.
- Upgrade third-party database backend packages to versions that support Django 4.x.

### default_app_config variable removed

`django_48c3fd8caa` · medium · confidence high · introduced in 4.1 · fires at upgrade

The default_app_config application configuration variable is removed in Django 4.1. Apps that still define default_app_config (for example in an app's __init__.py) will no longer have it honored after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where default_app_config was removed. (confidence high, judge supported)
  - dj_notes@4.1: "The default_app_config application configuration variable is removed."
  - dj_deprecation: "The default_app_config module variable will be removed."
- **[required] api_usage** `present` `"default_app_config"`: The application or its installed apps define the default_app_config variable. (confidence high, judge supported)
  - dj_notes@4.1: "The default_app_config application configuration variable is removed."
  - dj_deprecation: "The default_app_config module variable will be removed."
  - ⚠ The text does not state what exactly happens to apps that still set default_app_config after removal, or how to replace it.
  - ⚠ The text does not state what happens to apps that still define default_app_config after removal, nor what replaces it.

Actions:
- Search the project and its first-party apps for default_app_config and remove the usages.
- Consult the Django 3.2 deprecation notes (deprecated-features-3.2) for details on how to remove usage of this variable, as the parent context refers to.
- Search the codebase and installed first-party apps for default_app_config and remove each definition before upgrading to 4.1 or later.
- Check the Django 3.2 release notes, referenced by the parent context, for details on this change.

### PostgreSQL auto fields created as identity columns instead of serial

`django_4c5ef340ee` · medium · confidence medium · introduced in 4.1 · fires at first_use

On PostgreSQL, AutoField, BigAutoField, and SmallAutoField columns are now created as identity columns rather than serial columns with sequences. Schemas created at 4.1 or later (new tables, test databases) differ from those created by earlier versions. Code, raw SQL, or tooling that relies on serial columns and their sequences may behave differently.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where the change to identity columns was introduced. (confidence high, judge supported)
  - dj_notes@4.1: "On PostgreSQL, AutoField, BigAutoField, and SmallAutoField are now created as identity columns rather than serial columns with sequences."
- **[required] database** `contains` `"django.db.backends.postgresql"`: The deployment uses PostgreSQL as a database backend. (confidence high, judge supported)
  - dj_notes@4.1: "On PostgreSQL, AutoField, BigAutoField, and SmallAutoField are now created as identity columns"
- **[required] api_usage** `present` `"AutoField|BigAutoField|SmallAutoField"`: The application uses AutoField, BigAutoField, or SmallAutoField, including via DEFAULT_AUTO_FIELD or implicit primary keys. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "AutoField, BigAutoField, and SmallAutoField are now created as identity columns"
  - ⚠ The text does not state whether existing columns or tables created by earlier versions are converted; it only says the fields are now created as identity columns.
- **[optional] behavior** `present` `"serial/sequence dependency"`: Application code, raw SQL, or tooling depends on serial columns or their sequences (for example, sequence names or pg_get_serial_sequence). (confidence low, judge partially_supported)
  - dj_notes@4.1: "rather than serial columns with sequences"
  - ⚠ The text does not state what specific behaviors differ for code relying on sequences.

Actions:
- Review raw SQL, migrations, and tooling that reference serial sequences on PostgreSQL auto fields.
- Check schemas created before and after the upgrade (including test databases) with information_schema.columns to see which columns are identity versus serial.
- Run the test suite against PostgreSQL after upgrading to verify behavior of auto-incrementing primary keys.

### Sliced queryset unsupported operations now raise TypeError instead of AssertionError

`django_51eedd8b4d` · medium · confidence low · introduced in 4.0 · fires at first_use

Unsupported operations on a sliced queryset now raise TypeError instead of AssertionError. Code that catches AssertionError (or tests asserting AssertionError) for such operations will no longer handle the exception after upgrading across 4.0.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where unsupported sliced-queryset operations raise TypeError instead of AssertionError. (confidence high, judge supported)
  - dj_notes@4.0: "Unsupported operations on a sliced queryset now raise TypeError instead of AssertionError."
- **[required] api_usage** `present` `"except AssertionError"`: The application performs operations on sliced querysets that are unsupported (e.g. filtering/ordering after slicing) and catches or asserts AssertionError for them. (confidence low, judge partially_supported)
  - dj_notes@4.0: "Unsupported operations on a sliced queryset now raise TypeError instead of AssertionError."
  - ⚠ The text does not list which operations on a sliced queryset are unsupported.

Actions:
- Replace handling of AssertionError for unsupported sliced queryset operations with TypeError.
- Update tests that expect AssertionError from sliced queryset operations to expect TypeError.

### ModelAdmin log_addition/log_change/log_deletion argument renamed to obj

`django_6a3932e55f` · medium · confidence medium · introduced in 4.0 · fires at first_use

The object argument of the undocumented ModelAdmin.log_addition(), log_change(), and log_deletion() methods is renamed to obj in 4.0. Code that overrides these methods using the old parameter name, or calls them with object as a keyword argument, will break.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where the argument was renamed. (confidence high, judge supported)
  - dj_notes@4.0: "The object argument of undocumented ModelAdmin.log_addition(), log_change(), and log_deletion() methods is renamed to obj."
- **[required] api_usage** `present` `"log_addition|log_change|log_deletion"`: The application overrides or calls ModelAdmin.log_addition(), log_change(), or log_deletion(), in particular using the object keyword argument or the object parameter name. (confidence medium, judge supported)
  - dj_notes@4.0: "The object argument of undocumented ModelAdmin.log_addition(), log_change(), and log_deletion() methods is renamed to obj."
  - ⚠ The text does not state what happens when the old keyword name object is passed; the breakage for keyword callers and for overrides with the old parameter name is inferred from the rename.

Actions:
- Rename the object parameter to obj in any ModelAdmin overrides of log_addition(), log_change(), and log_deletion().
- Update any callers that pass object as a keyword argument to use obj instead.

### Custom sitemap index templates need updating for adjusted context variables

`django_7414aaded0` · medium · confidence medium · introduced in 4.1 · fires at first_use

The default sitemap index template now includes <lastmod> through the new get_latest_lastmod method, and the context variables were adjusted. Custom sitemap index templates should be updated to match the adjusted context variables.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where the sitemap index template change was introduced. (confidence high)
  - dj_notes@4.1: "The default sitemap index template <sitemapindex> now includes the <lastmod> timestamp where available"
- **[required] api_usage** `present` `"sitemapindex"`: The application uses a custom sitemap index template (overriding the default sitemapindex template). (confidence medium, judge supported)
  - dj_notes@4.1: "Custom sitemap index templates should be updated for the adjusted context variables."
  - ⚠ The text does not state which context variables were adjusted or how they changed.

Actions:
- Find custom sitemap index templates (e.g. overrides of sitemap_index.xml or templates passed to the sitemap index view).
- Update them to use the adjusted context variables introduced in 4.1; consult the Django 4.1 sitemaps documentation for the new variables.
- Optionally use get_latest_lastmod to emit <lastmod> in the sitemap index.

### Custom Node.render() returning non-string values

`django_764dcc1de2` · medium · confidence medium · introduced in 4.0 · fires at first_use

NodeList.render() no longer casts the output of each node's render() method to a string. Custom template Node subclasses whose render() returns a non-string value (contrary to the documented contract) may no longer be handled as before.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where NodeList.render() stopped casting node output to a string. (confidence high, judge supported)
  - dj_notes@4.0: "NodeList.render() no longer casts the output of render() method for individual nodes to a string."
- **[required] api_usage** `present` `"Node.render()"`: The application defines custom template Node subclasses or tags whose render() method may return a non-string value. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Node.render() should always return a string as documented."
  - ⚠ The text does not state what specific failure occurs when render() returns a non-string value.

Actions:
- Audit all custom template Node subclasses and ensure render() always returns a string (e.g., wrap return values with str()).
- Run template rendering tests for custom template tags after upgrading.

### makemigrations --check no longer creates migration files

`django_782bade359` · medium · confidence medium · introduced in 4.2 · fires at first_use

In 4.2, the makemigrations --check option no longer creates missing migration files. Scripts, CI jobs or workflows that relied on makemigrations --check to also generate missing migrations will no longer get those files created.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where makemigrations --check stops creating missing migration files. (confidence high, judge supported)
  - dj_notes@4.2: "The makemigrations --check option no longer creates missing migration files."
- **[required] api_usage** `present` `"makemigrations --check"`: The project's scripts, CI configuration, or tooling invoke makemigrations with the --check option and rely on it to create missing migration files. (confidence medium, judge supported)
  - dj_notes@4.2: "The makemigrations --check option no longer creates missing migration files."
  - ⚠ The text does not say how users should create missing migrations instead; presumably running makemigrations without --check.

Actions:
- Search CI pipelines, Makefiles, pre-commit hooks and scripts for makemigrations --check usage.
- Do not rely on --check to generate migration files; run makemigrations without --check to create missing migrations and commit them.
- Treat makemigrations --check as a verification-only step (non-zero exit if migrations are missing) after upgrading.

### output_field no longer guessed for combined expressions and database functions with mixed types

`django_7a4215cfe6` · medium · confidence medium · introduced in 4.1 · fires at first_use

As of Django 4.1, combined expressions no longer guess output_field when argument types match. Resolving an output_field for database functions and combined expressions may now crash with mixed types, so output_field must be set explicitly in such cases.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where combined expressions stopped guessing output_field. (confidence high, judge supported)
  - dj_notes@4.1: "Combined expressions no longer use the error-prone behavior of guessing output_field when argument types match."
- **[required] api_usage** `present` `"output_field"`: The application uses combined expressions or database functions (for example F() arithmetic, Func, Value, Coalesce) whose source arguments have mixed types and do not set output_field explicitly. (confidence medium, judge supported)
  - dj_notes@4.1: "resolving an output_field for database functions and combined expressions may now crash with mixed types"
  - ⚠ The text does not list which specific functions or expressions are affected, only 'database functions and combined expressions' in general.
  - ⚠ The text does not say how to determine whether argument types are mixed; this requires inspecting the field types involved.
- **[disqualifying] api_usage** `present` `"output_field="`: The expression already sets output_field explicitly, in which case the crash does not apply. (confidence low, judge partially_supported)
  - dj_notes@4.1: "You will need to explicitly set the output_field in such cases."

Actions:
- Audit uses of combined expressions and database functions that mix field types and explicitly set output_field on them.
- Run the test suite covering ORM queries with annotations, aggregations and expressions to find crashes from unresolved output_field.

### USE_L10N default changed from False to True

`django_80d51ec58c` · medium · confidence low · introduced in 4.0 · fires at upgrade

The default value of USE_L10N changes from False to True in 4.0. Projects that do not set USE_L10N explicitly will begin localizing dates and numbers displayed by Django after upgrading. USE_L10N is also deprecated as of 4.0, and from Django 5.0 localization is on by default.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the USE_L10N default changed. (confidence high, judge supported)
  - dj_notes@4.0: "the default value of the USE_L10N setting is changed from False to True"
  - dj_notes@4.0: "The default value of the USE_L10N setting is changed to True."
- **[required] configuration** `absent` `"USE_L10N"`: The project does not set USE_L10N explicitly in its settings, so it relies on the old default of False. (confidence low, judge partially_supported)
  - dj_notes@4.0: "the default value of the USE_L10N setting is changed from False to True"
  - dj_notes@4.0: "The default value of the USE_L10N setting is changed to True."
  - ⚠ The text does not say outright what happens when USE_L10N is explicitly set; the conclusion that explicit settings are unaffected is inferred from the fact that the default changed.
  - ⚠ The text does not state explicitly that projects setting USE_L10N explicitly are unaffected; this is inferred from the nature of a default change.
- **[required] behavior** `present` `"date or number rendering by Django"`: The application displays dates or numbers through Django, for example in templates or forms, so that localization changes the rendered output. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "any date or number displayed by Django will be localized"
  - dj_notes@4.0: "See the Localization section above for more details."
  - ⚠ The text states this behavior for Django 5.0 by default and says the default changes in 4.0; it does not describe in detail what formatting differences appear at 4.2.
  - ⚠ The text does not describe what behavior changes when USE_L10N becomes True.
- **[optional] api_usage** `present` `"{% localize %}"`: The templates use the {% localize %} tag or the localize/unlocalize filters, which Django will still honor. (confidence high, judge supported)
  - dj_notes@4.0: "The {% localize %} tag and the localize/ unlocalize filters will still be honored by Django."

Actions:
- Search the settings for USE_L10N and, if the project does not set it, check whether localized dates and numbers are acceptable.
- If the previous non-localized output must be kept at 4.2, set USE_L10N = False explicitly, noting that the setting is deprecated as of 4.0.
- Plan for Django 5.0, where localization is on by default, by reviewing templates, forms and tests that depend on date or number formatting.
- Use the {% localize %} tag or the localize/unlocalize filters in templates to control localization where needed.
- Explicitly set USE_L10N in the project settings to the desired value, or review behavior under the new default of True.
- Consult the Localization section of the Django 4.0 release notes for details on affected behavior.

### DEFAULT_HASHING_ALGORITHM setting removed

`django_8683c043db` · medium · confidence high · introduced in 4.0 · fires at upgrade

The DEFAULT_HASHING_ALGORITHM transitional setting is removed in Django 4.0. Projects that still set it in their settings will have a setting that Django no longer reads, and code that references it directly (for example via django.conf.settings) may fail. The text does not say what happens to a leftover definition.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the DEFAULT_HASHING_ALGORITHM setting is removed. (confidence high, judge supported)
  - dj_notes@4.0: "The DEFAULT_HASHING_ALGORITHM transitional setting is removed."
  - dj_deprecation: "The DEFAULT_HASHING_ALGORITHM transitional setting will be removed."
- **[required] configuration** `present` `"DEFAULT_HASHING_ALGORITHM"`: The project settings or code define or reference DEFAULT_HASHING_ALGORITHM. (confidence high, judge supported)
  - dj_notes@4.0: "The DEFAULT_HASHING_ALGORITHM transitional setting is removed."
  - dj_deprecation: "The DEFAULT_HASHING_ALGORITHM transitional setting will be removed."
  - ⚠ The text does not state what happens to a leftover definition of the removed setting, or what the replacement behavior is.
  - ⚠ The text does not state what happens if the setting is still defined after removal, or which hashing algorithm applies instead.

Actions:
- Remove DEFAULT_HASHING_ALGORITHM from all settings modules and any code that references it before or during the upgrade to 4.0 or later.
- See the Django 3.1 deprecation and release notes for the transitional setting and its removal.
- Search settings modules and environment-specific settings for DEFAULT_HASHING_ALGORITHM and remove it before or during the upgrade to 4.x.

### Removed Query.where_class property

`django_86a937a5d8` · medium · confidence medium · introduced in 4.0 · fires at upgrade

The where_class property of django.db.models.sql.query.Query is removed in 4.0. Code accessing Query.where_class will break; the text says to initialize django.db.models.sql.where.WhereNode instead if needed.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the where_class property of Query was removed. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The where_class property of django.db.models.sql.query.Query"
- **[required] api_usage** `present` `"where_class"`: The application code accesses the where_class property of a Query object. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The where_class property of django.db.models.sql.query.Query"

Actions:
- Replace uses of Query.where_class by initializing django.db.models.sql.where.WhereNode directly.

### was_modified_since size argument removed

`django_8d968fb0a8` · medium · confidence high · introduced in 4.1 · fires at upgrade

The size argument of the undocumented django.views.static.was_modified_since() function is removed in Django 4.1. Code that calls this function and passes size will break when upgrading from 3.2 to 4.2. The function is undocumented, so direct usage is likely uncommon.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where the size argument was removed. (confidence high, judge supported)
  - dj_notes@4.1: "The size argument of the undocumented django.views.static.was_modified_since() function is removed."
- **[required] api_usage** `present` `"was_modified_since"`: The application calls django.views.static.was_modified_since() and passes the size argument. (confidence high, judge supported)
  - dj_notes@4.1: "The size argument of the undocumented django.views.static.was_modified_since() function is removed."

Actions:
- Search the codebase for calls to was_modified_since() and remove the size argument from them.
- Check for third-party or vendored code that calls django.views.static.was_modified_since() with size.

### EmailBackend now verifies hostname and certificates for TLS/SSL connections

`django_8f4e0280c3` · medium · confidence medium · introduced in 4.2 · fires at first_use

In Django 4.2, EmailBackend verifies a hostname and certificates. Deployments that rely on the previous, less restrictive behavior (for example servers with mismatched hostnames or untrusted certificates) may no longer be able to send email. The text states that the previous behavior can be restored by subclassing EmailBackend and overriding the ssl_context property, but this is not recommended.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where EmailBackend begins verifying a hostname and certificates. (confidence high, judge supported)
  - dj_notes@4.2: "EmailBackend now verifies a hostname and certificates."
- **[required] api_usage** `present` `"EmailBackend"`: The application uses EmailBackend to send email (the backend whose verification behavior changed). (confidence medium, judge supported)
  - dj_notes@4.2: "EmailBackend now verifies a hostname and certificates."
  - ⚠ The text does not state which EMAIL_BACKEND setting values or TLS/SSL settings trigger the verification, so it is unclear whether it applies only when TLS or SSL is enabled.
- **[uncertain] behavior** `unknown` `"previous less restrictive behavior required"`: The email server presents a hostname or certificate that does not pass verification, so the previous less restrictive behavior is needed. (confidence low, judge partially_supported)
  - dj_notes@4.2: "If you need the previous behavior that is less restrictive and not recommended"
  - ⚠ The text does not describe the specific failure mode or what counts as failing verification.
- **[optional] api_usage** `present` `"ssl_context"`: The application already subclasses EmailBackend and overrides ssl_context, in which case it controls its own verification behavior. (confidence low, judge partially_supported)
  - dj_notes@4.2: "subclass EmailBackend and override the ssl_context property"
  - ⚠ The text does not state whether an existing ssl_context override is unaffected by the change.

Actions:
- Verify that the SMTP server's hostname and certificate pass verification, and fix the server's certificate or hostname configuration if possible.
- If the previous less restrictive behavior is needed (not recommended), subclass EmailBackend and override the ssl_context property.
- Test sending email through the configured EmailBackend after upgrading to 4.2.

### Durable nested atomic in TestCase raises RuntimeError

`django_8fee78f055` · medium · confidence medium · introduced in 4.1 · fires at first_use

A nested atomic block marked as durable inside django.test.TestCase now raises a RuntimeError, the same as outside of tests. Tests that relied on the previous behavior inside TestCase will fail.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, which introduced the RuntimeError for nested durable atomic blocks in django.test.TestCase. (confidence high, judge supported)
  - dj_notes@4.1: "A nested atomic block marked as durable in django.test.TestCase now raises a RuntimeError, the same as outside of tests."
- **[required] api_usage** `present` `"durable=True"`: The application's tests use atomic blocks marked as durable that are nested inside another atomic block while running under django.test.TestCase. (confidence high, judge supported)
  - dj_notes@4.1: "A nested atomic block marked as durable in django.test.TestCase now raises a RuntimeError"
- **[required] test_coverage** `present` `"django.test.TestCase"`: Test classes subclass django.test.TestCase, which wraps each test in an atomic block, so durable atomic blocks used in the code under test become nested. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "A nested atomic block marked as durable in django.test.TestCase now raises a RuntimeError"

Actions:
- Search code and tests for atomic(durable=True) and @transaction.atomic(durable=True) usages exercised under django.test.TestCase.
- If tests fail with RuntimeError after upgrade, restructure the tests (e.g. use TransactionTestCase for code paths that use durable atomic blocks) or adjust the code so the durable block is not nested.

### Cached template loader enabled by default when DEBUG is True

`django_8ffa5d85a3` · medium · confidence medium · introduced in 4.1 · fires at upgrade

Starting in Django 4.1, the cached template loader is enabled in development (DEBUG True) when OPTIONS['loaders'] is not specified in TEMPLATES. Projects that relied on the previous default behavior may see different template loading behavior. The text states OPTIONS['loaders'] can be specified to override this.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, which introduced the change to enable the cached template loader in development. (confidence high, judge supported)
  - dj_notes@4.1: "The cached template loader is now enabled in development, when DEBUG is True, and OPTIONS['loaders'] isn't specified."
  - dj_notes@4.1: "the cached template loader is now enabled in development"
- **[required] configuration** `equals` `"DEBUG = True"`: The project runs with DEBUG set to True (e.g. in development). (confidence medium, judge supported)
  - dj_notes@4.1: "when DEBUG is True"
  - dj_notes@4.1: "You may specify OPTIONS['loaders'] to override this, if necessary."
  - ⚠ The text does not state the exact conditions (e.g. DEBUG or APP_DIRS settings) under which the previous default applied.
- **[required] configuration** `absent` `"loaders"`: The TEMPLATES setting does not specify OPTIONS['loaders']. (confidence high, judge supported)
  - dj_notes@4.1: "OPTIONS['loaders'] isn't specified"
- **[disqualifying] configuration** `present` `"OPTIONS['loaders']"`: The project explicitly sets OPTIONS['loaders'], which overrides the new default. (confidence high, judge supported)
  - dj_notes@4.1: "You may specify OPTIONS['loaders'] to override this, if necessary."

Actions:
- Check whether TEMPLATES in settings specifies OPTIONS['loaders']; if not, expect the cached template loader to be used in development when DEBUG is True.
- If the previous non-cached behavior is needed in development, specify OPTIONS['loaders'] explicitly to override the default.
- Review TEMPLATES settings for development and check whether the new cached loader behavior is acceptable.
- If the previous behavior is needed, specify OPTIONS['loaders'] explicitly to override the default.

### Custom database backend overrides year_lookup_bounds_for_date_field/year_lookup_bounds_for_datetime_field without iso_year argument

`django_905d3a6384` · medium · confidence medium · introduced in 4.0 · fires at first_use

In Django 4.0, DatabaseOperations.year_lookup_bounds_for_date_field() and year_lookup_bounds_for_datetime_field() take an optional iso_year argument to support bounds for ISO-8601 week-numbering years. Third-party or custom database backends that override these methods may need to be updated to accept the new argument.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which changed the signatures of these DatabaseOperations methods. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "methods now take the optional iso_year argument in order to support bounds for ISO-8601 week-numbering years"
- **[required] api_usage** `present` `"year_lookup_bounds_for_date_field"`: The project uses a third-party or custom database backend whose DatabaseOperations subclass defines or overrides year_lookup_bounds_for_date_field() or year_lookup_bounds_for_datetime_field(). (confidence medium, judge supported)
  - dj_notes@4.0: "DatabaseOperations.year_lookup_bounds_for_date_field() and year_lookup_bounds_for_datetime_field() methods now take the optional iso_year argument"
  - dj_notes@4.0: "This section describes changes that may be needed in third-party database backends."
  - ⚠ The text does not state the exact failure mode if an override lacks the iso_year parameter.
- **[uncertain] api_usage** `absent` `"year_lookup_bounds_for_date_field"`: The project uses only Django's built-in database backends and does not override or call these methods. (confidence low, judge not_supported)
  - dj_notes@4.0: "This section describes changes that may be needed in third-party database backends."
  - ⚠ Judge: evidence does not support this claim. The quote says only that third-party backends may need changes. It does not say that projects using only built-in backends, or projects that neither override nor call these methods, are unaffected. It also says nothing about whether a project calls the methods.

Actions:
- Update overrides of year_lookup_bounds_for_date_field() and year_lookup_bounds_for_datetime_field() in custom or third-party database backends to accept the optional iso_year argument.
- If using a third-party database backend, check that its release supports Django 4.2.

### Test runner non-zero exit code for unexpected successes with unittest.expectedFailure

`django_ab11d5f38a` · medium · confidence medium · introduced in 4.1 · fires at upgrade

Starting in Django 4.1, the Django test runner returns a non-zero error code for unexpected successes from tests marked with unittest.expectedFailure. A test suite that previously passed (exit code 0) despite such tests unexpectedly succeeding may now report failure, which can break CI pipelines that rely on the test runner exit code.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where the test runner exit code behavior changed (upgrading from 3.2 to 4.2). (confidence medium, judge partially_supported)
  - dj_notes@4.1: "The Django test runner now returns a non-zero error code for unexpected successes from tests marked with unittest.expectedFailure."
- **[required] test_coverage** `present` `"expectedFailure"`: The test suite contains tests marked with unittest.expectedFailure and is run with the Django test runner. (confidence high, judge supported)
  - dj_notes@4.1: "unexpected successes from tests marked with unittest.expectedFailure"
- **[required] behavior** `present` `"unexpected success"`: One or more tests marked with expectedFailure currently pass (unexpected success), for example because the underlying bug was fixed. (confidence high, judge supported)
  - dj_notes@4.1: "unexpected successes from tests marked with unittest.expectedFailure"
- **[optional] deployment** `present` `"manage.py test"`: CI or automation relies on the exit code of the Django test runner (manage.py test). (confidence low, judge partially_supported)
  - dj_notes@4.1: "The Django test runner now returns a non-zero error code"
  - ⚠ The text does not state how CI is configured; whether pipelines gate on the exit code must be checked in the deployment.

Actions:
- Search the test suite for unittest.expectedFailure usages and check whether any now pass unexpectedly.
- Remove the expectedFailure decorator from tests that now pass, or fix the tests so they behave as intended.
- Run the test suite under Django 4.2 and verify the exit code in CI.

### Reverse foreign key related manager on unsaved instances raises ValueError

`django_ab55437a82` · medium · confidence medium · introduced in 4.1 · fires at first_use

As of Django 4.1, calling a reverse foreign key related manager on an unsaved model instance raises ValueError, to unify behavior with many-to-many relations. Code that used reverse FK managers on unsaved objects will fail at runtime when it exercises that path.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where reverse foreign key related managers began raising ValueError for unsaved objects. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "a reverse foreign key now raises ValueError when calling related managers for unsaved objects"
- **[required] api_usage** `present` `"reverse foreign key related manager called on an unsaved model instance"`: The application accesses reverse foreign key related managers (e.g. <model>_set or a custom related_name) on model instances that have not yet been saved. (confidence medium, judge supported)
  - dj_notes@4.1: "calling related managers for unsaved objects"
  - ⚠ The text does not give the specific manager attribute names or methods affected; it says only 'related managers'.

Actions:
- Ensure model instances are saved before accessing reverse foreign key related managers.
- Search for code that uses reverse FK managers (<model>_set or related_name) on instances created but not yet saved, and reorder to call save() first.
- Add or run tests covering code paths that use related managers on newly created instances to catch ValueError.

### Meta.index_together deprecated in favor of Meta.indexes

`django_aeb030463f` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Meta.index_together is deprecated in favor of Meta.indexes. Moving existing index_together definitions to indexes must be handled as a migration: makemigrations generates a RenameIndex operation that renames the existing index. Historical migrations that contain index_together or AlterIndexTogether can be squashed. AlterIndexTogether is now officially supported only for pre-4.2 migration files and should not be used in new migrations.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where Meta.index_together is deprecated. (confidence high, judge supported)
  - dj_notes@4.2: "The Meta.index_together option is deprecated in favor of the indexes option"
  - dj_notes@4.2: "The Meta.index_together option is deprecated in favor of the indexes option."
- **[required] api_usage** `present` `"index_together"`: Models declare Meta.index_together. (confidence medium, judge supported)
  - dj_notes@4.2: "Migrating existing index_together should be handled as a migration"
  - ⚠ The provided text does not state the version in which index_together will be removed.
- **[optional] api_usage** `present` `"AlterIndexTogether"`: Existing migration files use the AlterIndexTogether operation, so squashing is advised and it must not be used in new migrations. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The AlterIndexTogether migration operation is now officially supported only for pre-Django 4.2 migration files"

Actions:
- Replace Meta.index_together with Meta.indexes = [models.Index(fields=[...])] on each affected model.
- Run makemigrations to generate a migration containing a RenameIndex operation that renames the existing index.
- Consider squashing migrations to remove index_together from historical migrations.
- Do not use AlterIndexTogether in new migrations; use AddIndex and RemoveIndex instead.
- Replace Meta.index_together with Meta.indexes using models.Index(fields=[...]).
- Run makemigrations to generate the migration for the change.

### Removed where_class argument of get_extra_restriction()

`django_af4dde81fe` · medium · confidence medium · introduced in 4.0 · fires at upgrade

The where_class argument to the private get_extra_restriction() method of ForeignObject and ForeignObjectRel is removed in 4.0. Custom subclasses overriding or callers invoking get_extra_restriction() with where_class will break; the text says to initialize WhereNode instead.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the where_class argument of get_extra_restriction() was removed. (confidence high, judge supported)
  - dj_notes@4.0: "the where_class argument to the private get_extra_restriction() method of ForeignObject and ForeignObjectRel are removed"
- **[required] api_usage** `present` `"get_extra_restriction"`: The application defines or calls get_extra_restriction() on ForeignObject or ForeignObjectRel (or subclasses) using a where_class argument. (confidence medium, judge supported)
  - dj_notes@4.0: "the where_class argument to the private get_extra_restriction() method of ForeignObject and ForeignObjectRel"
  - ⚠ The text does not state whether custom overrides of get_extra_restriction() are affected beyond the removed argument.

Actions:
- Update get_extra_restriction() overrides and calls to drop the where_class argument and initialize django.db.models.sql.where.WhereNode instead if needed.

### SECURE_BROWSER_XSS_FILTER setting removed and X-XSS-Protection header no longer set

`django_b236d7b436` · medium · confidence medium · introduced in 4.0 · fires at upgrade

Django 4.0 removes the SECURE_BROWSER_XSS_FILTER setting, and SecurityMiddleware no longer sets the X-XSS-Protection header. Projects that set the setting no longer get the header, and the header is not sent unless it is added through custom middleware. Legacy browsers that honor the header lose that protection.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which removes the SECURE_BROWSER_XSS_FILTER setting and stops SecurityMiddleware from setting X-XSS-Protection. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The SecurityMiddleware no longer sets the X-XSS-Protection header if the SECURE_BROWSER_XSS_FILTER setting is True."
- **[required] configuration** `present` `"SECURE_BROWSER_XSS_FILTER"`: The project settings define SECURE_BROWSER_XSS_FILTER, which is removed in 4.0. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The setting is removed."
- **[required] configuration** `contains` `"django.middleware.security.SecurityMiddleware"`: The project uses SecurityMiddleware, which previously set the X-XSS-Protection header. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The SecurityMiddleware no longer sets the X-XSS-Protection header"
- **[optional] behavior** `present` `"X-XSS-Protection"`: The deployment must support legacy browsers that honor the X-XSS-Protection header. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "If you want to support legacy browsers and set the header"

Actions:
- Remove SECURE_BROWSER_XSS_FILTER from settings.
- Use Content-Security-Policy without allowing 'unsafe-inline' scripts instead of relying on X-XSS-Protection.
- If legacy browser support is required, add a custom middleware that runs response.headers.setdefault("X-XSS-Protection", "1; mode=block").

### argon2-cffi minimum version raised to 19.2.0

`django_b86ee766cf` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of argon2-cffi from 19.1.0 to 19.2.0. Deployments that have argon2-cffi installed at a version older than 19.2.0 (for example, for Argon2 password hashing) fall below the supported minimum after upgrading.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raises the minimum supported argon2-cffi version. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of argon2-cffi is increased from 19.1.0 to 19.2.0."
- **[required] dependency** `less_than` `"19.2.0"`: The project or deployment has argon2-cffi installed at a version below 19.2.0. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The minimum supported version of argon2-cffi is increased from 19.1.0 to 19.2.0."
  - ⚠ The text does not state how Django behaves with an unsupported argon2-cffi version, only that the minimum supported version is raised.

Actions:
- Upgrade argon2-cffi to 19.2.0 or newer before or together with upgrading to Django 4.2.
- Update dependency pins or requirements files that specify argon2-cffi below 19.2.0.

### Pre-Django 3.1 session encoding format support removed in 4.0

`django_c1af6215cc` · medium · confidence high · introduced in 4.0 · fires at upgrade

Support for the pre-Django 3.1 encoding format of sessions is removed in Django 4.0. Sessions still stored in the old encoding format may no longer be decoded after upgrading from 3.2 to 4.2. The text does not state what happens to such sessions.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where support for the pre-Django 3.1 session encoding format is removed. (confidence high, judge partially_supported)
  - dj_deprecation: "Support for the pre-Django 3.1 encoding format of sessions will be removed."
  - dj_notes@4.0: "Support for the pre-Django 3.1 encoding format of sessions is removed."
- **[required] behavior** `present` `"pre-Django 3.1 encoding format of sessions"`: The application or deployment has sessions stored or encoded in the pre-Django 3.1 session encoding format. (confidence high, judge supported)
  - dj_deprecation: "Support for the pre-Django 3.1 encoding format of sessions will be removed."
  - dj_notes@4.0: "Support for the pre-Django 3.1 encoding format of sessions is removed."
  - ⚠ The text does not state how to detect old-format sessions or what happens when they are read after removal.
  - ⚠ The text does not state how to identify sessions in the old format or what happens to them after the upgrade.
- **[disqualifying] behavior** `absent` `"sessions in pre-Django 3.1 encoding format"`: Sessions in the old format are all expired or were re-created under Django 3.1 or later before the upgrade, so none remain in the pre-3.1 format. (confidence low)
  - dj_deprecation: "Support for the pre-Django 3.1 encoding format of sessions will be removed."
  - ⚠ The text does not explicitly describe this mitigation; it follows from the removed support being specific to the pre-3.1 format.

Actions:
- Check whether any stored sessions were created under a Django version before 3.1 and are still in use.
- Ensure sessions in the old encoding format have expired or been re-created under Django 3.1 or later before upgrading to 4.x.
- Expect users with old-format sessions to possibly need to log in again after the upgrade.
- Check whether the deployment still holds sessions created before Django 3.1 and plan for those sessions no longer being supported after the upgrade.
- See deprecated-features-3.1 for details on this change, including how to remove usage of the removed support.

### Manually instantiated WSGIRequest requires file-like wsgi.input

`django_d556e0f842` · medium · confidence low · introduced in 4.2 · fires at first_use

In Django 4.2, manually instantiated WSGIRequest objects must be given a file-like object for wsgi.input, as the WSGI specification expects. Previously Django was more lax, so code or tests that pass a non-file-like value for wsgi.input may break.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which introduced the stricter wsgi.input requirement for WSGIRequest. (confidence high, judge supported)
  - dj_notes@4.2: "Manually instantiated WSGIRequest objects must be provided a file-like object for wsgi.input."
- **[required] api_usage** `present` `"WSGIRequest("`: The application or its tests manually instantiate WSGIRequest objects. (confidence high, judge supported)
  - dj_notes@4.2: "Manually instantiated WSGIRequest objects must be provided a file-like object for wsgi.input."
- **[required] behavior** `present` `"wsgi.input"`: The environ passed to WSGIRequest sets wsgi.input to something that is not a file-like object, for example a string, bytes or None. (confidence low, judge partially_supported)
  - dj_notes@4.2: "Previously, Django was more lax than the expected behavior as specified by the WSGI specification."
  - ⚠ The text does not state exactly which non-file-like values previously worked or how the failure appears.

Actions:
- Find every place that manually builds a WSGIRequest, including test helpers and custom handlers or middleware tests.
- Make sure each environ's wsgi.input is a file-like object, such as io.BytesIO(body), rather than a raw string, bytes or None.
- Run the test suite after upgrading to catch manual WSGIRequest construction that previously passed.

### UserCreationForm rejects case-insensitive duplicate usernames

`django_d8509a5a51` · medium · confidence high · introduced in 4.2 · fires at first_use

Starting in Django 4.2, UserCreationForm rejects usernames that differ only in case from existing usernames. Applications relying on the previous behavior (allowing case-variant usernames) will see new validation failures at signup; BaseUserCreationForm restores the previous behavior.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, which introduced the stricter UserCreationForm username validation. (confidence high, judge supported)
  - dj_notes@4.2: "UserCreationForm now rejects usernames that differ only in case."
- **[required] api_usage** `present` `"UserCreationForm"`: The application uses UserCreationForm (directly or via subclass) to create user accounts. (confidence high, judge supported)
  - dj_notes@4.2: "UserCreationForm now rejects usernames that differ only in case."
- **[optional] behavior** `present` `"case-variant usernames allowed"`: The application relies on being able to register usernames that differ only in case (previous behavior). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "If you need the previous behavior, use BaseUserCreationForm instead."
- **[disqualifying] api_usage** `present` `"BaseUserCreationForm"`: The application already uses BaseUserCreationForm instead of UserCreationForm for the previous behavior. (confidence low, judge partially_supported)
  - dj_notes@4.2: "use BaseUserCreationForm instead"

Actions:
- Search the codebase for UserCreationForm usages and subclasses.
- If case-variant usernames must remain allowed, switch to BaseUserCreationForm.
- Otherwise, test signup flows to confirm the new case-insensitive uniqueness validation is acceptable.

### set_language() no longer stores user language in request.session

`django_e8dd99cb1e` · medium · confidence low · introduced in 4.0 · fires at first_use

As of Django 4.0, django.views.i18n.set_language() no longer sets the user language in request.session under the key _language. Code that relies on the session key being populated by set_language() will no longer find it. The text does not state where the language is stored instead.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where this behavior was removed. (confidence high, judge supported)
  - dj_notes@4.0: "django.views.i18n.set_language() doesn't set the user language in request.session (key _language)."
  - dj_deprecation: "django.views.i18n.set_language() will no longer set the user language in request.session"
- **[required] api_usage** `present` `"set_language"`: The application uses the django.views.i18n.set_language view (e.g. in URL configuration). (confidence high, judge supported)
  - dj_notes@4.0: "django.views.i18n.set_language() doesn't set the user language in request.session (key _language)."
  - dj_deprecation: "django.views.i18n.set_language() will no longer set the user language in request.session"
  - dj_deprecation: "key django.utils.translation.LANGUAGE_SESSION_KEY"
  - ⚠ The text does not state what mechanism replaces the session key for storing the language.
- **[required] api_usage** `present` `"_language"`: The application code reads the _language key from request.session to get the user language. (confidence low, judge partially_supported)
  - dj_notes@4.0: "doesn't set the user language in request.session (key _language)"
  - ⚠ The text does not state which mechanism replaces the session key for storing the language, nor whether other code depends on the session key.

Actions:
- Audit code that reads request.session['_language'] (or LANGUAGE_SESSION_KEY) and stop relying on set_language() populating it.
- See the Django 3.0 deprecation notes (deprecated-features-3.0) for details on removing usage of this behavior.
- Search the codebase for uses of set_language() and LANGUAGE_SESSION_KEY.
- Remove or replace any code that expects the user language to be stored in request.session after set_language() is called.
- Test language switching end to end after upgrading.

### Pillow minimum version raised to 6.2.1

`django_ecd275c5ed` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of Pillow from 6.2.0 to 6.2.1. Deployments that have Pillow installed at 6.2.0 are below the new minimum supported version.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raised the minimum supported Pillow version. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of Pillow is increased from 6.2.0 to 6.2.1."
- **[required] dependency** `less_than` `"6.2.1"`: The environment has Pillow installed at a version below 6.2.1. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The minimum supported version of Pillow is increased from 6.2.0 to 6.2.1."
  - ⚠ The text does not state what happens when an unsupported Pillow version is used.
- **[optional] api_usage** `present` `"ImageField"`: The application uses Pillow-dependent Django features such as ImageField. (confidence low, judge partially_supported)
  - dj_notes@4.2: "The minimum supported version of Pillow is increased from 6.2.0 to 6.2.1."
  - ⚠ The text does not name which Django features depend on Pillow.

Actions:
- Upgrade Pillow to 6.2.1 or newer before or together with upgrading Django to 4.2.
- Update pinned Pillow versions in requirements files or lockfiles.

### OpenLayers widget map_css block removed and inline CSS dropped

`django_f332589611` · medium · confidence low · introduced in 4.2 · fires at upgrade

The OpenLayers template widget no longer includes inline CSS, which also removes the former map_css template block. Custom widget templates that extend the OpenLayers template and override map_css will no longer have that block rendered, and map styling that relied on the inline CSS must be provided elsewhere (e.g. via static CSS).

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where the OpenLayers template widget no longer includes inline CSS and the map_css block is removed. (confidence high, judge supported)
  - dj_notes@4.2: "The OpenLayers template widget no longer includes inline CSS (which also removes the former map_css block)"
- **[alternative] api_usage** `present` `"map_css"`: The application overrides or extends the OpenLayers widget template and uses the map_css block. (confidence low, judge supported)
  - dj_notes@4.2: "which also removes the former map_css block"
  - ⚠ The text does not state what happens to templates that still override map_css (e.g. silently ignored).
- **[alternative] api_usage** `present` `"OpenLayersWidget"`: The application uses the OpenLayers widget (OpenLayersWidget / OpenLayers template widget) and relies on its inline CSS for map styling. (confidence medium, judge supported)
  - dj_notes@4.2: "The OpenLayers template widget no longer includes inline CSS"
  - ⚠ The text does not state which styles were removed or whether the widget still renders acceptably without them.

Actions:
- Search custom templates for overrides of the map_css block and move any needed styles into static CSS files or another template block.
- Check rendered OpenLayers maps (admin and forms) after upgrading and supply any needed CSS via static files.
- Review Content Security Policy configuration, since inline CSS is no longer emitted by the widget.

### sqlparse minimum version raised to 0.3.1

`django_f751ebde09` · medium · confidence medium · introduced in 4.2 · fires at upgrade

Django 4.2 raises the minimum supported version of sqlparse from 0.2.2 to 0.3.1. A deployment that has sqlparse installed at a version older than 0.3.1 is below the supported minimum and needs sqlparse upgraded.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which raises the minimum supported sqlparse version. (confidence high, judge supported)
  - dj_notes@4.2: "The minimum supported version of sqlparse is increased from 0.2.2 to 0.3.1."
- **[required] dependency** `less_than` `"0.3.1"`: The deployment has sqlparse installed at a version lower than 0.3.1. (confidence medium, judge supported)
  - dj_notes@4.2: "The minimum supported version of sqlparse is increased from 0.2.2 to 0.3.1."
  - ⚠ The text does not state what specifically fails when an unsupported sqlparse version is used.

Actions:
- Upgrade sqlparse to version 0.3.1 or later before or together with the Django 4.2 upgrade.
- Check requirements files, lock files and constraints for pins of sqlparse below 0.3.1 and update them.

### pytz normalize()/localize() usage with non-UTC time zones under the zoneinfo default

`django_fc188b2194` · medium · confidence high · introduced in 4.0 · fires at upgrade

Django 4.0 makes zoneinfo the default timezone implementation instead of pytz. The change is described as largely transparent, but code that works with non-UTC time zones and uses the pytz normalize() and localize() APIs must be audited, because pytz and zoneinfo are not entirely equivalent. The transitional USE_DEPRECATED_PYTZ setting allows continued use of pytz during the 4.x cycle and will be removed in Django 5.0.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where zoneinfo became the default timezone implementation. (confidence high, judge supported)
  - dj_notes@4.0: "Django 4.0 makes zoneinfo the default implementation."
- **[required] api_usage** `present` `"normalize()/localize()"`: The application uses the pytz normalize() and localize() APIs. (confidence high, judge supported)
  - dj_notes@4.0: "using the pytz normalize() and localize() APIs"
- **[required] behavior** `present` `"non-UTC time zones"`: The application works with non-UTC time zones. (confidence high, judge supported)
  - dj_notes@4.0: "if you are working with non-UTC time zones"
- **[optional] configuration** `present` `"TIME_ZONE"`: The TIME_ZONE setting is possibly involved in the pytz usage. (confidence medium, judge supported)
  - dj_notes@4.0: "possibly with the TIME_ZONE setting"
  - ⚠ The text does not state which TIME_ZONE values are affected.
- **[disqualifying] configuration** `equals` `"True"`: USE_DEPRECATED_PYTZ is enabled, which allows continued use of pytz during 4.x and so defers the audit. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "the transitional USE_DEPRECATED_PYTZ setting allows continued use of pytz during the 4.x release cycle"
  - ⚠ The text does not explicitly state the value to set; True is the natural enabling value.

Actions:
- Audit code that uses pytz normalize() and localize() with non-UTC time zones, and migrate it to the zoneinfo APIs.
- Set USE_DEPRECATED_PYTZ to True as a transitional measure if time is needed for the audit; it is available only during the 4.x release cycle and will be removed in Django 5.0.
- Consider using the pytz_deprecation_shim package to help migrate away from pytz.

### Admin inline formset:added/formset:removed events no longer jQuery events

`django_fe4f42e3e7` · medium · confidence medium · introduced in 4.1 · fires at first_use

The formset:added and formset:removed admin JavaScript events are now pure JavaScript events that do not depend on jQuery. Custom admin JavaScript that listens to these events using jQuery handlers may be affected and should be adapted per the admin-javascript-inline-form-events documentation.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where the events became pure JavaScript events (upgrading from 3.2 to 4.2). (confidence high, judge supported)
  - dj_notes@4.1: "formset:added and formset:removed JavaScript events are now pure JavaScript events and don't depend on jQuery."
- **[required] api_usage** `present` `"formset:added|formset:removed"`: The application has custom JavaScript (e.g. in admin templates or media) that handles the formset:added or formset:removed events. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "formset:added and formset:removed JavaScript events are now pure JavaScript events"
  - ⚠ The text does not state exactly how existing jQuery-based listeners behave after the change; it only points to admin-javascript-inline-form-events for details.

Actions:
- Search project JavaScript and admin templates for formset:added and formset:removed listeners.
- Consult admin-javascript-inline-form-events in the Django documentation and update handlers to use pure JavaScript event listeners (e.g. addEventListener) instead of jQuery-bound handlers.

### floatformat filter always localizes output regardless of USE_L10N

`django_ff4e75de71` · medium · confidence high · introduced in 4.0 · fires at upgrade

The floatformat template filter no longer depends on the USE_L10N setting and always returns localized output. Templates using floatformat with USE_L10N disabled (or relying on non-localized output) may render numbers differently; the u suffix disables localization.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the floatformat behavior changed. (confidence high, judge supported)
  - dj_notes@4.0: "The floatformat template filter no longer depends on the USE_L10N setting and always returns localized output."
- **[required] api_usage** `present` `"floatformat"`: Templates (or code calling the filter) use the floatformat template filter. (confidence high, judge supported)
  - dj_notes@4.0: "The floatformat template filter no longer depends on the USE_L10N setting"
- **[optional] configuration** `equals` `"USE_L10N = False"`: The project sets USE_L10N to False, so floatformat previously produced non-localized output that will now be localized. (confidence low, judge partially_supported)
  - dj_notes@4.0: "no longer depends on the USE_L10N setting and always returns localized output"
  - ⚠ The text does not explicitly state the previous behavior for each USE_L10N value or the default in 3.2.

Actions:
- Audit templates that use the floatformat filter and check whether output must remain non-localized.
- Append the u suffix to the floatformat argument (e.g. floatformat:"2u") where localization must be disabled.
- Update tests or fixtures that assert on floatformat-rendered numbers.

### CookieStorage pre-3.2 message format support removed

`django_ffb36c7ea4` · medium · confidence high · introduced in 4.1 · fires at upgrade

Django 4.1 removes support for the pre-Django 3.2 format of messages used by django.contrib.messages.storage.cookie.CookieStorage. Applications using CookieStorage could be affected if messages in the old format are still present, for example in cookies set before 3.2. The text does not state the exact failure mode.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where support for the pre-3.2 CookieStorage message format is removed. (confidence high, judge supported)
  - dj_notes@4.1: "Support for the pre-Django 3.2 format of messages used by django.contrib.messages.storage.cookie.CookieStorage is removed."
  - dj_deprecation: "Support for the pre-Django 3.2 format of messages used by django.contrib.messages.storage.cookie.CookieStorage will be removed."
- **[required] configuration** `present` `"django.contrib.messages.storage.cookie.CookieStorage"`: The application uses django.contrib.messages.storage.cookie.CookieStorage as its message storage backend. (confidence high, judge supported)
  - dj_notes@4.1: "django.contrib.messages.storage.cookie.CookieStorage"
  - dj_deprecation: "django.contrib.messages.storage.cookie.CookieStorage"
  - ⚠ The text does not say whether CookieStorage must be explicitly configured or if the default FallbackStorage, which uses it, is also affected.
  - ⚠ The text does not state whether other storage backends such as FallbackStorage, which may use CookieStorage internally, are affected.
- **[uncertain] behavior** `unknown` `"messages in pre-3.2 cookie format present"`: Messages stored in the pre-Django 3.2 format may still exist, such as in cookies created before 3.2 and still unexpired. (confidence low, judge partially_supported)
  - dj_notes@4.1: "Support for the pre-Django 3.2 format of messages used by django.contrib.messages.storage.cookie.CookieStorage is removed."
  - dj_deprecation: "Support for the pre-Django 3.2 format of messages"
  - ⚠ The text does not state what happens to messages in the old format after removal.
  - ⚠ The text does not state the exact runtime consequence for old-format messages, such as whether they are dropped or raise errors.

Actions:
- Check whether the project uses CookieStorage as its message storage backend.
- Because the project is on 3.2 or later, messages are written in the new format, so verify that no long-lived pre-3.2 format message cookies remain.
- See deprecated-features-3.2 for details on this change, as referenced in the release notes.
- Check whether the project uses CookieStorage, directly or via MESSAGE_STORAGE.
- Since the project is on 3.2, the messages format is already the 3.2 one; ensure no messages in the pre-3.2 cookie format are expected to be read after the upgrade.
- Test message display across the upgrade for users with existing cookies.

### GZipMiddleware gzip response output now includes random bytes

`django_0190ffdbe6` · low · confidence high · introduced in 4.2 · fires at upgrade

GZipMiddleware now adds up to 100 random bytes to gzip responses as BREACH mitigation, so compressed output is no longer deterministic or byte-identical across identical responses and sizes may vary.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django release 4.2, which introduced the GZipMiddleware BREACH mitigation. (confidence high, judge supported)
  - dj_notes@4.2: "GZipMiddleware now includes a mitigation for the BREACH attack."
- **[required] api_usage** `present` `"GZipMiddleware"`: The application uses GZipMiddleware to gzip responses. (confidence high, judge supported)
  - dj_notes@4.2: "GZipMiddleware now includes a mitigation for the BREACH attack."
- **[optional] behavior** `unknown` `"deterministic gzip output"`: Code, tests, caches or clients depend on gzip response bytes or length being deterministic. (confidence low, judge partially_supported)
  - dj_notes@4.2: "It will add up to 100 random bytes to gzip responses to make BREACH attacks harder."
  - ⚠ The text does not state that any particular consumer depends on deterministic output.

Actions:
- Review tests or logic that compare gzip-compressed response bodies or sizes byte for byte and make them compare decompressed content instead.
- Be aware that gzip responses may be up to 100 bytes larger due to the BREACH mitigation.

### inspectdb CharField uses display_size from get_table_description()

`django_07f3f1dcee` · low · confidence medium · introduced in 4.2 · fires at first_use

inspectdb now takes the CharField size from display_size returned by DatabaseIntrospection.get_table_description() instead of internal_size. Third-party database backends that implement or override get_table_description() may need changes so display_size holds the correct value, otherwise inspectdb-generated CharField definitions may differ.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where inspectdb switched from internal_size to display_size for CharField. (confidence high, judge supported)
  - dj_notes@4.2: "inspectdb now uses display_size from DatabaseIntrospection.get_table_description() rather than internal_size for CharField."
- **[required] dependency** `present` `"DatabaseIntrospection.get_table_description"`: The project uses a third-party database backend that provides its own DatabaseIntrospection.get_table_description(). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "This section describes changes that may be needed in third-party database backends."
  - ⚠ The text does not state exactly what a backend must do beyond populating display_size, nor which backends are affected.
- **[required] api_usage** `present` `"inspectdb"`: The project runs inspectdb to generate models, so the CharField sizes it produces are affected. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "inspectdb now uses display_size from DatabaseIntrospection.get_table_description()"

Actions:
- If you maintain or use a third-party database backend, ensure DatabaseIntrospection.get_table_description() returns the correct display_size for character columns.
- Re-run inspectdb after the upgrade and review the generated CharField max_length values.

### Third-party database backend minimum_database_version requires get_database_version and super() call in init_connection_state

`django_0880a6fa66` · low · confidence medium · introduced in 4.1 · fires at first_use

Django 4.1 lets third-party database backends declare DatabaseFeatures.minimum_database_version. If a backend specifies a minimum version, it must also implement DatabaseWrapper.get_database_version(), and its DatabaseWrapper.init_connection_state() must call super() for the version check to run. This affects only custom or third-party backends that adopt this attribute; otherwise the check does not run.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, which introduced the minimum_database_version attribute for third-party backends. (confidence high, judge supported)
  - dj_notes@4.1: "Third-party database backends can now specify the minimum required version of the database using the DatabaseFeatures.minimum_database_version attribute"
- **[required] api_usage** `present` `"minimum_database_version"`: The project ships or uses a third-party/custom database backend that sets DatabaseFeatures.minimum_database_version. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "DatabaseFeatures.minimum_database_version attribute which is a tuple"
- **[required] api_usage** `absent` `"get_database_version"`: The backend's DatabaseWrapper does not implement get_database_version() returning a tuple of the current database version. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "backends must also implement DatabaseWrapper.get_database_version(), which returns a tuple of the current database version"
  - ⚠ The text does not state what happens if get_database_version() is missing.
- **[alternative] api_usage** `absent` `"super().init_connection_state()"`: The backend's DatabaseWrapper.init_connection_state() does not call super(), so the version check will not run. (confidence high, judge supported)
  - dj_notes@4.1: "The backend's DatabaseWrapper.init_connection_state() method must call super() in order for the check to run."

Actions:
- If the third-party backend sets DatabaseFeatures.minimum_database_version, implement DatabaseWrapper.get_database_version() returning a tuple of the current database version.
- Ensure DatabaseWrapper.init_connection_state() calls super() so the minimum version check runs.
- If the backend does not define minimum_database_version, no action is required.

### InlineAdminFormSet.non_form_errors property replaced by method

`django_0dc5985384` · low · confidence medium · introduced in 4.1 · fires at first_use

The undocumented InlineAdminFormSet.non_form_errors property is replaced by the non_form_errors() method, consistent with BaseFormSet. Code that accesses it as a property (for example in custom admin templates or code) must now call it as a method.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, which replaced the InlineAdminFormSet.non_form_errors property with a method. (confidence high, judge supported)
  - dj_notes@4.1: "The undocumented InlineAdminFormSet.non_form_errors property is replaced by the non_form_errors() method."
- **[required] api_usage** `present` `"non_form_errors"`: The application accesses InlineAdminFormSet.non_form_errors as a property (e.g. in custom admin templates or Python code). (confidence medium, judge supported)
  - dj_notes@4.1: "The undocumented InlineAdminFormSet.non_form_errors property is replaced by the non_form_errors() method."
  - ⚠ The text does not state exactly how the old property usage fails, e.g. in templates versus Python code.

Actions:
- Search for uses of InlineAdminFormSet.non_form_errors (including custom admin templates and subclasses) and update them to call non_form_errors() as a method, consistent with BaseFormSet.

### JSON-encoded string literals passed via Value() to JSONField

`django_0e37c20feb` · low · confidence medium · introduced in 4.2 · fires at future_removal

JSONField and its lookups used to accept JSON-encoded string literals such as Value("null"), Value("[]") or Value('"foo-bar"'). During the 4.2 deprecation period Django tries to JSON-decode such string literals and emits a warning if decoding succeeds. From Django 5.1 string literals will be implicitly interpreted as JSON string literals, which changes their meaning.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where passing encoded JSON string literals is deprecated (current version below 4.2). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "During the deprecation period string literals will be attempted to be JSON decoded"
  - dj_notes@4.2: "From Django 5.1+ string literals will be implicitly interpreted as JSON string literals."
- **[required] api_usage** `present` `"Value(\"<JSON-encoded string>\") assigned to a JSONField"`: The application passes JSON-encoded string literals wrapped in Value() to a JSONField, for example in bulk_create, create or update. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "Document.objects.bulk_create( Document(data=Value("null")), Document(data=Value("[]")),"
  - dj_notes@4.2: "JSONField and its associated lookups and aggregates used to allow passing JSON encoded string literals"
  - dj_notes@4.2: "Document(data=Value(None, JSONField())), Document(data=[]), Document(data="foo-bar"),"
  - ⚠ The text shows bulk_create examples but does not say which other operations are affected beyond 'lookups and aggregates'.

Actions:
- Replace Value("null") with Value(None, JSONField()).
- Replace Value("[]") with the plain Python value [].
- Replace Value('"foo-bar"') with the plain Python string "foo-bar".
- Run tests with deprecation warnings enabled to find remaining encoded string literals.
- Replace Value("[]") with [] and Value('"foo-bar"') with "foo-bar".
- Replace JSONBAgg default=Value("[]") with default=[].
- Watch for the deprecation warning emitted when encoded string literals are JSON decoded successfully.

### ManifestStaticFilesStorage rewrites JavaScript source map references

`django_1163fb83c9` · low · confidence medium · introduced in 4.0 · fires at first_use

As of Django 4.0, ManifestStaticFilesStorage replaces paths to JavaScript source map references with their hashed counterparts. Projects on 3.2 that use this storage will see different processed static file output after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0 (3.2 -> 4.2), where ManifestStaticFilesStorage began replacing source map paths with hashed counterparts. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "ManifestStaticFilesStorage now replaces paths to JavaScript source map references with their hashed counterparts."
- **[required] api_usage** `present` `"ManifestStaticFilesStorage"`: The application or deployment uses ManifestStaticFilesStorage as its static files storage. (confidence high, judge supported)
  - dj_notes@4.0: "ManifestStaticFilesStorage now replaces paths to JavaScript source map references"
- **[optional] behavior** `present` `"sourceMappingURL"`: The collected static JavaScript files contain source map references that are now rewritten to hashed paths. (confidence low, judge supported)
  - dj_notes@4.0: "replaces paths to JavaScript source map references with their hashed counterparts"
  - ⚠ The text does not say what happens when a referenced source map file is missing or how the rewriting affects output files.

Actions:
- After upgrading, run collectstatic with ManifestStaticFilesStorage and verify that JavaScript files and their source map references resolve to the hashed file names.
- Check that the staticfiles manifest and the served JavaScript and source map files are consistent.

### ExclusionConstraint opclasses argument deprecated in favor of OpClass()

`django_1cb09fde64` · low · confidence medium · introduced in 4.1 · fires at future_removal

The opclasses argument of django.contrib.postgres.constraints.ExclusionConstraint is deprecated in favor of OpClass() in ExclusionConstraint.expressions. Switching requires 'django.contrib.postgres' in INSTALLED_APPS. After the change, makemigrations generates a new migration with RemoveConstraint and AddConstraint operations. The text says these can be wrapped in SeparateDatabaseAndState state_operations so no SQL runs.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where the opclasses argument of ExclusionConstraint is deprecated (upgrading from a version below 4.1). (confidence medium, judge partially_supported)
  - dj_notes@4.1: "is deprecated in favor of using OpClass() in ExclusionConstraint.expressions"
  - ⚠ The text does not state in which release the opclasses argument will be removed.
- **[required] api_usage** `present` `"opclasses"`: The application passes the opclasses argument to django.contrib.postgres.constraints.ExclusionConstraint. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "The opclasses argument of django.contrib.postgres.constraints.ExclusionConstraint"
- **[optional] configuration** `contains` `"django.contrib.postgres"`: To use OpClass() in ExclusionConstraint.expressions, 'django.contrib.postgres' must be in INSTALLED_APPS. If it is not listed, it must be added when migrating. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "To use it, you need to add 'django.contrib.postgres' in your INSTALLED_APPS"

Actions:
- Replace the opclasses argument of ExclusionConstraint with OpClass() in ExclusionConstraint.expressions.
- Add 'django.contrib.postgres' to INSTALLED_APPS if it is not already present.
- Run makemigrations; it generates a migration with RemoveConstraint and AddConstraint operations.
- Because the change has no effect on the database schema, move the generated operations into the state_operations argument of migrations.SeparateDatabaseAndState with database_operations=[] so no SQL runs.

### ModelAdmin.list_editable edits now run in atomic transactions

`django_205678f117` · low · confidence high · introduced in 4.2 · fires at first_use

Starting in Django 4.2, edits made through ModelAdmin.list_editable use atomic transactions. Admin classes that use list_editable now run their edits transactionally, which may differ from 3.2 behavior in how saves are committed or rolled back. The release note does not state any specific breakage.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where list_editable edits became atomic (upgrading from 3.2). (confidence high, judge supported)
  - dj_notes@4.2: "ModelAdmin.list_editable now uses atomic transactions when making edits."
- **[required] api_usage** `present` `"list_editable"`: The application defines ModelAdmin classes that set list_editable. (confidence high, judge supported)
  - dj_notes@4.2: "ModelAdmin.list_editable now uses atomic transactions when making edits."
- **[uncertain] behavior** `unknown` `"reliance on non-atomic list_editable saves"`: The application depends on edits in list_editable being non-atomic, for example relying on partial saves or on custom save/signal logic that is sensitive to transaction boundaries. (confidence low, judge partially_supported)
  - dj_notes@4.2: "now uses atomic transactions when making edits"
  - ⚠ The text does not describe what behavior differs or what impact the atomic transactions have on existing code.

Actions:
- Find ModelAdmin classes that use list_editable.
- Review those admins for custom save_model, save_related, signal handlers or changelist_view overrides that assume non-atomic saves.
- Test bulk edits in the admin changelist after upgrading, including the case where one row fails validation or saving.

### Query.add_filter() signature change (filter_clause replaced by filter_lhs and filter_rhs)

`django_4368ec5052` · low · confidence high · introduced in 4.0 · fires at first_use

The filter_clause argument of the undocumented Query.add_filter() method is replaced by two positional arguments filter_lhs and filter_rhs. Code that calls Query.add_filter() with filter_clause will break after the upgrade to 4.0 or later.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the add_filter() signature changed. (confidence high, judge supported)
  - dj_notes@4.0: "The filter_clause argument of the undocumented Query.add_filter() method is replaced by two positional arguments filter_lhs and filter_rhs."
- **[required] api_usage** `present` `"add_filter"`: The application calls Query.add_filter() (for example on a Query object) passing filter_clause. (confidence high, judge supported)
  - dj_notes@4.0: "The filter_clause argument of the undocumented Query.add_filter() method is replaced by two positional arguments filter_lhs and filter_rhs."

Actions:
- Find calls to Query.add_filter() in application code and third-party code.
- Replace the filter_clause argument with the two positional arguments filter_lhs and filter_rhs.

### ModelMultipleChoiceField list message removed

`django_48318ce619` · low · confidence high · introduced in 4.0 · fires at upgrade

The 'list' error message for ModelMultipleChoiceField is removed in Django 4.0. Code or tests that reference this message key (for example in custom error_messages or when asserting on error messages) will be affected when upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, in which the list message for ModelMultipleChoiceField is removed. (confidence high, judge supported)
  - dj_deprecation: "The list message for ModelMultipleChoiceField will be removed."
  - dj_notes@4.0: "The list message for ModelMultipleChoiceField is removed."
- **[required] api_usage** `present` `"ModelMultipleChoiceField"`: The application uses ModelMultipleChoiceField. (confidence high, judge supported)
  - dj_deprecation: "The list message for ModelMultipleChoiceField will be removed."
  - dj_notes@4.0: "The list message for ModelMultipleChoiceField is removed."
  - ⚠ The text does not say how the 'list' message was exposed (e.g. error_messages key), so the exact usage pattern to check is not stated.
- **[uncertain] api_usage** `present` `"'list'"`: The application overrides or references the 'list' error message key for ModelMultipleChoiceField (e.g. in error_messages or in tests/templates). (confidence low, judge partially_supported)
  - dj_deprecation: "The list message for ModelMultipleChoiceField will be removed."
  - ⚠ The text does not state how the message is referenced (the key name, where it is used) or what replaces it.

Actions:
- Search for ModelMultipleChoiceField usages and remove or replace any reliance on the 'list' error message key.
- Review tests and custom error_messages that reference the 'list' message and update them before upgrading.
- Search for ModelMultipleChoiceField usages and remove any customization of or dependence on the 'list' message.
- See the Django 3.0 deprecation notes (deprecated-features-3.0) for details on how to remove usage of this feature.

### Pre-3.1 SHA-1 admin password reset tokens no longer accepted

`django_4db2f08fa1` · low · confidence high · introduced in 4.0 · fires at first_use

Django 4.0 removes support for pre-Django 3.1 password reset tokens in the admin site that use the SHA-1 hashing algorithm. Any such legacy token still outstanding will no longer be accepted after upgrading from 3.2 to 4.2.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where support for pre-3.1 SHA-1 admin password reset tokens is removed. (confidence high, judge supported)
  - dj_notes@4.0: "Support for the pre-Django 3.1 password reset tokens in the admin site (that use the SHA-1 hashing algorithm) is removed."
  - dj_deprecation: "Support for the pre-Django 3.1 password reset tokens in the admin site (that use the SHA-1 hashing algorithm) will be removed."
- **[required] behavior** `present` `"pre-Django 3.1 password reset tokens in the admin site"`: The deployment uses the admin site's password reset functionality and has pre-Django 3.1 (SHA-1) password reset tokens that are still in use. (confidence high, judge supported)
  - dj_notes@4.0: "Support for the pre-Django 3.1 password reset tokens in the admin site"
  - dj_deprecation: "Support for the pre-Django 3.1 password reset tokens in the admin site"
  - ⚠ The text does not say how long legacy tokens could remain valid, so whether any such tokens still exist on a 3.2 deployment is not stated.
  - ⚠ The text does not say how the removal manifests (e.g., the exact error shown to users).

Actions:
- Ensure any users with outstanding pre-Django 3.1 password reset tokens request a new password reset link after the upgrade.
- Check for custom code that generates or relies on SHA-1 password reset tokens issued before Django 3.1.
- Ensure no password reset tokens generated before Django 3.1 are still in circulation; have affected users request a new password reset link after upgrading.
- Since the project is on 3.2, tokens issued under 3.1+ already use the newer scheme, so no code change is expected beyond verifying no legacy tokens remain.

### QuerySet.iterator() with prefetch_related and no chunk_size

`django_50a921cea2` · low · confidence low · introduced in 4.1 · fires at first_use

Calling QuerySet.iterator() on a queryset that prefetches related objects without chunk_size is deprecated as of 4.1. Older versions did no prefetching in this case. Callers must pass chunk_size to signal that the additional prefetch query per chunk is wanted.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, which deprecates iterator() on prefetching querysets without chunk_size. (confidence high, judge supported)
  - dj_notes@4.1: "The usage of QuerySet.iterator() on a queryset that prefetches related objects without providing the chunk_size argument is deprecated."
  - dj_notes@4.1: "QuerySet.iterator now supports prefetching related objects as long as the chunk_size argument is provided."
- **[required] api_usage** `present` `"iterator("`: The application calls QuerySet.iterator(). (confidence medium, judge supported)
  - dj_notes@4.1: "The usage of QuerySet.iterator() on a queryset that prefetches related objects without providing the chunk_size argument is deprecated."
  - dj_notes@4.1: "QuerySet.iterator now supports prefetching related objects as long as the chunk_size argument is provided."
  - dj_notes@4.1: "In older versions, no prefetching was done."
  - dj_notes@4.1: "as long as the chunk_size argument is provided"
  - ⚠ The text does not explicitly mention prefetch_related(); that it is the source of the prefetch lookups is inferred.
  - ⚠ The text does not state what happens when chunk_size is omitted in 4.1+.
- **[required] api_usage** `present` `"prefetch_related"`: The queryset passed to iterator() prefetches related objects (for example via prefetch_related or Prefetch). (confidence low, judge supported)
  - dj_notes@4.1: "on a queryset that prefetches related objects without providing the chunk_size argument"
  - ⚠ The text does not name prefetch_related or Prefetch as the mechanism.
- **[required] api_usage** `absent` `"chunk_size"`: The iterator() call does not pass a chunk_size argument. (confidence high, judge supported)
  - dj_notes@4.1: "without providing the chunk_size argument is deprecated"
- **[optional] behavior** `present` `"additional query per chunk"`: Prefetching is now performed on iterator(), with one additional query per chunk, where older versions did none. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "In older versions, no prefetching was done."
  - dj_notes@4.1: "the additional query per chunk needed to prefetch"
  - ⚠ The text does not say what happens when chunk_size is omitted, or when the deprecation ends.

Actions:
- Find iterator() calls on querysets that use prefetch_related or Prefetch and pass an explicit chunk_size to each, accepting the additional prefetch query per chunk.
- Run the test suite with deprecation warnings enabled to surface these calls.
- Search the codebase for QuerySet.iterator() calls that pass chunk_size and check whether the querysets use prefetch_related().
- Review and test the additional queries and memory use now produced per chunk, and remove unneeded prefetch_related() lookups or adjust chunk_size if necessary.

### CSRF cookie no longer masked; request.META['CSRF_COOKIE'] holds unmasked secret

`django_51841a4bc3` · low · confidence medium · introduced in 4.1 · fires at upgrade

Starting in 4.1, CsrfViewMiddleware no longer masks the CSRF cookie, and stores the unmasked CSRF secret in request.META['CSRF_COOKIE'] rather than a masked version. The text calls this an undocumented, private API. Code that reads request.META['CSRF_COOKIE'] or assumes the cookie value is masked may behave differently.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where CsrfViewMiddleware stopped masking the CSRF cookie. (confidence high, judge supported)
  - dj_notes@4.1: "CsrfViewMiddleware no longer masks the CSRF cookie like it does the CSRF token in the DOM."
  - dj_notes@4.1: "CsrfViewMiddleware now uses request.META['CSRF_COOKIE'] for storing the unmasked CSRF secret rather than a masked version."
- **[required] api_usage** `present` `"request.META['CSRF_COOKIE']"`: The application reads or relies on request.META['CSRF_COOKIE'] and its previous masked value. (confidence medium, judge supported)
  - dj_notes@4.1: "CsrfViewMiddleware now uses request.META['CSRF_COOKIE'] for storing the unmasked CSRF secret rather than a masked version."
  - dj_notes@4.1: "This is an undocumented, private API."
  - ⚠ The text calls this an undocumented, private API and does not say which usages break.
  - ⚠ The text does not say what code reading this key would break or how.
- **[optional] behavior** `contains` `"CSRF cookie"`: The application code or client-side scripts read the CSRF cookie value directly and assume it is masked. (confidence low, judge partially_supported)
  - dj_notes@4.1: "CsrfViewMiddleware no longer masks the CSRF cookie like it does the CSRF token in the DOM."
  - ⚠ The text does not state that consumers of the cookie are affected, so this is an inferred impact.

Actions:
- Search for code using request.META['CSRF_COOKIE'] and stop depending on its masked form.
- Do not rely on the CSRF cookie value being masked; use the documented CSRF token APIs instead.
- Run CSRF-related tests after upgrading.
- Search the codebase and third-party middleware for direct access to request.META['CSRF_COOKIE'].
- Update any code that assumes the value is masked so that it handles the unmasked secret, or stop relying on this private API.

### PBKDF2 password hasher default iteration count increased

`django_5f49526547` · low · confidence medium · introduced in 4.2 · fires at upgrade

The default iteration count for the PBKDF2 password hasher increases from 390,000 to 600,000 in Django 4.2. Applications that use the PBKDF2 hasher with its default iteration count get the new value after the upgrade. The text does not state any further effects.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which changes the PBKDF2 default iteration count. (confidence medium, judge supported)
  - dj_notes@4.2: "The default iteration count for the PBKDF2 password hasher is increased from 390,000 to 600,000."
  - dj_notes@4.0: "The default iteration count for the PBKDF2 password hasher is increased from 260,000 to 320,000."
  - dj_notes@4.1: "The default iteration count for the PBKDF2 password hasher is increased from 320,000 to 390,000."
  - ⚠ History: in 4.0, 'PBKDF2 default iteration count increase' applied to the same symbol (pbkdf2passwordhasher); superseded by the 4.2 change (R2).
  - ⚠ History: in 4.1, 'PBKDF2 password hasher default iteration count increase' applied to the same symbol (pbkdf2passwordhasher); superseded by the 4.2 change (R2).
- **[required] api_usage** `present` `"PBKDF2PasswordHasher"`: The application uses the PBKDF2 password hasher and relies on its default iteration count. (confidence medium, judge supported)
  - dj_notes@4.2: "The default iteration count for the PBKDF2 password hasher is increased from 390,000 to 600,000."
  - ⚠ The text does not say how existing stored hashes or custom iteration settings are affected.
- **[optional] behavior** `contains` `"390000"`: Code, tests or configuration depend on the previous iteration count of 390,000. (confidence low, judge partially_supported)
  - dj_notes@4.2: "increased from 390,000 to 600,000"
  - ⚠ The text does not state that any such dependency exists or what its effect would be.
- **[disqualifying] api_usage** `present` `"iterations"`: The application overrides the iterations value in a custom PBKDF2 hasher subclass, so the new default may not apply. (confidence low, judge partially_supported)
  - dj_notes@4.2: "The default iteration count for the PBKDF2 password hasher is increased from 390,000 to 600,000."
  - ⚠ The text does not describe overriding the iteration count.

Actions:
- Check whether code, tests or configuration depend on the previous 390,000 iteration count.
- Review PASSWORD_HASHERS and any custom PBKDF2 hasher subclasses for the iteration count they use.

### modelform_factory now respects Meta.formfield_callback

`django_6028e954a2` · low · confidence medium · introduced in 4.2 · fires at first_use

Starting in 4.2, modelform_factory respects the formfield_callback attribute of the form's Meta. Forms generated by modelform_factory from a base form whose Meta defines formfield_callback may now produce different form fields than under 3.2.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where modelform_factory begins respecting Meta.formfield_callback. (confidence high, judge supported)
  - dj_notes@4.2: "modelform_factory now respects the formfield_callback attribute of the form's Meta."
- **[required] api_usage** `present` `"modelform_factory"`: The application calls modelform_factory. (confidence high, judge supported)
  - dj_notes@4.2: "modelform_factory now respects the formfield_callback attribute of the form's Meta."
- **[required] api_usage** `present` `"formfield_callback"`: The form passed to modelform_factory (or its Meta) defines formfield_callback. (confidence medium, judge supported)
  - dj_notes@4.2: "modelform_factory now respects the formfield_callback attribute of the form's Meta."
  - ⚠ The text does not state how modelform_factory behaved with Meta.formfield_callback before 4.2.

Actions:
- Search for modelform_factory calls whose base form's Meta defines formfield_callback.
- Verify that the fields generated by those factory-built forms are still correct under 4.2, and add or run tests for them.

### CsrfViewMiddleware internal CSRF cookie tracking attributes replaced

`django_646caddec9` · low · confidence medium · introduced in 4.0 · fires at upgrade

CsrfViewMiddleware now tracks whether the CSRF cookie should be sent with request.META['CSRF_COOKIE_NEEDS_UPDATE'] instead of request.META['CSRF_COOKIE_USED'], request.csrf_cookie_needs_reset and response.csrf_cookie_set. Custom code (for example custom middleware or tests) that reads or sets the old keys or attributes will no longer interact with CSRF cookie handling as before. The text describes these as undocumented, private API.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where this change was introduced (upgrading from 3.2 to 4.2). (confidence high, judge supported)
  - dj_notes@4.0: "CsrfViewMiddleware now uses request.META['CSRF_COOKIE_NEEDS_UPDATE'] in place of"
- **[alternative] api_usage** `present` `"CSRF_COOKIE_USED"`: Application code references request.META['CSRF_COOKIE_USED']. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "in place of request.META['CSRF_COOKIE_USED'], request.csrf_cookie_needs_reset, and response.csrf_cookie_set to track"
- **[alternative] api_usage** `present` `"csrf_cookie_needs_reset"`: Application code references request.csrf_cookie_needs_reset. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "in place of request.META['CSRF_COOKIE_USED'], request.csrf_cookie_needs_reset, and response.csrf_cookie_set to track"
- **[alternative] api_usage** `present` `"csrf_cookie_set"`: Application code references response.csrf_cookie_set. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "in place of request.META['CSRF_COOKIE_USED'], request.csrf_cookie_needs_reset, and response.csrf_cookie_set to track"

Actions:
- Search the codebase, custom middleware and tests for CSRF_COOKIE_USED, csrf_cookie_needs_reset and csrf_cookie_set.
- Replace usages with request.META['CSRF_COOKIE_NEEDS_UPDATE'] where the behavior is still needed, or remove reliance on this private API.

### No-op AlterField operations generated by makemigrations for ForeignKey/ManyToManyField

`django_6578964c0b` · low · confidence medium · introduced in 4.0 · fires at first_use

Starting in Django 4.0, the migrations autodetector uses model states instead of model classes, and migration operations for ForeignKey and ManyToManyField no longer specify attributes not passed during field initialization. As a side effect, makemigrations might generate no-op AlterField operations for ManyToManyField and ForeignKey fields in some cases.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the migrations autodetector began using model states and field operations stopped specifying attributes not passed at initialization. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "The migrations autodetector now uses model states instead of model classes."
- **[alternative] api_usage** `present` `"ForeignKey"`: The application defines models with ForeignKey fields (migrations are managed and makemigrations is run). (confidence medium, judge supported)
  - dj_notes@4.0: "migration operations for ForeignKey and ManyToManyField fields no longer specify attributes which were not passed to the fields during initialization"
  - ⚠ The text says only 'in some cases' and does not specify which ForeignKey definitions trigger no-op AlterField operations.
- **[alternative] api_usage** `present` `"ManyToManyField"`: The application defines models with ManyToManyField fields (migrations are managed and makemigrations is run). (confidence medium, judge supported)
  - dj_notes@4.0: "running makemigrations might generate no-op AlterField operations for ManyToManyField and ForeignKey fields in some cases"
  - ⚠ The text says only 'in some cases' and does not specify which ManyToManyField definitions trigger no-op AlterField operations.

Actions:
- After upgrading, run makemigrations and review any generated AlterField operations on ForeignKey and ManyToManyField fields before committing them.
- Be aware that such AlterField operations are described as no-ops, so they should not change the database schema.

### InlineModelAdmin.verbose_name_plural fallback change

`django_65b3b830af` · low · confidence low · introduced in 4.0 · fires at upgrade

Starting in Django 4.0, InlineModelAdmin.verbose_name_plural falls back to InlineModelAdmin.verbose_name + 's'. Inline admin classes that set verbose_name but not verbose_name_plural may display a different plural label in the admin after the upgrade. The text does not state what the previous fallback was.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where the verbose_name_plural fallback changed. (confidence high, judge supported)
  - dj_notes@4.0: "The InlineModelAdmin.verbose_name_plural attribute now fallbacks to the InlineModelAdmin.verbose_name + 's'."
- **[required] api_usage** `present` `"verbose_name"`: The application defines InlineModelAdmin subclasses (e.g. TabularInline or StackedInline) that set verbose_name. (confidence medium, judge supported)
  - dj_notes@4.0: "The InlineModelAdmin.verbose_name_plural attribute now fallbacks to the InlineModelAdmin.verbose_name + 's'."
  - ⚠ The text does not state how verbose_name_plural was derived before 4.0.
- **[required] api_usage** `absent` `"verbose_name_plural"`: The inline does not explicitly set verbose_name_plural, so the new fallback applies. (confidence low, judge partially_supported)
  - dj_notes@4.0: "The InlineModelAdmin.verbose_name_plural attribute now fallbacks to the InlineModelAdmin.verbose_name + 's'."
  - ⚠ The text does not explicitly say that explicitly set values are unaffected.

Actions:
- Review admin inline classes that set verbose_name without verbose_name_plural and check the plural label shown in the admin.
- Set verbose_name_plural explicitly on those inlines if a different plural label is required.

### Email attach/attach_alternative exception type changed from AssertionError to ValueError

`django_68ec37b26b` · low · confidence low · introduced in 4.0 · fires at first_use

Calling EmailMultiAlternatives.attach_alternative() or EmailMessage.attach() with invalid content or mimetype arguments now raises ValueError instead of AssertionError. Code that catches AssertionError (or tests asserting it) around these calls will no longer handle the error.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, which introduced the exception type change. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "now raise ValueError instead of AssertionError"
- **[required] api_usage** `present` `"attach_alternative|\\.attach("`: The application calls EmailMessage.attach() or EmailMultiAlternatives.attach_alternative(). (confidence high, judge supported)
  - dj_notes@4.0: "Calling EmailMultiAlternatives.attach_alternative() or EmailMessage.attach()"
- **[required] behavior** `present` `"AssertionError"`: The application or its tests catch or assert AssertionError around these attach calls, and invalid content or mimetype arguments can be passed. (confidence low, judge supported)
  - dj_notes@4.0: "with an invalid content or mimetype arguments now raise ValueError instead of AssertionError"
  - ⚠ The text does not state how the application handles these exceptions; whether code catches AssertionError must be checked in the codebase.

Actions:
- Update exception handling around EmailMessage.attach() and EmailMultiAlternatives.attach_alternative() to catch ValueError instead of AssertionError.
- Update tests that expect AssertionError from these calls to expect ValueError.

### AdminSite index view no longer wrapped in never_cache when accessed directly

`django_6b02370c63` · low · confidence medium · introduced in 4.0 · fires at upgrade

As of 4.0, the AdminSite method for the admin index view is no longer decorated with never_cache when it is accessed directly instead of via AdminSite.urls or AdminSite.get_urls(). Code that wires the index view directly into URL configuration loses the never_cache headers, so responses may be cached.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the never_cache decoration of the admin index view changed. (confidence high, judge supported)
  - dj_notes@4.0: "The AdminSite method for the admin index view is no longer decorated with never_cache when accessed directly"
- **[required] api_usage** `present` `"AdminSite.index"`: The application accesses the AdminSite index view method directly (for example in a custom URLconf) rather than via AdminSite.urls or AdminSite.get_urls(). (confidence medium, judge supported)
  - dj_notes@4.0: "no longer decorated with never_cache when accessed directly, rather than via the recommended AdminSite.urls property, or AdminSite.get_urls() method"
  - ⚠ The text does not name the method explicitly; it says only 'the AdminSite method for the admin index view'.
- **[disqualifying] api_usage** `present` `"AdminSite.urls"`: The application accesses the admin index only via AdminSite.urls or AdminSite.get_urls(), which are unaffected. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "rather than via the recommended AdminSite.urls property, or AdminSite.get_urls() method"

Actions:
- Expose the admin through AdminSite.urls or AdminSite.get_urls() instead of referencing the index view method directly.
- If the index view must be referenced directly, wrap it explicitly with django.views.decorators.cache.never_cache.

### Session cookies hidden in error reports

`django_7019792cec` · low · confidence low · introduced in 4.2 · fires at first_use

As of 4.2, session cookies are treated as credentials and replaced with stars in error reports. Workflows that read session cookie values in error reports (debug page or reports derived from it) will no longer see them.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which introduced masking of session cookies in error reports. (confidence high, judge supported)
  - dj_notes@4.2: "Session cookies are now treated as credentials and therefore hidden and replaced with stars"
- **[required] behavior** `present` `"session cookie values read from error reports"`: The application or its operations rely on seeing session cookie values in Django error reports. (confidence low, judge supported)
  - dj_notes@4.2: "Session cookies are now treated as credentials and therefore hidden and replaced with stars"
  - ⚠ The text does not say which error report mechanisms (debug page, email reports, custom reporters) are affected beyond 'error reports'.

Actions:
- Check any tooling, runbooks or tests that read session cookie values from Django error reports or the debug page and adjust them to expect masked values.

### Query.add_annotation() is_summary argument removed

`django_793d3b8716` · low · confidence high · introduced in 4.2 · fires at first_use

The is_summary argument of the undocumented Query.add_annotation() method is removed in Django 4.2. Code that calls Query.add_annotation() and passes is_summary will break. Because the method is undocumented, the affected code is most likely to be custom ORM internals or third-party libraries.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, which removes the is_summary argument of Query.add_annotation(). (confidence high, judge supported)
  - dj_notes@4.2: "The is_summary argument of the undocumented Query.add_annotation() method is removed."
- **[required] api_usage** `present` `"is_summary"`: Application code or a third-party library calls Query.add_annotation() and passes the is_summary argument. (confidence high, judge supported)
  - dj_notes@4.2: "The is_summary argument of the undocumented Query.add_annotation() method is removed."

Actions:
- Search the application and third-party code for calls to add_annotation() that pass is_summary.
- Remove the is_summary argument from those calls.
- Upgrade or patch any third-party library that passes is_summary to Query.add_annotation().

### RssFeed/Atom1Feed empty elements now self-closing

`django_7efc1311fa` · low · confidence high · introduced in 4.0 · fires at upgrade

Since Django 4.0, RssFeed, Atom1Feed, and their subclasses emit elements with no content as self-closing tags. Feed output for empty elements changes in form, which could affect consumers or tests that compare the generated XML textually.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where the feed output change was introduced (3.2 -> 4.2). (confidence high, judge supported)
  - dj_notes@4.0: "RssFeed, Atom1Feed, and their subclasses now emit elements with no content as self-closing tags."
- **[required] api_usage** `present` `"RssFeed|Atom1Feed"`: The application uses RssFeed, Atom1Feed, or a subclass of either to generate feeds. (confidence high, judge supported)
  - dj_notes@4.0: "RssFeed, Atom1Feed, and their subclasses now emit elements with no content as self-closing tags."
- **[optional] test_coverage** `contains` `"empty element in feed XML expected as <tag></tag>"`: Code or tests compare generated feed XML textually, or a consumer parses it in a way sensitive to self-closing versus open/close empty tags. (confidence low, judge partially_supported)
  - dj_notes@4.0: "emit elements with no content as self-closing tags"
  - ⚠ The text does not state which elements may be empty or how consumers handle the self-closing form.

Actions:
- Review tests and consumers that compare generated RSS/Atom XML as text and update expected output to use self-closing tags for empty elements.
- Verify downstream feed readers accept the self-closing form of empty elements.

### JSON-encoded string default passed to JSONBAgg

`django_863b5fb220` · low · confidence medium · introduced in 4.2 · fires at future_removal

Aggregates such as JSONBAgg used to accept JSON-encoded string literals as defaults, for example default=Value("[]"). During the 4.2 deprecation period these are JSON-decoded with a warning. From Django 5.1 string literals will be implicitly interpreted as JSON string literals.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where passing encoded JSON string literals is deprecated (current version below 4.2). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "During the deprecation period string literals will be attempted to be JSON decoded"
- **[required] api_usage** `present` `"JSONBAgg(..., default=Value(\"<JSON-encoded string>\"))"`: The application passes a JSON-encoded string literal in Value() as the default of JSONBAgg or another JSON aggregate. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "Document.objects.annotate( JSONBAgg("field", default=Value("[]")), )"

Actions:
- Replace default=Value("[]") with default=[] in JSONBAgg calls.
- Run tests with deprecation warnings enabled to find remaining encoded string defaults.

### django.test.runner.reorder_suite() renamed to reorder_tests() with changed argument and return types

`django_8abb4cc21d` · low · confidence high · introduced in 4.0 · fires at upgrade

The undocumented function django.test.runner.reorder_suite() is renamed to reorder_tests(). Code that still calls reorder_suite() (e.g. custom test runners) will fail to find it. The new function accepts an iterable of tests rather than a test suite and returns an iterator of tests, so callers must adapt to the new input and output types.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, which renamed reorder_suite() to reorder_tests(). (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented django.test.runner.reorder_suite() function is renamed to reorder_tests()."
- **[required] api_usage** `present` `"reorder_suite"`: The application or its test tooling (e.g. a custom test runner) calls or imports django.test.runner.reorder_suite(). (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented django.test.runner.reorder_suite() function is renamed to reorder_tests()."
- **[optional] behavior** `present` `"reorder_tests"`: Callers of the renamed function pass a test suite or rely on a suite being returned, which differs from the new iterable-in, iterator-out contract. (confidence high, judge supported)
  - dj_notes@4.0: "It now accepts an iterable of tests rather than a test suite, and returns an iterator of tests."

Actions:
- Replace usages of django.test.runner.reorder_suite() with django.test.runner.reorder_tests().
- Update callers to pass an iterable of tests instead of a test suite.
- Update code consuming the result to handle an iterator of tests rather than a test suite.

### CSS form media link tags no longer include type="text/css"

`django_910ce87d08` · low · confidence low · introduced in 4.1 · fires at upgrade

The type="text/css" attribute is no longer rendered in <link> tags for CSS form media. Code, tests, or templates that depend on that attribute in rendered output (e.g. HTML string assertions or selectors) may break or differ.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where the type attribute was removed from CSS form media link tags. (confidence high, judge supported)
  - dj_notes@4.1: "The type="text/css" attribute is no longer included in <link> tags for CSS form media."
- **[required] behavior** `present` `"type=\"text/css\""`: The application renders CSS form media (e.g. forms or widgets with Media css) and depends on the type="text/css" attribute being present in the rendered <link> tags, such as in tests asserting HTML output or in CSS/JS selectors. (confidence low, judge partially_supported)
  - dj_notes@4.1: "The type="text/css" attribute is no longer included in <link> tags for CSS form media."
  - ⚠ The text does not say what specifically may depend on the attribute; dependence on it in tests or client-side selectors is inferred.

Actions:
- Search tests and templates for assertions or selectors that expect type="text/css" in rendered form media <link> tags and update them to not require the attribute.

### RemoteUserBackend.configure_user subclass without created argument

`django_91802d0ff8` · low · confidence medium · introduced in 4.1 · fires at future_removal

Django 4.1 adds created=True to the signature of RemoteUserBackend.configure_user. Support for RemoteUserBackend subclasses whose configure_user does not accept this argument is deprecated, so such subclasses should be updated.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where the configure_user signature change and deprecation were introduced. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "created=True is added to the signature of RemoteUserBackend.configure_user."
- **[required] api_usage** `present` `"RemoteUserBackend"`: The application subclasses RemoteUserBackend and overrides configure_user. (confidence high, judge supported)
  - dj_notes@4.1: "Support for RemoteUserBackend subclasses that do not accept this argument is deprecated."
- **[required] api_usage** `absent` `"created"`: The overriding configure_user does not accept the created argument (for example no created parameter and no **kwargs). (confidence medium, judge supported)
  - dj_notes@4.1: "subclasses that do not accept this argument is deprecated"
  - ⚠ The text does not state what happens when support is removed, nor in which release.

Actions:
- Update configure_user in any RemoteUserBackend subclass to accept the created argument.

### FileSystemStorage.delete() empty name exception type changed

`django_9b38717bcc` · low · confidence medium · introduced in 4.0 · fires at first_use

In Django 4.0, calling FileSystemStorage.delete() with an empty name raises ValueError instead of AssertionError. Code that catches AssertionError (or tests asserting it) around this call will no longer handle the exception.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the exception type changed. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Calling FileSystemStorage.delete() with an empty name now raises ValueError instead of AssertionError."
- **[required] api_usage** `present` `"FileSystemStorage"`: The application calls FileSystemStorage.delete() (directly or via a subclass or storage API) and may pass an empty name. (confidence high, judge supported)
  - dj_notes@4.0: "Calling FileSystemStorage.delete() with an empty name now raises ValueError instead of AssertionError."
- **[optional] behavior** `present` `"AssertionError"`: The application or its tests catch or assert AssertionError from FileSystemStorage.delete(). (confidence low, judge partially_supported)
  - dj_notes@4.0: "now raises ValueError instead of AssertionError"
  - ⚠ The text does not state whether any callers rely on catching AssertionError.

Actions:
- Update exception handling around FileSystemStorage.delete() to catch ValueError instead of AssertionError.
- Update tests that expect AssertionError when deleting with an empty name to expect ValueError.
- Avoid calling delete() with an empty name.

### AlterIndexTogether not to be used in new migrations

`django_9f3db82e18` · low · confidence high · introduced in 4.2 · fires at first_use

AlterIndexTogether is officially supported only for pre-Django 4.2 migration files. It remains part of the public API with no plan to deprecate or remove it, but it should not be used in new migrations. AddIndex and RemoveIndex should be used instead.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, from which AlterIndexTogether is officially supported only for pre-4.2 migration files. (confidence high, judge supported)
  - dj_notes@4.2: "The AlterIndexTogether migration operation is now officially supported only for pre-Django 4.2 migration files."
- **[required] api_usage** `present` `"AlterIndexTogether"`: The codebase uses or writes AlterIndexTogether in migration files, or plans to add it to new migrations. (confidence high, judge supported)
  - dj_notes@4.2: "The AlterIndexTogether migration operation is now officially supported only for pre-Django 4.2 migration files."

Actions:
- Do not use AlterIndexTogether in new migrations.
- Use AddIndex and RemoveIndex operations instead for new migrations.

### GeoJSON serializer output now includes id key

`django_a03bfcb268` · low · confidence high · introduced in 4.2 · fires at upgrade

In 4.2 the GeoJSON serializer adds an id key to each serialized feature, defaulting to the object's primary key. Code, tests, or API clients that depend on the exact GeoJSON output of earlier versions may see a different structure.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses release 4.2, where the GeoJSON serializer started outputting the id key. (confidence high, judge supported)
  - dj_notes@4.2: "The GeoJSON serializer now outputs the id key for serialized features"
- **[required] api_usage** `present` `"geojson"`: The application serializes data with the GeoJSON serializer. (confidence high, judge supported)
  - dj_notes@4.2: "The GeoJSON serializer now outputs the id key for serialized features"
- **[uncertain] test_coverage** `contains` `"GeoJSON feature output compared exactly"`: Tests or downstream consumers compare or strictly validate the exact GeoJSON feature structure, so the added id key could cause a mismatch. (confidence low, judge not_supported)
  - dj_notes@4.2: "which defaults to the primary key of objects"
  - ⚠ The text does not state how the id key is configured or disabled, or whether any consumers are affected.
  - ⚠ Judge: evidence does not support this claim. The quote only says the id defaults to the primary key of objects; it says nothing about tests or downstream consumers comparing or strictly validating the GeoJSON structure, nor any mismatch risk from the added id key.

Actions:
- Review code, tests, and API consumers that use the GeoJSON serializer output and make sure they tolerate the additional id key on each feature.
- Update test fixtures or expected GeoJSON output to include the id key, which defaults to the object's primary key.

### Tests that fail to load now always match test --tag

`django_a34fcce24b` · low · confidence high · introduced in 4.0 · fires at first_use

Starting in Django 4.0, tests that fail to load (for example due to syntax errors) always match when running the test command with --tag. Tag-filtered test runs will therefore include and surface these load failures rather than excluding them.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where tests that fail to load now always match when using test --tag. (confidence high, judge supported)
  - dj_notes@4.0: "Tests that fail to load, for example due to syntax errors, now always match when using test --tag."
- **[required] behavior** `present` `"--tag"`: The project or its CI runs the Django test command with the --tag option to select tests. (confidence high, judge supported)
  - dj_notes@4.0: "now always match when using test --tag"
- **[optional] test_coverage** `present` `"tests that fail to load"`: Some tests in the project fail to load (for example due to syntax or import errors), which will now be matched by --tag filters and surface as failures. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "Tests that fail to load, for example due to syntax errors"

Actions:
- Check CI scripts and test commands that use --tag and make sure all test modules import and load without errors.
- Fix any syntax or import errors in test modules, since they will now be included in tag-filtered runs and reported as failures.

### Undocumented URL resolver internals moved to django.contrib.admindocs.utils

`django_af968f5ff7` · low · confidence medium · introduced in 4.1 · fires at first_use

The undocumented URLResolver._is_callback(), URLResolver._callback_strs, and URLPattern.lookup_str() were moved to django.contrib.admindocs.utils in Django 4.1. Code that calls these private attributes on the URL resolver/pattern classes will no longer find them there and must use the new location.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, where these undocumented methods were moved. (confidence high, judge supported)
  - dj_notes@4.1: "The undocumented URLResolver._is_callback(), URLResolver._callback_strs, and URLPattern.lookup_str() are moved to django.contrib.admindocs.utils."
- **[required] api_usage** `present` `"_is_callback|_callback_strs|lookup_str"`: The application code references URLResolver._is_callback, URLResolver._callback_strs, or URLPattern.lookup_str. (confidence medium, judge supported)
  - dj_notes@4.1: "The undocumented URLResolver._is_callback(), URLResolver._callback_strs, and URLPattern.lookup_str() are moved to django.contrib.admindocs.utils."
  - ⚠ The text does not state whether the old attributes remain available on URLResolver/URLPattern after the move, only that they are moved.

Actions:
- Search the codebase and third-party code for uses of _is_callback, _callback_strs and lookup_str.
- Replace usages with the equivalents in django.contrib.admindocs.utils, or avoid relying on these undocumented private APIs.

### Renamed admin utility lookup_needs_distinct to lookup_spawns_duplicates

`django_b75c50a6ca` · low · confidence medium · introduced in 4.0 · fires at upgrade

The undocumented function django.contrib.admin.utils.lookup_needs_distinct() is renamed to lookup_spawns_duplicates() in 4.0. Code that imports or calls the old name will no longer find it after the upgrade.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses release 4.0, where lookup_needs_distinct() is renamed. (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented django.contrib.admin.utils.lookup_needs_distinct() function is renamed to lookup_spawns_duplicates()."
- **[required] api_usage** `present` `"lookup_needs_distinct"`: The application code imports or calls django.contrib.admin.utils.lookup_needs_distinct(). (confidence medium, judge supported)
  - dj_notes@4.0: "The undocumented django.contrib.admin.utils.lookup_needs_distinct() function is renamed to lookup_spawns_duplicates()."
  - ⚠ The text does not explicitly say that the old name stops working, only that the function is renamed.

Actions:
- Replace usages of lookup_needs_distinct() with lookup_spawns_duplicates() from django.contrib.admin.utils.
- Because the function was undocumented, check whether custom admin code or third-party packages depend on it.

### django-db-logger logger now logs transaction queries at DEBUG

`django_b7d77765c8` · low · confidence medium · introduced in 4.2 · fires at upgrade

Starting in Django 4.2, the django-db-logger logger logs transaction management queries (BEGIN, COMMIT, and ROLLBACK) at the DEBUG level. Deployments that capture DEBUG output from this logger may see additional log entries, which can increase log volume or affect log-based assertions or monitoring.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django 4.2, where the logger started logging transaction management queries. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "now logs transaction management queries (BEGIN, COMMIT, and ROLLBACK) at the DEBUG level"
- **[required] configuration** `present` `"django-db-logger"`: The application or deployment configures or consumes the django-db-logger logger, for example in LOGGING handlers or loggers with DEBUG level enabled. (confidence medium, judge partially_supported)
  - dj_notes@4.2: "The django-db-logger logger now logs transaction management queries"
  - ⚠ The text does not say which handlers or levels are affected, only that the messages are logged at DEBUG level.
- **[optional] configuration** `equals` `"DEBUG"`: The logger or handler level is set to DEBUG or lower so the new DEBUG-level messages are emitted, increasing log output. (confidence low, judge partially_supported)
  - dj_notes@4.2: "at the DEBUG level"
  - ⚠ The text does not describe the impact of the extra messages.

Actions:
- Review LOGGING configuration for the django-db-logger logger and check whether DEBUG-level handlers will now receive BEGIN, COMMIT and ROLLBACK entries.
- Adjust the logger or handler level, or add filters, if the additional entries are unwanted.

### TRANSLATOR_COMMENT_MARK moved from django.template.base

`django_cad51ea34e` · low · confidence high · introduced in 4.0 · fires at upgrade

The undocumented TRANSLATOR_COMMENT_MARK constant was moved from django.template.base to django.utils.translation.template in 4.0. Code importing or referencing it from django.template.base will no longer find it there. Because it was undocumented, few projects are likely to use it.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where the constant was moved. (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented TRANSLATOR_COMMENT_MARK constant is moved from django.template.base to django.utils.translation.template."
- **[required] api_usage** `present` `"TRANSLATOR_COMMENT_MARK"`: The application references TRANSLATOR_COMMENT_MARK from django.template.base. (confidence high, judge supported)
  - dj_notes@4.0: "The undocumented TRANSLATOR_COMMENT_MARK constant is moved from django.template.base to django.utils.translation.template."

Actions:
- Change imports and references of TRANSLATOR_COMMENT_MARK to use django.utils.translation.template instead of django.template.base.

### mark_safe lazy object preservation

`django_cd2220a8df` · low · confidence medium · introduced in 4.1 · fires at first_use

Starting in Django 4.1, mark_safe preserves lazy objects. Code that passes lazy objects (for example lazy strings) to mark_safe may now get a lazy object back instead of the previous result. The text does not describe the previous behavior or the practical impact.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where mark_safe began preserving lazy objects. (confidence high, judge supported)
  - dj_notes@4.1: "mark_safe now preserves lazy objects."
- **[required] api_usage** `present` `"mark_safe"`: The application calls mark_safe, possibly with lazy objects as input. (confidence medium, judge supported)
  - dj_notes@4.1: "mark_safe now preserves lazy objects."
  - ⚠ The text does not say what mark_safe returned for lazy objects before 4.1, so the exact behavioral difference is unknown.
- **[uncertain] behavior** `present` `"lazy objects passed to mark_safe"`: The application passes lazy objects, such as lazy translation strings or SimpleLazyObject instances, to mark_safe. (confidence low, judge partially_supported)
  - dj_notes@4.1: "mark_safe now preserves lazy objects."
  - ⚠ The text does not specify which kinds of lazy objects are affected.

Actions:
- Find all mark_safe calls and identify those that receive lazy objects such as lazy translation strings or SimpleLazyObject.
- Test the code paths that mark lazy values as safe, and confirm that rendered output and any type or isinstance checks on the result still behave as expected on 4.2.

### PickleSerializer deprecated in 4.1

`django_cd78591007` · low · confidence medium · introduced in 4.1 · fires at future_removal

django.contrib.sessions.serializers.PickleSerializer is deprecated in 4.1 due to the risk of remote code execution. Applications using it will be affected by the deprecation; the text does not state a removal version or a replacement.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade from 3.2 to 4.2 crosses release 4.1, in which PickleSerializer was deprecated. (confidence high, judge supported)
  - dj_notes@4.1: "django.contrib.sessions.serializers.PickleSerializer is deprecated due to the risk of remote code execution."
- **[required] api_usage** `present` `"PickleSerializer"`: The application uses django.contrib.sessions.serializers.PickleSerializer, for example as the SESSION_SERIALIZER setting. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "django.contrib.sessions.serializers.PickleSerializer is deprecated due to the risk of remote code execution."
  - ⚠ The text does not state how PickleSerializer is configured (e.g. via SESSION_SERIALIZER) or what replaces it.

Actions:
- Search the codebase and settings for PickleSerializer and stop using it.
- Review the Django documentation for a non-pickle session serializer, since the release note names no replacement.

### log_response exc_info argument replaced by exception

`django_d1c6eb373c` · low · confidence medium · introduced in 4.1 · fires at first_use

The exc_info argument of the undocumented django.utils.log.log_response() function was replaced by exception in 4.1. Code calling log_response() with exc_info will need to pass exception instead.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where the log_response() argument change was introduced. (confidence high, judge supported)
  - dj_notes@4.1: "The exc_info argument of the undocumented django.utils.log.log_response() function is replaced by exception."
- **[required] api_usage** `present` `"log_response("`: The application code calls django.utils.log.log_response() passing the exc_info argument. (confidence medium, judge supported)
  - dj_notes@4.1: "The exc_info argument of the undocumented django.utils.log.log_response() function is replaced by exception."
  - ⚠ The text does not state what happens (e.g. TypeError) when exc_info is passed after the change.

Actions:
- Search for calls to django.utils.log.log_response() and replace the exc_info argument with exception.
- Note that log_response() is undocumented, so consider avoiding direct use of it.

### Admin log out UI now uses POST requests

`django_e15fd536b5` · low · confidence medium · introduced in 4.1 · fires at upgrade

The Django admin log out UI now uses POST requests instead of the previous behavior. The text lists this as a backwards incompatible change, so custom templates, links, tests or integrations that depend on the previous log out request method in the admin may be affected. The text does not state the previous method or the exact impact.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses release 4.1, where the admin log out UI change was introduced (3.2 -> 4.2). (confidence high, judge supported)
  - dj_notes@4.1: "The admin log out UI now uses POST requests."
- **[required] api_usage** `present` `"admin log out"`: The application uses the Django admin log out UI, or has custom templates, links, tests or integrations that depend on how admin log out requests are made. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "The admin log out UI now uses POST requests."
  - ⚠ The text does not state what request method was used previously or which customizations are affected.

Actions:
- Check the admin log out flow after upgrading and confirm it works with POST requests.
- Review any custom admin templates, links or tests that trigger admin log out (e.g. via GET) and update them to use POST.

### ProjectState real_apps must be a set

`django_e2d9e19604` · low · confidence medium · introduced in 4.0 · fires at first_use

The real_apps argument of the undocumented django.db.migrations.state.ProjectState.__init__() method must now be a set if provided. Code that constructs ProjectState with a non-set real_apps (e.g. a list) will break. This is an undocumented API, so only custom migration tooling or tests calling it directly are likely affected.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade from 3.2 to 4.2 crosses release 4.0, where real_apps was changed to require a set. (confidence high, judge supported)
  - dj_notes@4.0: "The real_apps argument of the undocumented django.db.migrations.state.ProjectState.init() method must now be a set if provided."
- **[required] api_usage** `present` `"ProjectState("`: The application constructs ProjectState and passes the real_apps argument. (confidence high, judge supported)
  - dj_notes@4.0: "The real_apps argument of the undocumented django.db.migrations.state.ProjectState.init() method must now be a set if provided."
- **[required] behavior** `not_equals` `"set"`: The real_apps value passed is not a set (e.g. a list or tuple). (confidence medium, judge supported)
  - dj_notes@4.0: "must now be a set if provided"
  - ⚠ The text does not state what exactly happens (e.g. which exception) when a non-set is passed.

Actions:
- Search for direct calls to ProjectState(...) that pass real_apps and ensure the value is a set (e.g. set(...) or a set literal).
- Avoid relying on this undocumented API where possible.

### Model.full_clean converts exclude to a set; callers and overrides should pass exclude as a set

`django_e6d7f4a0bb` · low · confidence medium · introduced in 4.1 · fires at first_use

Since 4.1, Model.full_clean converts an exclude value to a set. Code that passes exclude (e.g. as a list) to full_clean, or overrides these methods and relies on the exclude type, may see different behavior. The text states it is preferable to pass exclude as a set to clean_fields, full_clean, validate_unique and validate_constraints.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where Model.full_clean began converting exclude to a set (upgrading from 3.2 to 4.2). (confidence medium, judge partially_supported)
  - dj_notes@4.1: "The Model.full_clean method now converts an exclude value to a set."
- **[required] api_usage** `present` `"full_clean"`: The application calls or overrides Model.full_clean, clean_fields, validate_unique or validate_constraints with an exclude argument. (confidence medium, judge partially_supported)
  - dj_notes@4.1: "It's also preferable to pass an exclude value as a set to the Model.clean_fields, Model.full_clean, Model.validate_unique, and Model.validate_constraints methods."
  - ⚠ The text does not state what breaks if exclude is not passed as a set, only that a set is preferable.
- **[optional] behavior** `present` `"exclude=["`: The application passes exclude as a non-set type such as a list or tuple. (confidence low, judge partially_supported)
  - dj_notes@4.1: "It's also preferable to pass an exclude value as a set"

Actions:
- Search for calls to full_clean, clean_fields, validate_unique and validate_constraints that pass exclude and change them to pass a set.
- Review custom overrides of these methods that mutate or index into exclude, since full_clean now passes a set.
- Run model validation tests after upgrading.

### django.utils.timezone.utc now aliases datetime.timezone.utc

`django_f019e59923` · low · confidence medium · introduced in 4.0 · fires at upgrade

As part of the move to zoneinfo, django.utils.timezone.utc is changed to alias datetime.timezone.utc. Code that imports or relies on django.utils.timezone.utc as a distinct (pytz-based) object may behave differently. The text does not state specific breakages.

- **[required] version** `in_range` `{"current_version": "< 4.0", "target_version": ">= 4.0"}`: The upgrade crosses Django 4.0, where django.utils.timezone.utc was changed to alias datetime.timezone.utc. (confidence medium, judge partially_supported)
  - dj_notes@4.0: "django.utils.timezone.utc is changed to alias datetime.timezone.utc"
- **[required] api_usage** `present` `"django.utils.timezone.utc"`: The application uses django.utils.timezone.utc. (confidence medium, judge supported)
  - dj_notes@4.0: "django.utils.timezone.utc is changed to alias datetime.timezone.utc"
  - ⚠ The text does not describe which specific behaviors differ between the old object and datetime.timezone.utc.

Actions:
- Search the codebase for uses of django.utils.timezone.utc.
- Consider replacing django.utils.timezone.utc with datetime.timezone.utc directly.
- Run tests covering code that compares, serializes or inspects UTC tzinfo objects.

### OpenLayersWidget upgraded to OpenLayers 7.2.2

`django_ff6ba9a221` · low · confidence medium · introduced in 4.2 · fires at upgrade

The OpenLayersWidget in django.contrib.gis is now based on OpenLayers 7.2.2 instead of 4.6.5. Applications that use the widget, or customize it, may see differences in map behavior or rendering. The text does not state specific incompatibilities.

- **[required] version** `in_range` `{"current_version": "< 4.2", "target_version": ">= 4.2"}`: The upgrade crosses Django release 4.2, where OpenLayersWidget moved to OpenLayers 7.2.2. (confidence high, judge supported)
  - dj_notes@4.2: "OpenLayersWidget is now based on OpenLayers 7.2.2 (previously 4.6.5)."
- **[required] api_usage** `present` `"OpenLayersWidget"`: The application uses OpenLayersWidget (for example in GIS model admin or forms). (confidence medium, judge partially_supported)
  - dj_notes@4.2: "OpenLayersWidget is now based on OpenLayers 7.2.2"
  - ⚠ The text does not state what specific behavior differs between OpenLayers 4.6.5 and 7.2.2.
- **[uncertain] api_usage** `present` `"custom OpenLayersWidget template or JavaScript using the OpenLayers API"`: The application customizes the widget's JavaScript or templates, or relies on OpenLayers 4.6.5-specific APIs, which may be affected by the library version change. (confidence low)
  - dj_notes@4.2: "OpenLayersWidget is now based on OpenLayers 7.2.2 (previously 4.6.5)."
  - ⚠ The text does not say whether customizations are impacted.

Actions:
- Search for usage of OpenLayersWidget, including in admin GISModelAdmin and custom forms.
- Test map widgets in the browser after upgrading to confirm they render and function correctly.
- Review any custom OpenLayers JavaScript or template overrides written against OpenLayers 4.6.5 for compatibility with 7.2.2.

### ModelAdmin.actions and inlines default changed from list to tuple

`django_ff918e477f` · low · confidence medium · introduced in 4.1 · fires at first_use

The ModelAdmin.actions and inlines attributes now default to an empty tuple instead of an empty list. Code that mutates these inherited defaults in place (e.g. append/extend) will fail on a tuple.

- **[required] version** `in_range` `{"current_version": "< 4.1", "target_version": ">= 4.1"}`: The upgrade crosses Django 4.1, where the default of ModelAdmin.actions and inlines changed to an empty tuple. (confidence high, judge supported)
  - dj_notes@4.1: "The ModelAdmin.actions and inlines attributes now default to an empty tuple rather than an empty list"
- **[required] api_usage** `present` `"actions|inlines on ModelAdmin classes"`: The application uses ModelAdmin.actions or inlines attributes, in particular relying on the default value or mutating it. (confidence medium, judge supported)
  - dj_notes@4.1: "The ModelAdmin.actions and inlines attributes now default to an empty tuple rather than an empty list"
  - ⚠ The text does not state exactly which usage patterns break; mutation is only implied by the stated purpose of discouraging unintended mutation.
- **[uncertain] behavior** `unknown` `"in-place mutation of default actions/inlines"`: Code mutates the inherited default (e.g. appends to ModelAdmin.actions or inlines) rather than assigning its own list or tuple. (confidence low, judge partially_supported)
  - dj_notes@4.1: "to discourage unintended mutation"
  - ⚠ The text does not explicitly say that in-place mutation now raises an error.

Actions:
- Search ModelAdmin subclasses and admin site code for in-place mutation of actions or inlines and replace it with assignment of a new list or tuple.
- Ensure code treating these attributes as lists does not rely on list-only behavior.

## Review checklist

### Low confidence or disputed

- [ ] django_594eb9c388: MariaDB 10.2 no longer supported
- [ ] django_bd48e50291: MySQL 5.7 database no longer supported
- [ ] django_da674827bd: MariaDB 10.3 database no longer supported
- [ ] django_0bf0a41371: Expression.get_group_by_cols() subclasses must accept alias=None
- [ ] django_2da27e16b5: Third-party database backend overrides date/time DatabaseOperations methods with old field_name signatures
- [ ] django_4fceb7f197: get_random_string() called without length argument
- [ ] django_7a421fde8d: BaseCommand.requires_system_checks boolean value removed
- [ ] django_e78cbd4ca0: MiddlewareMixin.__init__ get_response required
- [ ] django_17b16d25e5: has_case_insensitive_like default changed from True to False for third-party database backends
- [ ] django_18e8b24987: DeleteView custom delete() logic must move to form_valid()
- [ ] django_51eedd8b4d: Sliced queryset unsupported operations now raise TypeError instead of AssertionError
- [ ] django_80d51ec58c: USE_L10N default changed from False to True
- [ ] django_905d3a6384: Custom database backend overrides year_lookup_bounds_for_date_field/year_lookup_bounds_for_datetime_field without iso_year argument
- [ ] django_d556e0f842: Manually instantiated WSGIRequest requires file-like wsgi.input
- [ ] django_e8dd99cb1e: set_language() no longer stores user language in request.session
- [ ] django_f332589611: OpenLayers widget map_css block removed and inline CSS dropped
- [ ] django_50a921cea2: QuerySet.iterator() with prefetch_related and no chunk_size
- [ ] django_65b3b830af: InlineModelAdmin.verbose_name_plural fallback change
- [ ] django_68ec37b26b: Email attach/attach_alternative exception type changed from AssertionError to ValueError
- [ ] django_7019792cec: Session cookies hidden in error reports
- [ ] django_910ce87d08: CSS form media link tags no longer include type="text/css"
- [ ] django_a03bfcb268: GeoJSON serializer output now includes id key

### Inferred conditions

- [ ] django_11d22d1a94: The application runs on a Python version newer than 3.12, which is not in the listed supported versions.
- [ ] django_0bf0a41371: The overriding get_group_by_cols() signature does not already include alias=None.
- [ ] django_2da27e16b5: The project uses only Django's built-in database backends and does not override or call these methods.
- [ ] django_4fceb7f197: All get_random_string() calls already pass an explicit length, so the risk does not apply.
- [ ] django_7a421fde8d: The application has no custom commands that set requires_system_checks to a boolean value.
- [ ] django_a0a165bd4b: CSRF_TRUSTED_ORIGINS is not already configured to cover the subdomain origins.
- [ ] django_e78cbd4ca0: The application instantiates a MiddlewareMixin subclass directly, or calls its __init__, without get_response or with get_response=None.
- [ ] django_00ef9fd5ad: The custom save() already adds the modified fields to update_fields before calling super(), so the risk does not apply.
- [ ] django_17b16d25e5: The backend's DatabaseFeatures explicitly sets has_case_insensitive_like, so the new default does not apply.
- [ ] django_18e8b24987: The application's DeleteView subclasses already implement deletion in form_valid() or a shared helper, so no custom delete() logic remains.
- [ ] django_21dcaab3e7: The application relies on cross-origin popups or windows sharing the same browsing context (e.g. OAuth/payment popups communicating via window.opener).
- [ ] django_21e9ff39c5: The application overrides or calls get_search_results, which followed the old sequential-filter behavior in 4.0 and earlier.
- [ ] django_21e9ff39c5: Users or tests rely on multi-term admin searches returning parents whose different related rows each match different terms.
- [ ] django_279f3f0fb3: The application relies on the previous rendered HTML structure of these widgets, for example in CSS, JavaScript, or HTML assertions in tests.
- [ ] django_3b5ed48e22: The application validates models, for example via full_clean() or ModelForm/admin validation, so the new constraint checks can surface as validation errors.
- [ ] django_448b2e13b9: The asvar variable is output in HTML templates, where the new safe marking changes escaping behavior.
- [ ] django_4c5ef340ee: Application code, raw SQL, or tooling depends on serial columns or their sequences (for example, sequence names or pg_get_serial_sequence).
- [ ] django_51eedd8b4d: The application performs operations on sliced querysets that are unsupported (e.g. filtering/ordering after slicing) and catches or asserts AssertionError for them.
- [ ] django_7a4215cfe6: The expression already sets output_field explicitly, in which case the crash does not apply.
- [ ] django_80d51ec58c: The project does not set USE_L10N explicitly in its settings, so it relies on the old default of False.
- [ ] django_8f4e0280c3: The email server presents a hostname or certificate that does not pass verification, so the previous less restrictive behavior is needed.
- [ ] django_8f4e0280c3: The application already subclasses EmailBackend and overrides ssl_context, in which case it controls its own verification behavior.
- [ ] django_905d3a6384: The project uses only Django's built-in database backends and does not override or call these methods.
- [ ] django_ab11d5f38a: CI or automation relies on the exit code of the Django test runner (manage.py test).
- [ ] django_c1af6215cc: Sessions in the old format are all expired or were re-created under Django 3.1 or later before the upgrade, so none remain in the pre-3.1 format.
- [ ] django_d556e0f842: The environ passed to WSGIRequest sets wsgi.input to something that is not a file-like object, for example a string, bytes or None.
- [ ] django_d8509a5a51: The application already uses BaseUserCreationForm instead of UserCreationForm for the previous behavior.
- [ ] django_e8dd99cb1e: The application code reads the _language key from request.session to get the user language.
- [ ] django_ecd275c5ed: The application uses Pillow-dependent Django features such as ImageField.
- [ ] django_f332589611: The application overrides or extends the OpenLayers widget template and uses the map_css block.
- [ ] django_ff4e75de71: The project sets USE_L10N to False, so floatformat previously produced non-localized output that will now be localized.
- [ ] django_ffb36c7ea4: Messages stored in the pre-Django 3.2 format may still exist, such as in cookies created before 3.2 and still unexpired.
- [ ] django_0190ffdbe6: Code, tests, caches or clients depend on gzip response bytes or length being deterministic.
- [ ] django_1163fb83c9: The collected static JavaScript files contain source map references that are now rewritten to hashed paths.
- [ ] django_205678f117: The application depends on edits in list_editable being non-atomic, for example relying on partial saves or on custom save/signal logic that is sensitive to transaction boundaries.
- [ ] django_48318ce619: The application overrides or references the 'list' error message key for ModelMultipleChoiceField (e.g. in error_messages or in tests/templates).
- [ ] django_50a921cea2: The queryset passed to iterator() prefetches related objects (for example via prefetch_related or Prefetch).
- [ ] django_51841a4bc3: The application code or client-side scripts read the CSRF cookie value directly and assume it is masked.
- [ ] django_5f49526547: Code, tests or configuration depend on the previous iteration count of 390,000.
- [ ] django_5f49526547: The application overrides the iterations value in a custom PBKDF2 hasher subclass, so the new default may not apply.
- [ ] django_65b3b830af: The inline does not explicitly set verbose_name_plural, so the new fallback applies.
- [ ] django_68ec37b26b: The application or its tests catch or assert AssertionError around these attach calls, and invalid content or mimetype arguments can be passed.
- [ ] django_7019792cec: The application or its operations rely on seeing session cookie values in Django error reports.
- [ ] django_7efc1311fa: Code or tests compare generated feed XML textually, or a consumer parses it in a way sensitive to self-closing versus open/close empty tags.
- [ ] django_910ce87d08: The application renders CSS form media (e.g. forms or widgets with Media css) and depends on the type="text/css" attribute being present in the rendered <link> tags, such as in tests asserting HTML output or in CSS/JS selectors.
- [ ] django_9b38717bcc: The application or its tests catch or assert AssertionError from FileSystemStorage.delete().
- [ ] django_a03bfcb268: Tests or downstream consumers compare or strictly validate the exact GeoJSON feature structure, so the added id key could cause a mismatch.
- [ ] django_b7d77765c8: The logger or handler level is set to DEBUG or lower so the new DEBUG-level messages are emitted, increasing log output.
- [ ] django_cd2220a8df: The application passes lazy objects, such as lazy translation strings or SimpleLazyObject instances, to mark_safe.
- [ ] django_e6d7f4a0bb: The application passes exclude as a non-set type such as a list or tuple.
- [ ] django_ff6ba9a221: The application customizes the widget's JavaScript or templates, or relies on OpenLayers 4.6.5-specific APIs, which may be affected by the library version change.
- [ ] django_ff918e477f: Code mutates the inherited default (e.g. appends to ModelAdmin.actions or inlines) rather than assigning its own list or tuple.

### Source disagreements


### Open questions

- Third-party packages (django-rest-framework, celery, database drivers other than psycopg2) pin Django versions; compatibility is not covered by Django's docs.
- Patch releases are scanned only for reverts, not for new incompatibilities.
- Tier-2 sources (Django Trac tickets, forum threads) were not mined; real-world triggers such as CSRF failures behind TLS-terminating proxies may be under-represented.
- Revert note in 4.1.2 not linked to a risk path (unresolved: The note reverts the caching of related managers, which is a different 4.1 change. None of the candidates describes manager caching. The reverse FK )
- [django_11d22d1a94] Unconfirmed: The application runs on a Python version newer than 3.12, which is not in the listed supported versions. (The text does not say whether Python versions newer than 3.12 work or fail with Django 4.2.)
- [django_594eb9c388] Unconfirmed: The deployment uses a MariaDB database server at version 10.2 (less than 10.3) with Django. (The text does not state exactly how Django behaves on an unsupported MariaDB 10.2 server (e.g. error at startup vs. unsupported/untested).)
- [django_bd48e50291] Unconfirmed: The deployment uses a MySQL database server at version 5.7. (The text does not say whether Django 4.2 actively fails on MySQL 5.7 or merely no longer supports it.)
- [django_da674827bd] Unconfirmed: The deployment uses a MariaDB database server older than 10.4 (e.g. 10.3). (The text does not state how Django 4.2 behaves on MariaDB 10.3 (e.g. error at startup or merely unsupported).)
- [django_2da27e16b5] Unconfirmed: The project uses only Django's built-in database backends and does not override or call these methods. (Judge: evidence does not support this claim. The quote only says the changes may be needed in third-party backends; it does not establish that projects using only built-in backends are unaffected or t)
- [django_4fceb7f197] Unconfirmed: All get_random_string() calls already pass an explicit length, so the risk does not apply. (Judge: evidence does not support this claim. The quote only says length will be required; it does not establish that all calls already pass an explicit length or that the risk does not apply. The clai)
- [django_7a421fde8d] Unconfirmed: The application has no custom commands that set requires_system_checks to a boolean value. (Judge: evidence does not support this claim. The quote only says boolean support is removed in 4.1; it says nothing about applications lacking such custom commands. The claim describes an unaffected s)
- [django_a0a165bd4b] Unconfirmed: CSRF_TRUSTED_ORIGINS is not already configured to cover the subdomain origins. (The text says only that setting it 'may' be needed and does not give the required format or values.)
- [django_17b16d25e5] Unconfirmed: The backend's DatabaseFeatures explicitly sets has_case_insensitive_like, so the new default does not apply. (The text does not explicitly discuss overrides; this follows from the change being to the base class default.)
- [django_18e8b24987] Unconfirmed: The application's DeleteView subclasses already implement deletion in form_valid() or a shared helper, so no custom delete() logic remains. (Judge: evidence does not support this claim. The quote only says that in 4.0 DeleteView handles POST deletion in form_valid(). It does not establish that the application's subclasses already implement)
- [django_21e9ff39c5] Unconfirmed: Users or tests rely on multi-term admin searches returning parents whose different related rows each match different terms. (The text does not state whether any given application relies on the old matching behavior.)
- [django_279f3f0fb3] Unconfirmed: The application relies on the previous rendered HTML structure of these widgets, for example in CSS, JavaScript, or HTML assertions in tests. (The text does not describe the previous markup, so which CSS selectors or tests are affected is not stated.)
- [django_3b5ed48e22] Unconfirmed: The application validates models, for example via full_clean() or ModelForm/admin validation, so the new constraint checks can surface as validation errors. (The text does not name the specific validation entry points (full_clean, ModelForm, admin) or the resulting error behavior.)
- [django_448b2e13b9] Unconfirmed: The asvar variable is output in HTML templates, where the new safe marking changes escaping behavior. (The text does not state the previous escaping behavior or specific impact on rendered output.)
- [django_8f4e0280c3] Unconfirmed: The email server presents a hostname or certificate that does not pass verification, so the previous less restrictive behavior is needed. (The text does not describe the specific failure mode or what counts as failing verification.)
- [django_905d3a6384] Unconfirmed: The project uses only Django's built-in database backends and does not override or call these methods. (Judge: evidence does not support this claim. The quote says only that third-party backends may need changes. It does not say that projects using only built-in backends, or projects that neither overri)
- [django_ffb36c7ea4] Unconfirmed: Messages stored in the pre-Django 3.2 format may still exist, such as in cookies created before 3.2 and still unexpired. (The text does not state what happens to messages in the old format after removal.)
- [django_205678f117] Unconfirmed: The application depends on edits in list_editable being non-atomic, for example relying on partial saves or on custom save/signal logic that is sensitive to transaction boundaries. (The text does not describe what behavior differs or what impact the atomic transactions have on existing code.)
- [django_48318ce619] Unconfirmed: The application overrides or references the 'list' error message key for ModelMultipleChoiceField (e.g. in error_messages or in tests/templates). (The text does not state how the message is referenced (the key name, where it is used) or what replaces it.)
- [django_a03bfcb268] Unconfirmed: Tests or downstream consumers compare or strictly validate the exact GeoJSON feature structure, so the added id key could cause a mismatch. (The text does not state how the id key is configured or disabled, or whether any consumers are affected.)
- [django_cd2220a8df] Unconfirmed: The application passes lazy objects, such as lazy translation strings or SimpleLazyObject instances, to mark_safe. (The text does not specify which kinds of lazy objects are affected.)
- [django_ff6ba9a221] Unconfirmed: The application customizes the widget's JavaScript or templates, or relies on OpenLayers 4.6.5-specific APIs, which may be affected by the library version change. (The text does not say whether customizations are impacted.)
- [django_ff918e477f] Unconfirmed: Code mutates the inherited default (e.g. appends to ModelAdmin.actions or inlines) rather than assigning its own list or tuple. (The text does not explicitly say that in-place mutation now raises an error.)

## Context facts (not risks)

- (4.0) The new django.core.cache.backends.redis.RedisCache cache backend provides built-in support for caching with Redis. — _The item announces a new, additive RedisCache backend. The redis-py 3.0.0 requirement applies only if an application opts in to the new backend, and the text states no change to existing behavior or required action when upgrading 3.2 -> 4.2._
- (4.0) Forms, Formsets, and ErrorList are now rendered using the template engine to enhance customization. — _The item only states that Forms, Formsets, and ErrorList are now rendered using the template engine, and names the new render, get_context, and template_name APIs. It describes no removed API, changed default, required configuration, or migration step, and it states no breaking impact or required user action. It is an additive feature, so no risk path can be supported from this text alone._
- (4.0) jQuery is upgraded from version 3.5.1 to 3.6.0. — _The item only states that the bundled jQuery in the admin is upgraded from 3.5.1 to 3.6.0. It describes no removed API, changed behavior, or required user action, so it is informational and needs no action at 4.2._
- (4.0) BaseFormSet now renders non-form errors with an additional class of nonform to help distinguish them from form-specific errors. — _The release notes describe an additive change: BaseFormSet non-form errors are rendered with an extra CSS class, nonform, alongside the existing classes. The text states no removed API, changed signature or required migration, so no action is needed at 4.2. The text does not say whether any application relies on the exact rendered markup._
- (4.0) The shell command now respects sys.interactivehook at startup. — _The shell command now respects sys.interactivehook, which allows loading shell history between interactive sessions. As a consequence, readline is no longer loaded when running in isolated mode. This only affects interactive shell convenience such as line editing and history, and only in isolated mode. The text describes no application breakage, migration work or operational risk, so no action is needed at 4.2._
- (4.0) To allow serving a Django site on a subpath without changing the value of STATIC_URL, the leading slash is removed from that setting (now 'static/') in the default startproject template. — _The change only affects the default startproject template, where STATIC_URL is now 'static/' without the leading slash. The text does not say that existing projects or their STATIC_URL values change, so no action is needed when upgrading an existing project to 4.2. It only affects newly generated projects._
- (4.0) These features have reached the end of their deprecation cycle and are removed in Django 4.0. — _The item is only the introductory sentence of the 'Features removed in 4.0' section. It says that features whose deprecation cycle has ended are removed in 4.0, and it names no specific API, setting or behavior that an application could be checked against. The individual removals (for example urlquote, force_text, ugettext, is_ajax, NullBooleanField, django.conf.urls.url) are separate list entries and should be assessed as their own items._
- (4.1) The admin dark mode CSS variables are now applied in a separate stylesheet and template block. — _The item only says the admin dark mode CSS variables are now applied in a separate stylesheet and template block. It describes an additive, cosmetic admin change. The text states no removed API, changed default, or required user action, so no risk path is warranted at 4.2._
- (4.1) ManifestStaticFilesStorage now replaces paths to CSS source map references with their hashed counterparts. — _The 4.1 release notes list this under minor features. ManifestStaticFilesStorage now rewrites CSS source map references to their hashed counterparts. The text states no removal, incompatibility, required configuration or migration step, so no action is required at 4.2._
- (4.1) The default template used to render forms when cast to a string, e.g. — _This is an additive feature. The default form template can now be set per project via form_template_name on the FORM_RENDERER class, and formsets get a matching formset_template_name attribute. Form.template_name is now a property deferring to the renderer, but the text says it may still be overridden with a string per form class. The text states no required action at 4.2. The div-based output only becomes the default from Django 5.0, and the transitional renderers are opt-in._
- (4.1) Python files created by startproject, startapp, optimizemigration, makemigrations, and squashmigrations are now formatted using the black command if it is present on your PATH. — _The item describes an additive, opt-in-by-presence behavior: generated Python files are formatted with black only if it is on PATH. It does not remove or break any API, require action, or change runtime requirements. At most, generated file formatting may differ cosmetically, and the text states no required action or breakage._
- (4.1) The migrations autodetector now generates RenameIndex operations instead of RemoveIndex and AddIndex, when renaming indexes defined in the Meta.indexes. — _The change improves the migrations autodetector: renamed indexes in Meta.indexes now produce a RenameIndex operation instead of RemoveIndex and AddIndex. The text names no removed API, no required user action and no breakage. It is an additive improvement to generated migrations, so it needs no action at 4.2._
- (4.1) The migrations autodetector now generates RenameIndex operations instead of AlterIndexTogether and AddIndex, when moving indexes defined in the Meta.index_together to the Meta.indexes. — _The item describes an improvement to the migrations autodetector: when indexes move from Meta.index_together to Meta.indexes, it now generates RenameIndex operations instead of AlterIndexTogether and AddIndex. The text states no breakage, removal, required action, or operational risk. It is an additive, behavior-improving change that needs no action at 4.2._
- (4.1) The pre_delete and post_delete signals now dispatch the origin of the deletion. — _The item describes an additive feature: pre_delete and post_delete signals now dispatch the origin of the deletion. The text states no removed API, changed existing behavior, or required user action, so existing receivers continue to work without changes at 4.2._
- (4.1) The makemessages command no longer changes .po files when up to date. — _The makemessages command now leaves .po files unchanged when they are already up to date, where older versions always updated POT-Creation-Date. The text describes no breakage, removed API, or migration step, so no action is required at 4.2._
- (4.2) Django now supports psycopg version 3.1.8 or higher. — _Psycopg 3 support is additive and optional. The text says django.db.backends.postgresql supports both libraries, so existing psycopg2 deployments need no change at 4.2. Support for psycopg2 is only 'likely to be deprecated and removed at some point in the future', with no version or date given. The breaking changes in psycopg 3 matter only if an application chooses to switch libraries, and the text does not name them._
- (4.2) The admin's font stack now prefers system UI fonts and no longer requires downloading fonts. — _The item describes a cosmetic admin change: the font stack prefers system UI fonts and CSS variables are now available to override font families. It states no removed API, required migration, or breaking behavior, and no user action is needed at 4.2. Customizing the font families is optional._
- (4.2) UserCreationForm now saves many-to-many form fields for a custom user model. — _The item describes a bug-fix-style improvement: UserCreationForm now also saves many-to-many form fields for a custom user model. It is additive and the text states no breaking change, removal, required migration or operational risk, so no user action is required at 4.2._
- (4.2) Now now supports microsecond precision on MySQL and millisecond precision on SQLite. — _The item only states that Now() gained microsecond precision on MySQL and millisecond precision on SQLite. It is an additive improvement in the Minor features list. It names no removed API, no required migration step, and no breaking change, so no user action is required at 4.2._
- (4.2) The private internal vendored copy of urllib.parse.urlsplit() now strips '\r', ' ', and '\t' (see 2022-0391 and 43882). — _This is a security hardening of a private internal vendored copy of urllib.parse.urlsplit(). The text says it protects projects that may be incorrectly using the internal url_has_allowed_host_and_scheme() function and that "The Django functions were not affected." It states no breakage, removed API or required migration, and it asks for no user action at 4.2._
- (4.2) The list of common passwords used by CommonPasswordValidator is updated to the most recent version. — _The release note only says the CommonPasswordValidator common-password list was updated to the most recent version. It names no removed API, changed setting or required migration, so no action is required at 4.2. The text does not say which passwords are affected, so any impact on existing password fixtures or tests is not stated._
- (4.2) The autofocus HTML attribute in the admin search box is removed as it can be confusing for screen readers. — _The admin search box no longer renders the autofocus HTML attribute, for accessibility reasons. The text states no API removal, setting change or migration step, so no user action is required. The only effect is that the search box no longer takes focus automatically on page load._
- (4.0) This section describes changes that may be needed in third-party database backends. — _This is only an introductory pointer stating that the following section concerns third-party database backends, with no change itself._
- (4.0) As part of the move to zoneinfo, use of pytz time zones is deprecated. — _Use of pytz time zones is deprecated but still works, so this produces only warnings at this release._
- (4.0) django.db.models.query.QuerySet.datetimes — _QuerySet.datetimes is listed as a pytz-related deprecation in 4.0, so it still works and only warns._
- (4.0) django.db.models.functions.Trunc — _The Trunc function is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncSecond — _TruncSecond is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncMinute — _TruncMinute is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncHour — _TruncHour is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncDay — _TruncDay is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncWeek — _TruncWeek is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncMonth — _TruncMonth is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncQuarter — _TruncQuarter is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.db.models.functions.TruncYear — _TruncYear is listed under the pytz deprecation, which warns but does not yet break existing code._
- (4.0) django.utils.timezone.make_aware — _make_aware is listed under the pytz deprecation, which warns but still works in this release._
- (4.0) Support for use of pytz will be removed in Django 5.0. — _The pytz removal is scheduled for Django 5.0, so it requires no action for an upgrade ending at 4.2._
- (4.0) In order to follow good practice, the default value of the USE_TZ setting will change from False to True, and time zone support will be enabled by default, in Django 5.0. — _The USE_TZ default change is scheduled for Django 5.0, after this upgrade target, and the text notes it can be opted out of before then._
- (4.0) SERIALIZE test setting is deprecated as it can be inferred from the databases with the serialized_rollback option enabled. — _The SERIALIZE test setting is deprecated but still functions, so it only triggers a warning._
- (4.0) The undocumented django.utils.baseconv module is deprecated. — _The undocumented baseconv module is deprecated with a warning and still works._
- (4.0) The undocumented django.utils.datetime_safe module is deprecated. — _The undocumented datetime_safe module is deprecated with a warning and still works._
- (4.0) The default sitemap protocol for sitemaps built outside the context of a request will change from 'http' to 'https' in Django 5.0. — _The sitemap protocol default change is scheduled for Django 5.0, beyond this upgrade's target._
- (4.0) The extra_tests argument for DiscoverRunner.build_suite and DiscoverRunner.run_tests is deprecated. — _The extra_tests argument is deprecated but still accepted, so only a warning is produced._
- (4.0) The ArrayAgg, JSONBAgg, and StringAgg aggregates will return None when there are no rows instead of [], [], and '' respectively in Django 5.0. — _The aggregate return-value change is scheduled for Django 5.0, and the text gives an explicit way to keep the old behavior._
- (4.0) The django.contrib.gis.admin.GeoModelAdmin and OSMGeoAdmin classes are deprecated. — _GeoModelAdmin and OSMGeoAdmin are deprecated with replacements named, so they still work and need no action at this release._
- (4.0) Since form rendering now uses the template engine, the undocumented BaseForm._html_output() helper method is deprecated. — _The undocumented BaseForm._html_output() is only deprecated, so it still functions and requires no action now._
- (4.0) The ability to return a str from ErrorList and ErrorDict is deprecated. — _Returning a str from ErrorList and ErrorDict is merely deprecated, so existing code keeps working for now._
- (4.0) See deprecated-features-3.1 for details on these changes, including how to remove usage of these features. — _This is only a pointer to the 3.1 deprecation notes and requires no action by itself._
- (4.1) Related managers for ForeignKey, ManyToManyField, and GenericRelation are now cached on the Model instance to which they belong. — _The caching change was reverted in Django 4.1.2, so it has no effect on upgrading to the release and needs no user action._
- (4.1) Logging out via GET requests to the built-in logout view is deprecated. — _Logging out via GET is deprecated but still works, so it needs no immediate action beyond planning a move to POST._
- (4.1) The context for sitemap index templates of a flat list of URLs is deprecated. — _The flat-list sitemap index context is deprecated with only a warning, so custom templates can be updated later without breaking now._
- (4.1) CSRF_COOKIE_MASKED transitional setting is deprecated. — _The CSRF_COOKIE_MASKED setting is only deprecated, so it still works and needs no action in this release._
- (4.1) The name argument of django.utils.functional.cached_property is deprecated as it's unnecessary as of Python 3.6. — _The name argument of cached_property is deprecated but still accepted, so existing code keeps working._
- (4.1) The undocumented ability to pass errors=None to SimpleTestCase.assertFormError and assertFormsetError() is deprecated. — _Passing errors=None to assertFormError is deprecated while errors=[] is the replacement, so tests keep working for now._
- (4.1) Passing unsaved model instances to related filters is deprecated. — _Passing unsaved model instances to related filters only emits a deprecation warning now and the exception comes in Django 5.0._
- (4.1) The django.utils.timezone.utc alias to datetime.timezone.utc is deprecated. — _The django.utils.timezone.utc alias is deprecated but still works, so only a warning is produced._
- (4.1) Passing a response object and a form/formset name to SimpleTestCase.assertFormError() and assertFormsetError() is deprecated. — _Passing a response object with a form name to assertFormError is deprecated but still functions, and the replacement pattern is given._
- (4.1) The undocumented django.contrib.gis.admin.OpenLayersWidget is deprecated. — _The undocumented OpenLayersWidget is deprecated, which only produces a warning._
- (4.1) django.contrib.auth.hashers.CryptPasswordHasher is deprecated. — _CryptPasswordHasher is deprecated but remains available, so no immediate action is needed._
- (4.1) The ability to pass nulls_first=False or nulls_last=False to Expression.asc() and Expression.desc() methods, and the OrderBy expression is deprecated. — _Passing nulls_first=False or nulls_last=False is deprecated in favor of None, but the old form still works._
- (4.1) The "django/forms/default.html" and "django/forms/formsets/default.html" templates which are a proxy to the table-based templates are deprecated. — _The default.html form templates are deprecated proxies that still work, and the specific templates are the recommended replacement._
- (4.1) These features have reached the end of their deprecation cycle and are removed in Django 4.1. — _This is a documentation pointer to the 3.2 deprecated-features notes and requires no direct action in itself._
- (4.2) Should become: class Author(models.Model): rank = models.IntegerField() name = models.CharField(max_length=30) class Meta: indexes = [models.Index(fields=["rank", "name"])] — _This is a code example showing the replacement indexes option, serving as a documentation pointer with no required action by itself._
- (4.2) Should become: Document.objects.bulk_create( Document(data=Value(None, JSONField())), Document(data=[]), Document(data="foo-bar"), ) Document.objects.annotate( JSONBAgg("field", default=[]), ) — _This example shows the recommended replacement form for JSONField values and is documentation guidance only._
- (4.2) The BaseUserManager.make_random_password() method is deprecated. — _BaseUserManager.make_random_password() is only deprecated, so it still works and the item points to a recommended alternative._
- (4.2) The length_is template filter is deprecated in favor of length and the == operator within an {% if %} tag. — _The length_is template filter is deprecated but still functional, and the item gives a replacement pattern with no required action now._
- (4.2) django.contrib.auth.hashers.SHA1PasswordHasher, django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher, and django.contrib.auth.hashers.UnsaltedMD5PasswordHasher are deprecated. — _The SHA1 and MD5 password hashers are deprecated but remain available, so no immediate action is required._
- (4.2) django.contrib.postgres.fields.CICharField is deprecated in favor of CharField(db_collation="...") with a case-insensitive non-deterministic collation. — _CICharField is deprecated in favor of CharField with a non-deterministic collation, and the deprecated field still works in this release._
- (4.2) django.contrib.postgres.fields.CIEmailField is deprecated in favor of EmailField(db_collation="...") with a case-insensitive non-deterministic collation. — _CIEmailField is deprecated in favor of EmailField with db_collation, and the old field still functions in this release._
- (4.2) django.contrib.postgres.fields.CITextField is deprecated in favor of TextField(db_collation="...") with a case-insensitive non-deterministic collation. — _CITextField is deprecated in favor of TextField with db_collation, and the old field still functions in this release._
- (4.2) django.contrib.postgres.fields.CIText mixin is deprecated. — _The CIText mixin is deprecated but still available, so it needs no action at this release._
- (4.2) The map_height and map_width attributes of BaseGeometryWidget are deprecated, use CSS to size map widgets instead. — _The map_height and map_width attributes are deprecated, but they still work and the item recommends CSS sizing as an optional alternative._
- (4.2) SimpleTestCase.assertFormsetError() is deprecated in favor of assertFormSetError(). — _SimpleTestCase.assertFormsetError() is deprecated in favor of assertFormSetError(), a warning-level deprecation that still works._
- (4.2) TransactionTestCase.assertQuerysetEqual() is deprecated in favor of assertQuerySetEqual(). — _The item says assertQuerysetEqual() is deprecated in favor of assertQuerySetEqual(), which is a warning-only deprecation with no required change at this release._
- (4.2) Passing positional arguments to Signer and TimestampSigner is deprecated in favor of keyword-only arguments. — _Passing positional arguments to Signer and TimestampSigner is deprecated in favor of keyword-only arguments, so existing code keeps working for now._
- (4.2) The DEFAULT_FILE_STORAGE setting is deprecated in favor of STORAGES["default"]. — _The DEFAULT_FILE_STORAGE setting is deprecated in favor of STORAGES["default"], and the old setting still functions at this release._
- (4.2) The STATICFILES_STORAGE setting is deprecated in favor of STORAGES["staticfiles"]. — _The STATICFILES_STORAGE setting is deprecated in favor of STORAGES["staticfiles"], and the deprecated setting still works at this release._
- (4.2) The django.core.files.storage.get_storage_class() function is deprecated. — _The get_storage_class() function is deprecated, which is a warning-only change that does not require action in this release._
- (4.1) See the Django 3.2 release notes for more details on these changes. — _The text is only a pointer to the Django 3.2 release notes and describes no change requiring user action._
- (4.0) See the Django 3.0 release notes for more details on these changes. — _This is a documentation pointer to the Django 3.0 release notes and requires no action at this release._
- (4.0) See the Django 3.1 release notes for more details on these changes. — _This is a documentation pointer to the Django 3.1 release notes and requires no action at this release._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): See the Django 4.2 release notes for more details on these changes. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The BaseUserManager.make_random_password() method will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The model's Meta.index_together option will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The length_is template filter will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The django.contrib.auth.hashers.SHA1PasswordHasher, django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher, and django.contrib.auth.hashers.UnsaltedMD5PasswordHasher will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The model django.contrib.postgres.fields.CICharField, django.contrib.postgres.fields.CIEmailField, and django.contrib.postgres.fields.CITextField will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The django.contrib.postgres.fields.CIText mixin will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The map_width and map_height attributes of BaseGeometryWidget will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The SimpleTestCase.assertFormsetError() method will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The TransactionTestCase.assertQuerysetEqual() method will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): Support for passing encoded JSON string literals to JSONField and associated lookups and expressions will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): Support for passing positional arguments to Signer and TimestampSigner will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The DEFAULT_FILE_STORAGE and STATICFILES_STORAGE settings will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.1) Scheduled for removal in 5.1 (after target 4.2): The django.core.files.storage.get_storage_class() function will be removed. — _Still works at 4.2; it is removed only in 5.1, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): See the Django 4.0 release notes for more details on these changes. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The SERIALIZE test setting will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The undocumented django.utils.baseconv module will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The undocumented django.utils.datetime_safe module will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The default value of the USE_TZ setting will change from False to True. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The default sitemap protocol for sitemaps built outside the context of a request will change from 'http' to 'https'. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The extra_tests argument for DiscoverRunner.build_suite() and DiscoverRunner.run_tests() will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The django.contrib.postgres.aggregates.ArrayAgg, JSONBAgg, and StringAgg aggregates will return None when there are no rows instead of [], [], and '' respectively. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The USE_L10N setting will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The USE_DEPRECATED_PYTZ transitional setting will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): Support for pytz timezones will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The is_dst argument will be removed from: * QuerySet.datetimes() * django.utils.timezone.make_aware() * django.db.models.functions.Trunc() * django.db.models.functions.TruncSecond() * django.db.models.functions.TruncMinute() * django.db.models.functions.TruncHour() * django.db.models.functions.TruncDay() * django.db.models.functions.TruncWeek() * django.db.models.functions.TruncMonth() * django.db.models.functions.TruncQuarter() * django.db.models.functions.TruncYear() — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The django.contrib.gis.admin.GeoModelAdmin and OSMGeoAdmin classes will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The undocumented BaseForm._html_output() method will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The ability to return a str, rather than a SafeString, when rendering an ErrorDict and ErrorList will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): See the Django 4.1 release notes for more details on these changes. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The SitemapIndexItem.str() method will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The CSRF_COOKIE_MASKED transitional setting will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The name argument of django.utils.functional.cached_property() will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The opclasses argument of django.contrib.postgres.constraints.ExclusionConstraint will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The undocumented ability to pass errors=None to SimpleTestCase.assertFormError() and assertFormsetError() will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): django.contrib.sessions.serializers.PickleSerializer will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The usage of QuerySet.iterator() on a queryset that prefetches related objects without providing the chunk_size argument will no longer be allowed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): Passing unsaved model instances to related filters will no longer be allowed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): created=True will be required in the signature of RemoteUserBackend.configure_user() subclasses. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): Support for logging out via GET requests in the django.contrib.auth.views.LogoutView and django.contrib.auth.views.logout_then_login() will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The django.utils.timezone.utc alias to datetime.timezone.utc will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): Passing a response object and a form/formset name to SimpleTestCase.assertFormError() and assertFormsetError() will no longer be allowed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The django.contrib.gis.admin.OpenLayersWidget will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The django.contrib.auth.hashers.CryptPasswordHasher will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The "django/forms/default.html" and "django/forms/formsets/default.html" templates will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._
- (5.0) Scheduled for removal in 5.0 (after target 4.2): The ability to pass nulls_first=False or nulls_last=False to Expression.asc() and Expression.desc() methods, and the OrderBy expression will be removed. — _Still works at 4.2; it is removed only in 5.0, after the target (R6)._

## Disqualified candidates

- Reverted caching related managers for ForeignKey, ManyToManyField, and GenericRelation that caused the incorrect refreshing of related objects (#33984).: R1: a 4.1 change was reverted in 4.1.2, at or before the target; no extracted risk path matched it, so the revert is recorded on its own.

## Sources

| Source | Type | Tier | Status | Pinned ref |
|---|---|---|---|---|
| [dj_deprecation](https://docs.djangoproject.com/en/4.2/internals/deprecation/) | official_deprecation_notice | 1 | used | `branch:stable/4.2.x` |
| [dj_notes@4.0](https://docs.djangoproject.com/en/4.2/releases/4.0/) | official_release_notes | 1 | used | `branch:stable/4.2.x` |
| [dj_notes@4.1](https://docs.djangoproject.com/en/4.2/releases/4.1/) | official_release_notes | 1 | used | `branch:stable/4.2.x` |
| [dj_notes@4.2](https://docs.djangoproject.com/en/4.2/releases/4.2/) | official_release_notes | 1 | used | `branch:stable/4.2.x` |
| [dj_patch@4.1.2](https://docs.djangoproject.com/en/4.2/releases/4.1.2/) | official_release_notes | 1 | used | `branch:stable/4.2.x` |
| [dj_pypi@3.2](https://pypi.org/project/Django/3.2/) | package_registry_metadata | 1 | used | `pypi:3.2` |
| [dj_pypi@4.0](https://pypi.org/project/Django/4.0/) | package_registry_metadata | 1 | used | `pypi:4.0` |
| [dj_pypi@4.1](https://pypi.org/project/Django/4.1/) | package_registry_metadata | 1 | used | `pypi:4.1` |
| [dj_pypi@4.2](https://pypi.org/project/Django/4.2/) | package_registry_metadata | 1 | used | `pypi:4.2` |

## What we trusted and what we did not

- Trusted: package metadata for version numbers; official guides, release notes and changelogs pinned to a tag, branch or commit.
- Not trusted: LLM self-reported confidence, unpinned current pages when they disagree with pinned ones, any quote that fails exact match, transclusion stubs.
