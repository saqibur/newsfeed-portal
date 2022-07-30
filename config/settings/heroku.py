import os
from typing import Any

from .base import *

SECRET_KEY: str = get_key("KEY_NAME_HERE")
FROM_EMAIL: str = get_key("KEY_NAME_HERE")

DEBUG: bool = False

DATABASES: dict[dict[str, Any]] = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_key("DB_NAME"),
        "USER": get_key("DB_USER"),
        "PASSWORD": get_key("DB_PASS"),
        "HOST": get_key("DB_HOST"),
        "PORT": "5432",
    }
}
