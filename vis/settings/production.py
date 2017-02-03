from .base import *
import os



SECRET_KEY = os.environ.get('SECRET_KEY', '<not-used>')

PIPELINE_COMPILERS = ()
PIPELINE_ENABLED = True

ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"]

DEBUG = False
#review-2017
TEMPLATE_DEBUG = DEBUG

#review-2017
#STATICFILES_STORAGE = 'core.storage.GulpManifestStaticFilesStorage'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True


STATIC_URL = os.environ.get('STATIC_URL', '/static/')

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_FRAME_DENY = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True



# REDIS
# inherit from base








# EMAILS
if 'EMAIL_HOST_USER' in os.environ and 'EMAIL_HOST_PASSWORD' in os.environ:
    EMAIL_SUBJECT_PREFIX = '[VIS]'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_SSL = True
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_PORT = 465
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


EXPORT_RECIPIENTS = os.environ.get('EXPORT_RECIPIENTS', '').split(',')

CACHE_CONTROL_MAX_AGE = 60*60

#STILL TO DO #review2017
#exists in heroku but not in prod0
#set(['LOGGING ', 'S3_BUCKET_NAME ', 'CACHES ', 'DJ_DATABASE_URL ', 'STATICFILES_STORAGE ', 'S3_SECRET_ACCESS_KEY_ID ', 'DATABASES ', 'INSTALLED_APPS ', 'S3_ACCESS_KEY_ID ', 'redis_url '])
#exists in heroku and not inherited by base and doesnt exist in prod
#set(['LOGGING ', 'S3_SECRET_ACCESS_KEY_ID ', 'STATICFILES_STORAGE ', 'S3_ACCESS_KEY_ID ', 'S3_BUCKET_NAME '])
# The S3/STATICFILES stuff probably not needed because it's for assets. So maybe just LOGGING is needed.


