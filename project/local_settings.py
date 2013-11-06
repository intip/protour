# coding: utf-8
DEBUG = True

TEMPLATE_DEBUG = True

MEDIA_ROOT = 'media/'

from unipath import Path

PROJECT_DIR = Path(__file__).parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portalturismo',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
