"""
Django settings for elecciones_peru project.
Generated by 'django-admin startproject' using Django 3.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from django.core.management.utils import get_random_secret_key
from decouple import config
import dj_database_url
import mimetypes
import os
import sys


# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

mimetypes.add_type("text/css", ".css", True)

# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG", "False") == "True"
DEBUG = True

#ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1, localhost, elegimos.pe, nex.ieh.mybluehost.me, *").split(",")

ALLOWED_HOSTS = ["*"]
BASE_DIR = Path(__file__).resolve().parent.parent

# CSRF_COOKIE_SECURE = True

# SESSION_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True

# Investigar
# SECURE_HSTS_SECONDS = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'elecciones',
    'import_export'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'elecciones_peru.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'elecciones_peru.wsgi.application'
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
   'default' : {
       'ENGINE' : 'django.db.backends.postgresql',
       'NAME' : 'proyecto_elecciones',
       'USER' : 'postgres',
       'PASSWORD' : '1234567',
       'HOST' : 'localhost',
       'PORT' : 5432,
   }
}



#DATABASES = {
#   'default' : {
#       'ENGINE' : 'django.db.backends.postgresql',
#       'NAME' : 'elecciones_peru',
#       'USER' : 'postgres',
#       'PASSWORD' : 'pvta',
#       'HOST' : 'localhost',
#       'PORT' : 5432,
#   }
#}


# DATABASES = {
#    'default': dj_database_url.config(
#        default=config('DATABASE_URL')
#    )
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
