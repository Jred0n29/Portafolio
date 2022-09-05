from .base import *




DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'publicaciones',
        'USER': 'postgres',
        'PASSWORD': '2002',
        'HOST': 'localhost',
        'PORT': 5432,
         
    }
}
