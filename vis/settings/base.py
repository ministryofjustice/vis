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
PROJECT_DIR = os.path.join(BASE_DIR, '../')
sys.path.insert(0, os.path.join(PROJECT_DIR, 'vis/apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dn@b!u!a^)g&61d^ec2!+fi$9g@%7^kh*@b$vby2^l+ra_ut0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'markdown_deux',
    'pipeline',

    'taggit',
    'modelcluster',
    'compressor',
    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailembeds',
    'wagtail.wagtailusers',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.wagtailsitemaps',

    'info',
    'core',
    'pages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
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
    os.path.join(BASE_DIR, 'assets-src/vendor'),
    os.path.join(PROJECT_DIR, 'vis/assets'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


ROOT_URLCONF = 'vis.urls'

WSGI_APPLICATION = 'vis.wsgi.application'


from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)


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

STATIC_URL = '/static/'

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


ADDRESSFINDER_API_HOST = os.environ.get('ADDRESSFINDER_API_HOST',
    'http://127.0.0.1:8003')
ADDRESSFINDER_API_TOKEN = os.environ.get('ADDRESSFINDER_API_TOKEN', '')


try:
    from .local import *
except ImportError:
    pass
