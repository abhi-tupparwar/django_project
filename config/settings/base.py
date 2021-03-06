import os

# CONFIG_DIR points to config package (project/src/apps/config)
import sys

from corsheaders.defaults import default_headers

CONFIG_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# BASE_DIR points to starting point of the projects's base directory path (<project_name>/(config, apps))
BASE_DIR = os.path.abspath(os.path.join(CONFIG_DIR, '..'))

# ASSETS_MEDIA_DIR points to the top level directory (one directory up from BASE_DIR)
# assets, media, database, and venv will be located in this directory
ASSETS_MEDIA_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

# APPS_DIR points to the core package (project/src/apps).
# All custom apps and newly created apps will be located in this directory.
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, APPS_DIR)

BUILT_IN_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'debug_toolbar',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]

USER_DEFINED_APPS = [
    'apps.core',
]

INSTALLED_APPS = BUILT_IN_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

BUILT_IN_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THIRD_PARTY_MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

USER_DEFINED_MIDDLEWARE = []

MIDDLEWARE = BUILT_IN_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + USER_DEFINED_MIDDLEWARE

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangonew.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangonew.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-in'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files')  # project/core/static_files
]
STATIC_ROOT = os.path.join(ASSETS_MEDIA_DIR, 'assets')  # project/assets

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ASSETS_MEDIA_DIR, 'media')  # project/media

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    # API Versioning.
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',

    # Authentication.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    # DateTime formatting
    'DATETIME_FORMAT': '%d/%m/%Y, %I:%M %p',
}

SWAGGER_SETTINGS = {
    "PERSIST_AUTH": True,
    "SECURITY_DEFINITIONS": {
        # For session based auth.
        "Basic": {"type": "basic"},
        # For JWT token based auth.
        "JWT": {"name": "Authorization", "type": "apiKey", "in": "header"},
    },
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'token',
    'otp-token',
    'cancelToken',
    'permissions',
]
CORS_EXPOSE_HEADERS = [
    'token',
    'otp-token',
    'cancelToken',
    'permissions',
]
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'DELETE',
    'PUT',
    'PATCH'
)
SESSION_COOKIE_SAMESITE = None
