import os
from pathlib import Path
import logging

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logger = logging.getLogger('settings')
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.environ.get('ENV')


def load_environment_variable(name: str) -> str:
    variable_value = os.environ.get(name, None)
    if not variable_value:
        raise ValueError(
            f'Brak zmienneś środowiskowej - {name}')
    return variable_value


SECRETS = {
    'DB_NAME': None,
    'DB_USER': None,
    'DB_PASSWORD': None,
    'DB_HOST': None,
    'DB_PORT': None,
    'SECRET_KEY': None,
}
if ENV == 'prod':

    DEBUG = False
    for secret in SECRETS.keys():
        SECRETS[secret] = load_environment_variable(secret)

    SECRET_KEY = SECRETS['SECRET_KEY']
    logger.warning('POSTGRES')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': SECRETS['DB_NAME'],
            'USER': SECRETS['DB_USER'],
            'PASSWORD': SECRETS['DB_PASSWORD'],
            'HOST': SECRETS['DB_HOST'],
            'PORT': SECRETS['DB_PORT'],
        }
    }
else:

    logger.warning('SQLITE')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    DEBUG = True
    SECRET_KEY = 'django-insecure-dummy'


# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CSRF_TRUSTED_ORIGINS = [ 'http://localhost', 'http://0.0.0.0', 'http://127.0.0.1:8000']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    "drf_spectacular",
    'images',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imageprocessor.urls'


WSGI_APPLICATION = 'imageprocessor.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

SPECTACULAR_SETTINGS = {
    'TITLE': 'Image Processor',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
