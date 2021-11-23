from pathlib import Path
import os

BASE_DIR: Path = Path(__file__).resolve().parent.parent


def get_key(key_name: str) -> str:
    match os.environ.get(key_name, None):
        case str(SECRET_KEY):
            return SECRET_KEY
        case None:
            raise Exception(
                f"""
                You haven't configured a '{key_name}' for your environment yet.
                For help, please check `Environment Secrets` in the project README.
                """
            )


LOCAL_APPS: list[str] = [
    'news',
    'users',
]

THIRD_PARTY_APPS: list[str] = [
    'rest_framework',
    'django_apscheduler',
]

DJANGO_APPS: list[str] = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS: list[str] =  DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE: list[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF: str = 'config.urls'

TEMPLATES: list[str] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / '../templates' ],
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

WSGI_APPLICATION: str = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
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

LOGIN_REDIRECT_URL = 'user:home'

LANGUAGE_CODE: str  = 'en-us'
TIME_ZONE:     str  = 'UTC'
USE_I18N:      bool = True
USE_L10N:      bool = True
USE_TZ:        bool = True

STATIC_URL: str = '/static/'

DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

# django-aps configs #
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25 # Seconds
