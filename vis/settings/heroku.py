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

STATICFILES_STORAGE = 'core.storage.GulpManifestStaticFilesStorage'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

STATIC_URL = os.environ.get('STATIC_URL', '/static/')


# REDIS
if 'REDISTOGO_URL' in os.environ:
    redis_url = urlparse.urlparse(os.environ['REDISTOGO_URL'])

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


# EMAILS
if 'EMAIL_HOST_USER' in os.environ and 'EMAIL_HOST_PASSWORD' in os.environ:
    EMAIL_SUBJECT_PREFIX = '[VIS]'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_SSL = True
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = 465
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


CACHE_CONTROL_MAX_AGE = 60*60


# MEDUSA

INSTALLED_APPS += (
    'django_medusa',
)

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_DEPLOY_DIR = os.path.join(PROJECT_DIR, '_static_site')


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
