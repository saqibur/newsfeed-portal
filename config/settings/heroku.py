import os
from typing import Any

from .base import *

SECRET_KEY:  str = get_key('KEY_NAME_HERE')
NEWSAPI_KEY: str = get_key('KEY_NAME_HERE')

FROM_EMAIL: str = 'FROM@WHERE.COM'

DEBUG: bool = False

DATABASES: dict[dict[str, Any]] = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     os.environ.get('DB_NAME', None),
        'USER':     os.environ.get('DB_USER', None),
        'PASSWORD': os.environ.get('DB_PASS', None),
        'HOST':     os.environ.get('DB_HOST', None),
        'PORT':     '5432',
    }
}
