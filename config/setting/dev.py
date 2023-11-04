from config.settings import *


SECRET_KEY = 'django-insecure-x3hca8q@6lavbm^&+2-@g*sr3z%=!ks1!*o8#^e^dxiw22yg^'
DEBUG = True
ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR.joinpath('/static')
MEDIA_ROOT = BASE_DIR.joinpath('media/')

STATICFILES_DIRS = [
    BASE_DIR/'static',
    BASE_DIR/'media',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'