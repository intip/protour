import os

from settings import *

os.environ['REUSE_DB'] = "1"

INSTALLED_APPS.remove('south')

NOSE_ARGS = ['--with-yanc', '--verbosity=2', '-x', '-d']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_portalturismo',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
