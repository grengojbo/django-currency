# -*- mode: python; coding: utf-8; -*- 
# Django settings for django_test project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import os, os.path, sys
import logging

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, '../../apps'))
#sys.path.insert(0, os.path.join(PROJECT_ROOT, './'))

DJANGO_PROJECT = 'currency'
DJANGO_SETTINGS_MODULE = 'settings'

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_SQL = True # Show debug information about sql queries at the bottom of page
ORM_DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'currency_test.db')



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
gettext_noop = lambda s:s

LANGUAGE_CODE = 'ru-ru'
LANGUAGES = (
   ('en', gettext_noop('English')),
   ('ru', gettext_noop('Russian')),
)
#LANGUAGES_BIDI = ('he', 'ar', 'fa')
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
I18N_URLS = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g_a5r^%-u00w6o4@1+=!+mu=l24%_yy2kcrvi#!cm4n*b&s11*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    #"django.contrib.csrf.middleware.CsrfMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    #"djanjinja.middleware.RequestContextMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.auth',
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    #"sugar.context_processors.admin_media_prefix",
    #"sugar.context_processors.settings_vars",
    )

TEMPLATE_DIRS = (
    #os.path.realpath(os.path.join(PROJECT_PATH, '../contrib/grappelli/templates/')),
    os.path.join(PROJECT_ROOT, "templates"),
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.admindocs',
    #'django.contrib.comments',
    'django.contrib.sessions',
    'django_extensions',
    'devserver',
    'keyedcache',
    'livesettings',
    'l10n',
    'south',
    'currency',
    'currency_test',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    #'devserver.modules.profile.MemoryUseModule',
    #'devserver.modules.cache.CacheSummaryModule',
)
CACHE_BACKEND = "locmem:///"
CACHE_TIMEOUT = 60*5
CACHE_PREFIX = "S"

#Configure logging
LOGFILE = "currency.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

fileLog = logging.FileHandler(os.path.join(PROJECT_ROOT, LOGFILE), 'w')
fileLog.setLevel(logging.DEBUG)
# add the handler to the root logger
logging.info("Currency start")
