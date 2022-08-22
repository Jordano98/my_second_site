from my_second_site.settings import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2t0i*)x9xi7j_ao2^iwq4e^+%_k#_5gxf=#vx_*@esgueh6nl9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

#INSTALLED_APPS = []

#debugger config
DEBUGGER_ENABLE = True
INTERNAL_IPS = [
    '127.0.0.1',
]
#sites framework
SITE_ID = 1




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR /'static'
MEDIA_ROOT = BASE_DIR /'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS='SAMEORIGIN'
