#!/usr/bin/env python 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import logging

from django.contrib import messages

import janeway.core.plugin_installed_apps as plugin_installed_apps

#TODO: use djangorc here
ROOTDIR = os.environ.get('ROOTDIR', '/home/www/ahnjournal-devel')
BASE_DIR = os.path.join(ROOTDIR, 'src/janeway')
PROJECT_DIR = os.path.dirname(BASE_DIR)

JOURNAL_CODE = 'ahnjournal'
ENABLE_PRESS_MIDDLEWARE = False

sys.path.append(os.path.join(BASE_DIR, "plugins"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# You should change this key before you go live!
SECRET_KEY = 'uxprsdslddk^gzd-r=_2zzaqq23yolxn)$k6tsd8_cepl^s^tms2w1qrv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
COMMAND = sys.argv[1:]
IN_TEST_RUNNER = COMMAND[:1] == ['test']
ALLOWED_HOSTS = ['*']

ENABLE_TEXTURE = True

FILE_UPLOAD_PERMISSIONS = 0o644

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Installed Apps
    'cms',
    'core',
    'copyediting',
    'cron',
    'events',
    'identifiers',
    'journal',
    'metrics',
    'comms',
    'preprint',
    'press',
    'production',
    'proofing',
    'review',
    'reports',
    'security',
    'submission',
    'transform',
    'utils',
    #'install',
    'workflow',
    #'webinar',
    #'demo',

    # 3rd Party
    'django_summernote',
    'markdown_deux',
    'hvad',
    'raven.contrib.django.raven_compat',
    'bootstrap4',
    'rest_framework',
    'foundationform',
    'materialize',
    #'snowpenguin.django.recaptcha2',
    'simplemathcaptcha',
    'towel',
    #'notifications',

    # Forms
    'django.forms',

    # newsletter
    #'newsletter'
]

INSTALLED_APPS += plugin_installed_apps.load_plugin_apps(BASE_DIR)
INSTALLED_APPS += plugin_installed_apps.load_homepage_element_apps(BASE_DIR)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'janeway.core.middleware.TimezoneMiddleware',
    'janeway.core.middleware.SiteSettingsMiddleware',
    'janeway.utils.template_override_middleware.ThemeEngineMiddleware',
    #'janeway.core.middleware.MaintenanceModeMiddleware',
    'janeway.cron.middleware.CronMiddleware',
    'janeway.core.middleware.CounterCookieMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'janeway.core.middleware.PressMiddleware',
    'janeway.core.middleware.GlobalRequestMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'janeway.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ([
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'common'),
            os.path.join(BASE_DIR, 'templates', 'admin'),
        ]
            + plugin_installed_apps.load_plugin_templates(BASE_DIR)
            + plugin_installed_apps.load_homepage_element_templates(BASE_DIR)
        ),
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'janeway.core.context_processors.journal',
                'janeway.core.context_processors.journal_settings',
                'janeway.core.context_processors.press',
                'janeway.core.context_processors.active',
                'janeway.core.context_processors.navigation',
                'janeway.core.context_processors.date',
                'janeway.core.context_processors.version',
                'django_settings_export.settings_export',
                'django.template.context_processors.i18n'
            ],
            'loaders': [
                'janeway.utils.template_override_middleware.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'builtins': [
                'janeway.core.templatetags.fqdn',
            ]
        },
    },
]

#TEMPLATE_CONTEXT_PROCESSORS = TEMPLATES[0]['OPTIONS']['context_processors']
#FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

SETTINGS_EXPORT = [
    'ORCID_API_URL',
    'ORCID_TOKEN_URL',
    'ORCID_CLIENT_SECRET',
    'ORCID_CLIENT_ID',
    'ORCID_URL',
#    'ENABLE_ENHANCED_MAILGUN_FEATURES',
    'ENABLE_ORCID',
    'DEBUG',
    'LANGUAGE_CODE',
]

WSGI_APPLICATION = 'janeway.core.wsgi.application'
DEFAULT_HOST = 'https://open-neurosecurity.org/'  # This is the default redirect if no other sites are found.

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# We recommend mysql but Django supports PGSQL and SQLite amongst others
if os.environ.get("DB_VENDOR") == "postgres":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ["DB_NAME"],
            'USER': os.environ["DB_USER"],
            'PASSWORD': os.environ["DB_PASSWORD"],
            'HOST': os.environ["DB_HOST"],
            'PORT': os.environ["DB_PORT"],
        }
    }
elif os.environ.get("DB_VENDOR") in {"mysql", "mariadb"}:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ["DB_NAME"],
            'USER': os.environ["DB_USER"],
            'PASSWORD': os.environ["DB_PASSWORD"],
            'HOST': os.environ["DB_HOST"],
            'PORT': os.environ["DB_PORT"],
            'OPTIONS': {
                'init_command': 'SET default_storage_engine=INNODB; '
                'ALTER DATABASE {0} CHARACTER SET utf8mb4 COLLATE '
                'utf8mb4_general_ci'.format(os.environ["DB_NAME"]),
                'charset': 'utf8mb4',
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/var/db/janeway.sqlite3',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'core', 'locales')
] + plugin_installed_apps.load_plugin_locales(BASE_DIR)

def ugettext(s):
    return s

LANGUAGES = (
    ('en', ugettext('English')),
    ('fr', ugettext('French')),
    ('de', ugettext('German')),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://open-neurosecurity.org/media/'

USE_I18N = False
USE_L10N = False
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')
STATICFILES_DIRS = [
    # The /src/static/ folder is used by Janeway and should not be removed.
    os.path.join(BASE_DIR, 'static'),
    ]
STATIC_URL = 'https://open-neurosecurity.org/static/'

if ENABLE_TEXTURE:
    STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'texture'))

SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': False,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False, 

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Set text direction : 'left to right' is default.
    'direction': 'ltr',

    # Change editor size
    'width': '100%',
    'height': '480',

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,
    'attachment_filesize_limit': 2056 * 2056,
}

# 1.9 appears confused about where null and blank are required for many to
# many fields, so we're hiding these warning from the console
SILENCED_SYSTEM_CHECKS = (
    'fields.W340',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'DEBUG' if DEBUG else 'INFO',
        'handlers': ['console', 'log_file'],
    },
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s '
            'P:%(process)d T:%(thread)d %(message)s',
        },
        'coloured': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(levelname)s %(asctime)s %(module)s '
            'P:%(process)d T:%(thread)d %(message)s',
            'log_colors' : {
                'DEBUG':    'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red',
            }
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'coloured',
            'stream': 'ext://sys.stdout',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*50,  # 50 MB
            'backupCount': 1,
            'filename': '/var/log/janeway.log',
            'formatter': 'default'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console', 'log_file'],
            'propagate': False,
        },
    },
}

class SuppressDeprecated(logging.Filter):
    def filter(self, record):
        WARNINGS_TO_SUPPRESS = [
            'RemovedInDjango110Warning',
        ]
        # Return false to suppress message.
        return not any(
            [warn in record.getMessage() for warn in WARNINGS_TO_SUPPRESS]
        )


MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

LOGIN_REDIRECT_URL = '/ahnjournal/user/profile/'
LOGIN_URL = '/ahnjournal/login/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DUMMY_EMAIL_DOMAIN = "@example.com"

# Settings for use with Mailgun
#MAILGUN_ACCESS_KEY = ''
#MAILGUN_SERVER_NAME = ''
#MAILGUN_REQUIRE_TLS = False
#ENABLE_ENHANCED_MAILGUN_FEATURES = False  # Enables email tracking

DATE_FORMT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i"
AUTH_USER_MODEL = 'core.Account'

PLUGIN_HOOKS = {}
NOTIFY_FUNCS = []
#JANEWAY_CRONJOBS = []

ENABLE_ORCID = True
ORCID_API_URL = 'http://pub.orcid.org/v1.2_rc7/'
ORCID_URL = 'https://orcid.org/oauth/authorize'
ORCID_TOKEN_URL = 'https://pub.orcid.org/oauth/token'
ORCID_CLIENT_SECRET = '4198cf6d-cc09-4757-8fa4-186a720b5f51'
ORCID_CLIENT_ID = 'APP-5IWTN5G13WHTGGBM'

SESSION_COOKIE_NAME = 'JANEWAYSESSID'
SESSION_SAVE_EVERY_REQUEST = True

#S3_ACCESS_KEY = ''
#S3_SECRET_KEY = ''
#S3_BUCKET_NAME = ''
#END_POINT = 'eu-west-2'  # eg. eu-west-1
#S3_HOST = 's3.eu-west-2.amazonaws.com'  # eg. s3.eu-west-1.amazonaws.com
#BACKUP_TYPE = 'directory'  # s3 or directory
#BACKUP_DIR = '/path/to/backup/dir/'
#BACKUP_EMAIL = False  # If set to True, will send an email each time backup is run

URL_CONFIG = 'path'  # XXX path or domain

# Captcha
# You can get reCaptcha keys for your domain here: https://developers.google.com/recaptcha/intro
# You can set either to use Google's reCaptcha or a basic math field with no external requirements

CAPTCHA_TYPE = 'simple_math'  # should be either 'simple_math' or 'recaptcha' to enable captcha fields otherwise disabled
#RECAPTCHA_PRIVATE_KEY = '' # Public and private keys are required when using recaptcha
#RECAPTCHA_PUBLIC_KEY = ''

#BOOTSTRAP4 = {
#    'required_css_class': 'required',
#}

SUMMERNOTE_THEME = 'bs4'

#Deprecated settings
#SILENT_IMPORT_CACHE = True
#WORKFLOW_PLUGINS = {}
#SILENT_IMPORT_CACHE = True
# Default timeout for outgoing HTTP connections
#HTTP_TIMEOUT_SECONDS = 0
# New XML galleys will be associated with this stylesheet by default when they
# are first uploaded
#DEFAULT_XSL_FILE_LABEL = 'Janeway default (1.3.8)'

# Twitter API settings imported from mainapp.config.global_settings.py
TWITTER_API_KEY = 'KMJIFslk9yP1Nj8N29PUj3Mz6' # CLIENT_ID
TWITTER_API_SECRET_KEY = '0yTzEGMU6wKNkkU0xwiSlXu4suJ1Wh6S5RqYnwoNPFb64uWU7b'

