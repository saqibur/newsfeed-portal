from typing import Any

from .base import *

SECRET_KEY:  str = get_key('KEY_NAME_HERE')
NEWSAPI_KEY: str = get_key('KEY_NAME_HERE')

DEBUG: bool = True

DATABASES: dict[dict[str, Any]] = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     '', # Change this to the name of your db, for example, `iglu-db`
        'USER':     '', # Username in your db
        'PASSWORD': '', # Corresponding password for the user
        'HOST':     'localhost',
        'PORT':     '5432', # Default Postgres port, change if required
    }
}
