from .common import *
import mimetypes

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n!g4a%z6&gf@u@%pb^3u8gmd(wm6o39o0(z-yttslwnaxs7!h0"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# mimetypes.add_type("text/html", ".html", True)
# mimetypes.add_type("text/css", ".css", True)
