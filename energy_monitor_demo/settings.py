"""
Django settings for Happearth app project.

"""

import os

__author__ = "Daniel Fernando Santos Bustos"
__license__ = "GPL V3"
__version__ = "1.0"
__email__ = "dfsantosbu@unal.edu.co"
__status__ = "Production"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

with open (BASE_DIR+"/"+"bq-secret-key.mqp") as f:
    SECRET_KEY = f.read().strip()

ASGI_APPLICATION = "energy_monitor_demo.routing.application"

DEBUG = False

ALLOWED_HOSTS = ["0.0.0.0", "localhost", ".happearth.site"]

COMPRESS_OFFLINE = True

INSTALLED_APPS = [
    'channels',
    #'compressor', #More efficient
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_honeypot',
    'monitor.apps.MonitorConfig',
    'accounts.apps.AccountsConfig',
    'house.apps.HouseConfig', 
    #'django-alexa'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'energy_monitor_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'monitor.context_processor.global_monitor',
            ],
        },
    },
]

WSGI_APPLICATION = 'energy_monitor_demo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGIN_REDIRECT_URL = 'monitor:home'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './bq-user-creds.json'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rcodigame@gmail.com'
EMAIL_HOST_PASSWORD = (os.environ.get("EMAIL_HOST_PASSWORD") or "").replace("\\", "")
EMAIL_PORT = 587
FIXTURE_DIRS = (
   'accounts/fixtures/',
)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
if not DEBUG:
  SECURE_HSTS_SECONDS = True
  SECURE_HSTS_INCLUDE_SUBDOMAINS = True
  SECURE_CONTENT_TYPE_NOSNIFF = True
  SECURE_BROWSER_XSS_FILTER = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  X_FRAME_OPTIONS = "DENY"
  SECURE_HSTS_PRELOAD = True
""" Configs for ALEXA-DJANGO
ALEXA_APP_ID_DEFAULT= os.environ.get("ALEXA_APP_ID_DEFAULT")
ALEXA_APP_ID_OTHER=os.environ.get("ALEXA_APP_ID_OTHER")
ALEXA_REQUEST_VERIFICATON=bool( os.environ.get("ALEXA_REQUEST_VERIFICATION") or False )
"""
