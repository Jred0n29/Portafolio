from .base import *

DEBUG = True

ALLOWED_HOSTS = ['blogjredon.herokuapp.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddpvmbleddna1n',
        'USER': 'vjeqfirhefxgkf',
        'PASSWORD': '7b83aca5ac1d7e4e4c2de5ed7d6089c558e93e4d90dac73814cadbb95491a8d4',
        'HOST': 'ec2-44-205-112-253.compute-1.amazonaws.com',
        'PORT': 5432,
         
    }
}
STATICFILES_DIRS = (BASE_DIR,'static')
