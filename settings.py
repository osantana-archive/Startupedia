#!/usr/bin/env python
# -*- encoding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-
#

# Utility
# =======
import os
ROOTDIR = os.path.dirname(os.path.realpath(__file__))


# Administration
# ==============
ADMINS = (
    ('Osvaldo Santana Neto', 'osantana@triveos.com'),
)

MANAGERS = ADMINS


# Databases
# =========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(ROOTDIR, 'startupedia.db'),
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# E-Mail
# ======
DEFAULT_FROM_EMAIL = "website@startupedia.org"
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER="website@startupedia.org"
EMAIL_HOST_PASSWORD="[secret-password]"
EMAIL_USE_TLS=True

# Internationalization
# ====================
USE_I18N = True
USE_L10N = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    ('en-us', u'English'),
    ('pt-br', u'Português (Brasil)'),
)


# Paths & URLs
# ============
ROOT_URLCONF = 'startupedia.urls'
SSL_ENABLED=True


# Static Media
# ============
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOTDIR, "media")
ADMIN_MEDIA_PREFIX = '/media-admin/'


# Miscelaneous
# ============
SITE_ID = 1
SECRET_KEY = 'c5lt9)e=xyz+in7np(hnc#*i+vviio)lcu!3^t_y6k+zwz#%b_'


# Security
# ========


# Templates
# =========
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_DIRS = [
    os.path.join(ROOTDIR, "templates"),
]


# Middleware Classes
# ==================
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# Applications
# ============
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'main',
]


# Development Settings
# ====================

import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"

if DEBUG:
    import debug_toolbar
    MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    TEMPLATE_DIRS.append(os.path.join(os.path.dirname(debug_toolbar.__file__), 'templates'))
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'HIDE_DJANGO_SQL': False,
        'TAG': 'div',
    }
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    INSTALLED_APPS.append("django_nose")

