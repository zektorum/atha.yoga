import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "")

DEBUG = bool(int(os.environ.get("DEBUG", "0")))

ALLOWED_HOSTS = ["*"]
SITE_URL = os.environ.get("SITE_URL")
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "django_extensions",
    "core",
    "lessons",
    "django_elasticsearch_dsl",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_CLASSES": [
        "core.custom_middleware.CustomAnonRateThrottle",
        "core.custom_middleware.CustomUserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "100/min", "user": "100/min"},
    "DEFAULT_THROTTLE_DENIED_DURATION": "600",
    "EXCEPTION_HANDLER": "core.app.utils.exceptions.custom_exception_handler",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ATHA Yoga API",
    "DESCRIPTION": "Atha yoga",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", ""),
        "USER": os.environ.get("POSTGRES_USER", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", ""),
        "PORT": os.environ.get("POSTGRES_PORT", ""),
    }
}
AUTH_USER_MODEL = "core.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "UTC"
USE_I18N = True
USE_T10N = True
USE_TZ = True

STATIC_URL = os.path.join(BASE_DIR, "static/")
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_PER_PAGE = 15

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": f"{os.environ.get('ELASTIC_LOGIN')}:{os.environ.get('ELASTIC_PASSWORD')}@"
        f"{os.environ.get('ELASTIC_HOST')}:{os.environ.get('ELASTIC_PORT')}"
    },
}

TERMINAL_KEY = os.getenv("TERMINAL_KEY")
TERMINAL_PASSWORD = os.getenv("TERMINAL_PASSWORD")

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "simple": {
            "format": "Time: {asctime} \n Module: {module} \n Line: {lineno} \n Message: {message} \n",
            "style": "{",
        },
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "console": {
            "formatter": "verbose",
            "class": "logging.StreamHandler",
        },
        "app_log": {
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "core/logs/app_log.log"),
            "formatter": "simple",
            "level": "DEBUG",
        },
        "daily_file": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "core/logs/daily_log.log"),
            "when": "D",
            "interval": 1,
            "backupCount": 10,
            "formatter": "simple",
        },
    },
    "loggers": {
        "app_log": {"handlers": ["app_log"], "propagate": False, "level": "DEBUG"},
        "daily_log": {"handlers": ["daily_file"], "propagate": False, "level": "ERROR"},
        "django": {
            "handlers": ["console"],
            "propagate": True,
            "level": "INFO",
        },
        "": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
