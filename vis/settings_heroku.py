from .settings import *
import dj_database_url

DJ_DATABASE_URL = os.environ.get('DATABASE_URL')
if DJ_DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DJ_DATABASE_URL)
    }

PIPELINE_COMPILERS = ()
PIPELINE_ENABLED = TRUE

DEBUG = True

TEMPLATE_DEBUG = DEBUG

STATICFILES_DIRS += (
    os.path.join(PROJECT_DIR, 'static'),
)
