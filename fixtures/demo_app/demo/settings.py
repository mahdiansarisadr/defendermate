SECRET_KEY = "fixture-only"
DEBUG = True
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.postgres", "shop"]
USE_TZ = True
USE_L10N = True
CSRF_TRUSTED_ORIGINS = ["shop.example.com", "admin.example.com"]
DEFAULT_HASHING_ALGORITHM = "sha1"
DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql", "NAME": "demo"}}
