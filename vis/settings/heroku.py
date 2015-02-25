from .base import *
import os
import urlparse
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


# REDIS
redis_url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost:6959'))

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password,
        }
    }
}


# LOGGING
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
