"""
Django settings for vis project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url

# PATH vars
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
sys.path.insert(0, os.path.join(PROJECT_DIR, 'vis/apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dn@b!u!a^)g&61d^ec2!+fi$9g@%7^kh*@b$vby2^l+ra_ut0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'djangosecure',

    'markdown_deux',
    'pipeline',
    'wagtailextra',

    'taggit',
    'modelcluster',
    'compressor',
    'django.contrib.staticfiles',
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailimages',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailembeds',
    'wagtail.wagtailusers',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.wagtailsitemaps',

    'zendesk',

    'info',
    'core',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
    'core.middleware.MaxAgeMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'vis/templates'),
)

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

ROOT_URLCONF = 'vis.urls'

WSGI_APPLICATION = 'vis.wsgi.application'


from django.conf import global_settings

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                'core.context_processors.globals',
            ],
            # 'context_processors': global_settings.TEMPLATE['OPTIONS']['context_processors'] + (
            #     'django.core.context_processors.request',
            #     'core.context_processors.globals',
            # )
        },
    },
]

# TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
#     'django.core.context_processors.request',
#     'core.context_processors.globals',
# )


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vis',
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('POSTGRES_HOST', ''),
        'PORT': os.environ.get('POSTGRES_PORT', ''),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CACHE_CONTROL_MAX_AGE = 0

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

PIPELINE_COMPILERS = ()
PIPELINE_ENABLED = True

MARKDOWN_PROTECT_PREVIEW = True

# Heroku
DJ_DATABASE_URL = os.environ.get('DATABASE_URL')
if DJ_DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DJ_DATABASE_URL)
    }

    PIPELINE_COMPILERS = ()
    PIPELINE_ENABLED = True

    DEBUG = True

    TEMPLATE_DEBUG = DEBUG

PIPELINE_YUGLIFY_BINARY = os.path.join(PROJECT_DIR, 'node_modules/.bin/yuglify')

WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False
LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'
WAGTAIL_SITE_NAME = 'VIS'

BING_API_TOKEN = os.environ.get('BING_API_TOKEN', '')

ZENDESK_API_USERNAME = os.environ.get('ZENDESK_API_USERNAME', '')
ZENDESK_API_TOKEN = os.environ.get('ZENDESK_API_TOKEN', '')
ZENDESK_REQUESTER_ID = os.environ.get('ZENDESK_REQUESTER_ID', '')
ZENDESK_GROUP_ID = os.environ.get('ZENDESK_GROUP_ID', '24622458') # Defaults to 'VIS' group
ZENDESK_CUSTOM_FIELD_URL_ID = os.environ.get('ZENDESK_CUSTOM_FIELD_URL_ID', '')
ZENDESK_CUSTOM_FIELD_USERAGENT_ID = os.environ.get('ZENDESK_CUSTOM_FIELD_USERAGENT_ID', '')
ZENDESK_CUSTOM_FIELD_SERVICE_ID = os.environ.get('ZENDESK_CUSTOM_FIELD_SERVICE_ID', '')
ZENDESK_API_ENDPOINT = os.environ.get('ZENDESK_API_ENDPOINT', 'https://ministryofjustice.zendesk.com/api/v2/')


S3_ACCESS_KEY_ID = os.environ.get('S3_ACCESS_KEY_ID')
S3_SECRET_ACCESS_KEY_ID = os.environ.get('S3_SECRET_ACCESS_KEY_ID')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

# URL2PNG

URL2PNG_API_KEY = os.environ.get('URL2PNG_API_KEY', '')
URL2PNG_SECRET_KEY = os.environ.get('URL2PNG_SECRET_KEY', '')


# EXPORT

DEFAULT_FROM_EMAIL = 'noreply@digital.justice.gov.uk'

EXPORT_ZIP_NAME = 'vis-export'
EXPORT_EMAIL_SUBJECT = 'VIS - Export'
EXPORT_EMAIL_BODY = 'Find attached the VIS website.'
EXPORT_RECIPIENTS = []

GA_ID = os.environ.get('GA_ID', '')

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


try:
    from .local import *
except ImportError:
    pass
