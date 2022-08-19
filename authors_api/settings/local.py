from .base import *
from .base import env

DEBUG=True
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="0jbe^2cbog#tgqnhr)tqc0=#f!=!ilc1c8@dwcc5603pmk2dye")

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]