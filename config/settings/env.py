import logging
from datetime import timedelta

# from django_project.config.utils import get_env_variable
from .base import *
from ..utils import get_env_variable

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable("DEBUG")

ENVIRONMENT_NAME = get_env_variable("ENVIRONMENT_NAME")

if DEBUG:
    # configuration for django debug toolbar
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'  # django debug toolbar middleware
    ]
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("SECRET_KEY")

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ASSETS_MEDIA_DIR, 'db.sqlite3'),
    }
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800  # 5MB limit.

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
}

WKHTMLTOPDF_CMD = get_env_variable("WKHTMLTOPDF_CMD", default='/usr/bin/wkhtmltopdf')

FLAG_ENABLE_SENTRY = get_env_variable("FLAG_ENABLE_SENTRY")

if FLAG_ENABLE_SENTRY:
    import sentry_sdk
    from sentry_sdk.integrations.celery import CeleryIntegration
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    sentry_logging = LoggingIntegration(
        level=logging.INFO,  # Capture info and above as breadcrumbs
        event_level=logging.ERROR,  # Send errors as events
    )

    integrations = [
        sentry_logging,
        DjangoIntegration(),
        CeleryIntegration(),
    ]

    sentry_sdk.init(
        dsn=get_env_variable("SENTRY_DNS"),
        integrations=integrations,

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
        environment=ENVIRONMENT_NAME,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s "
                          "%(process)d %(thread)d %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            }
        },
        "root": {"level": "INFO", "handlers": ["console"]},
        "loggers": {
            "django.db.backends": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": False,
            },
            # Errors logged by the SDK itself
            "sentry_sdk": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": False,
            },
            "django.security.DisallowedHost": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": False,
            },
        },
    }
