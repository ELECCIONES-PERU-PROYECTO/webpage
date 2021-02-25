import os

import environ
from django.contrib.messages import constants as messages
from django.utils.translation import ugettext_lazy as _

# ------------------------ CONFIGURACIÓN PERSONALIZADA ------------------------
# Configuración de directorios y entorno --------------------------------------
# Directorio raíz del proyecto
project = environ.Path(__file__) - 2

# Directorios de aplicaciones
apps = os.listdir(project("elecciones_peru"))
apps = [project.path("elecciones_peru", x) for x in apps]
apps = [x for x in apps if os.path.isdir(x())]
apps = [x for x in apps if "__" not in x()]

# Directorio de elementos públicos
public = project.path("public")

if not os.path.exists(public()):
    os.makedirs(public())

# Directorio de elementos privados
private = project.path("private")

if not os.path.exists(private()):
    os.makedirs(private())

# Directorio de plantillas
templates = project.path("templates")

if not os.path.exists(templates()):
    os.makedirs(templates())

# Configuracion de entorno (Lectura de archivo .env)
environment_file = project(".env")
environment = environ.Env()

if os.path.exists(environment_file) and os.path.isfile(environment_file):
    environment.read_env(environment_file)


# -------------------------- CONFIGURACIÓN DE DJANGO --------------------------
# Debugging -------------------------------------------------------------------
DEBUG = environment.bool("DEBUG", default=True)
DEBUG_TOOLBAR = environment.bool("DEBUG_TOOLBAR", default=True)
DEBUG_TEMPLATES = environment.bool("DEBUG_TEMPLATES", default=True)

# Estructura de Directorios ---------------------------------------------------
# Directorio base del proyecto
BASE_DIR = project()

# Directorio en donde colectar archivos subidos por usuarios
MEDIA_ROOT = public("media")

# Directorio en donde colectar archivos estáticos
STATIC_ROOT = public("static")

STATICFILES_DIRS = [x("static") for x in apps if os.path.isdir(x("static"))]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Aministradores y Managers ---------------------------------------------------
MANAGERS = ADMINS = (("SoftButterfly SysAdmin", "sysadmin@softbutterfly.io"),)

# Hosts -----------------------------------------------------------------------
ALLOWED_HOSTS = environment.list(
    "ALLOWED_HOSTS", cast=lambda x: x.split(":"), default=[["*"]]
)[0]

# Seguridad -------------------------------------------------------------------
# Llave secreta para la firma de cookies
SECRET_KEY = environment.str("SECRET_KEY", default="%Up#r*%#CR#T*k#i")

# Diversos heades para enviar de vuelta en los 'responses'
# Hay que verificar su utilidad y que tan efectivo es delegar
# esto a nginx
SECURE_BROWSER_XSS_FILTER = environment.bool("SECURE_BROWSER_XSS_FILTER", default=False)

SECURE_SSL_REDIRECT = environment.bool("SECURE_SSL_REDIRECT", default=False)

SECURE_CONTENT_TYPE_NOSNIFF = environment.bool(
    "SECURE_CONTENT_TYPE_NOSNIFF", default=False
)

SECURE_FRAME_DENY = environment.bool("SECURE_FRAME_DENY", default=False)

SECURE_HSTS_INCLUDE_SUBDOMAINS = environment.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False
)

SESSION_COOKIE_HTTPONLY = environment.bool("SESSION_COOKIE_HTTPONLY", default=False)

SESSION_COOKIE_SECURE = environment.bool("SESSION_COOKIE_SECURE", default=False)

# Seguridad CSRF
CSRF_COOKIE_SECURE = environment.bool("CSRF_COOKIE_SECURE", default=True)

CSRF_COOKIE_HTTPONLY = environment.bool("CSRF_COOKIE_HTTPONLY", default=True)

CSRF_COOKIE_DOMAIN = environment.str("CSRF_COOKIE_DOMAIN", default=None)

CSRF_TRUSTED_ORIGINS = environment.list(
    "CSRF_TRUSTED_ORIGINS", cast=lambda x: x.split(":"), default=[["*"]]
)[0]

# Registro de aplicaciones de aplicaciones ------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Covid Registry
    "elecciones_peru.elecciones",
  
    
]

if DEBUG:
    INSTALLED_APPS += [
        "django_extensions",
    ]

# Registro de Middlewares -----------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Configuración de Plantillas -------------------------------------------------
CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.template.context_processors.request",
]

LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

if not DEBUG:
    LOADERS = [("django.template.loaders.cached.Loader", LOADERS)]

TEMPLATE_DIRS = [x("templates") for x in apps if os.path.isdir(x("templates"))]

TEMPLATE_DIRS += [templates()]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": environment.list(
            "TEMPLATES_DIRS", cast=lambda x: x.split(":"), default=[TEMPLATE_DIRS],
        )[0],
        "OPTIONS": {
            "context_processors": CONTEXT_PROCESSORS,
            "loaders": LOADERS,
            "debug": DEBUG_TEMPLATES,
        },
    },
]

# WSGI ------------------------------------------------------------------------
WSGI_APPLICATION = "elecciones_peru.wsgi.application"

# ASGI ------------------------------------------------------------------------
# ASGI_APPLICATION = "covid_registry.routing.application"

# Configuración de URL --------------------------------------------------------
INTERNAL_IPS = environment.list(
    "INTERNAL_IPS", cast=lambda x: x.split(":"), default=[["*"]]
)[0]

ROOT_URLCONF = "elecciones_peru.urls"

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Configuración de base de caché ----------------------------------------------
if not DEBUG:
    CACHE_URL_LOCMEM = "locmemcache://temporal"
    CACHE_DEFAULT = environment.cache_url(var="CACHE_URL", default=CACHE_URL_LOCMEM)

    CACHES = {
        "default": CACHE_DEFAULT,
    }


# Configuración de base de datos ----------------------------------------------
DATABASE_URL_SQLITE = "sqlite:///" + project("db.sqlite3")
DATABASE_DEFAULT = environment.db_url("DATABASE_URL", default=DATABASE_URL_SQLITE)

DATABASES = {
    "default": DATABASE_DEFAULT,
}

# Configuración de Sessiones --------------------------------------------------
SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# Autenticación ---------------------------------------------------------------
# AUTH_USER_MODEL = "accounts.User"

# Autenticación ---------------------------------------------------------------
PASSWORD_VALIDATORS = [
    "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    "django.contrib.auth.password_validation.MinimumLengthValidator",
    "django.contrib.auth.password_validation.CommonPasswordValidator",
    "django.contrib.auth.password_validation.NumericPasswordValidator",
]

AUTH_PASSWORD_VALIDATORS = [{"NAME": x} for x in PASSWORD_VALIDATORS]

LOGIN_REDIRECT_URL = "dashboard:home"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
)

# Internacionalización y localización -----------------------------------------
LANGUAGE_COOKIE_NAME = environment.str("LANGUAGE_COOKIE_NAME", default="local_laguage")

LANGUAGE_CODE = "es-pe"

LANGUAGES = [
    ("en", _("English")),
    ("es", _("Spanish")),
]

TIME_ZONE = environment.str("TIME_ZONE", default="America/Lima")
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ---------------------- CONFIGURACIÓN PARA APLICACIONES ----------------------
# django.contrib.sites (django) ------------------------------------------------
SITE_ID = 1

# django.contrib.auth (django) -------------------------------------------------
PASSWORD_RESET_TIMEOUT_DAYS = 1

# django.contrib.messages ------------------------------------------------------
MESSAGE_TAGS = {
    messages.ERROR: _("alert"),
}

# django-debug-toolbar --------------------------------------------------------
if DEBUG_TOOLBAR:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware",] + MIDDLEWARE

    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.versions.VersionsPanel",
        "debug_toolbar.panels.timer.TimerPanel",
        "debug_toolbar.panels.settings.SettingsPanel",
        "debug_toolbar.panels.headers.HeadersPanel",
        "debug_toolbar.panels.request.RequestPanel",
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.templates.TemplatesPanel",
        "debug_toolbar.panels.staticfiles.StaticFilesPanel",
        "debug_toolbar.panels.cache.CachePanel",
        "debug_toolbar.panels.signals.SignalsPanel",
        "debug_toolbar.panels.logging.LoggingPanel",
        "debug_toolbar.panels.redirects.RedirectsPanel",
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ]

    def show_toolbar(request):  # pylint: disable=unused-argument
        return True

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": show_toolbar,
        "RENDER_PANELS": True,
        "INTERNAL_IPS": INTERNAL_IPS,
        "RESULTS_CACHE_SIZE": 3,
        "SHOW_COLLAPSED": True,
        "SQL_WARNING_THRESHOLD": 100,
        "JQUERY_URL": "/static/admin/js/vendor/jquery/jquery.js",
    }

# django-storages -------------------------------------------------------------
""" USE_AWS_STORAGE = environment.bool("USE_AWS_STORAGE", False)

AWS_ACCESS_KEY_ID = environment.str("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = environment.str("AWS_SECRET_ACCESS_KEY", "")

AWS_STORAGE_BUCKET_NAME = environment.str("AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_REGION_NAME = environment.str("AWS_S3_REGION_NAME", "")
AWS_LOCATION = environment.str("AWS_LOCATION", "")
AWS_MEDIA_LOCATION = environment.str("AWS_MEDIA_LOCATION", AWS_LOCATION + "/media")
AWS_STATIC_LOCATION = environment.str("AWS_STATIC_LOCATION", AWS_LOCATION + "/static")

AWS_S3_USE_SSL = environment.bool("AWS_S3_USE_SSL", True)
AWS_DEFAULT_ACL = environment.bool("AWS_DEFAULT_ACL", None)
AWS_QUERYSTRING_AUTH = environment.bool("AWS_QUERYSTRING_AUTH", False)
AWS_S3_FILE_OVERWRITE = environment.bool("AWS_S3_FILE_OVERWRITE", True)

AWS_S3_CUSTOM_DOMAIN = environment.str("AWS_S3_CUSTOM_DOMAIN", "")

if USE_AWS_STORAGE:
    STATICFILES_STORAGE = "covid_registry.core.storage.S3StaticStorage"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"

    DEFAULT_FILE_STORAGE = "covid_registry.core.storage.S3MediaStorage"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/"
 """