import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# ------------------------------------------------------------------------------
# Project Basic Configuration
# ------------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# Step 1: Loading base .env file (for ENV_TYPE)
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Step 2: Getting environment type
ENV_TYPE = os.getenv("ENV_TYPE", "stagging").lower()

# Step 3: Loading respective credentials
SECRETS_FILE_MAP = {
    "stagging": ".env.stagging.secrets",
    "production": ".env.production.secrets"
}

secret_file = SECRETS_FILE_MAP.get(ENV_TYPE)
if secret_file:
    load_dotenv(dotenv_path=BASE_DIR / secret_file, override=True)
else:
    raise Exception(f"Unknown ENV_TYPE: {ENV_TYPE}")

DEBUG = os.getenv('DEBUG', default=True)
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY not set in environment variables")


# ------------------------------------------------------------------------------
# Allowed Hosts & CORS
# ------------------------------------------------------------------------------


ALLOWED_HOSTS = []


# ------------------------------------------------------------------------------
# Installed Apps
# ------------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'rest_framework'
]

# ------------------------------------------------------------------------------
# Middleware
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ------------------------------------------------------------------------------
# URL & WSGI
# ------------------------------------------------------------------------------


ROOT_URLCONF = 'storeapi.urls'
WSGI_APPLICATION = 'storeapi.wsgi.application'

# ------------------------------------------------------------------------------
# Templates
# ------------------------------------------------------------------------------


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ------------------------------------------------------------------------------
# Database Settings
# ------------------------------------------------------------------------------

DATABASE_ENV_TYPE = os.getenv("DATABASE_ENV_TYPE", "stagging").lower()
if DATABASE_ENV_TYPE == "stagging":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv("DB_NAME", default=""),
            'USER': os.getenv("DB_USER", default=""),
            'PASSWORD': os.getenv("DB_PASSWORD", default=""),
            'HOST': os.getenv("DB_HOST", default="localhost"),
            'PORT': os.getenv("DB_PORT", default=3306),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        },
        'replica': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv("REPLICA_DB_NAME", os.getenv("DB_NAME")),  # fallback to master
            'USER': os.getenv("REPLICA_USER", os.getenv("DB_USER")),
            'PASSWORD': os.getenv("REPLICA_PASSWORD", os.getenv("DB_PASSWORD")),
            'HOST': os.getenv("REPLICA_HOST", os.getenv("DB_HOST")),
            'PORT': os.getenv("REPLICA_PORT", 3306),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv("DB_NAME", default=""),
            'USER': os.getenv("DB_USER", default=""),
            'PASSWORD': os.getenv("DB_PASSWORD", default=""),
            'HOST': os.getenv("DB_HOST", default="localhost"),
            'PORT': os.getenv("DB_PORT", default=3306),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        },
        'replica': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv("REPLICA_DB_NAME", os.getenv("DB_NAME")),  # fallback to master
            'USER': os.getenv("REPLICA_USER", os.getenv("DB_USER")),
            'PASSWORD': os.getenv("REPLICA_PASSWORD", os.getenv("DB_PASSWORD")),
            'HOST': os.getenv("REPLICA_HOST", os.getenv("DB_HOST")),
            'PORT': os.getenv("REPLICA_PORT", 3306),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
        }
    }

DATABASE_ROUTERS = ['storeapi.db_router.MasterSlaveRouter']


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# ------------------------------------------------------------------------------
# Localization
# ------------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = False


# ------------------------------------------------------------------------------
# Static & Media Files
# ------------------------------------------------------------------------------

CONTENT_DIR = os.path.join(BASE_DIR, 'content')
STATIC_ROOT = os.path.join(CONTENT_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [CONTENT_DIR]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
