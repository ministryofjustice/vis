from .base import *
import dj_database_url

DJ_DATABASE_URL = os.environ.get('DATABASE_URL')
if DJ_DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DJ_DATABASE_URL)
    }

SECRET_KEY = os.environ.get('SECRET_KEY', '<not-used>')

PIPELINE_COMPILERS = ()
PIPELINE_ENABLED = True

ALLOWED_HOSTS = ['*']

DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
        },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
            },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
            },
    }
}
