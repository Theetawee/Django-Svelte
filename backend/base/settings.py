import os
from pathlib import Path
from django.contrib.messages import constants as messages
"""
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()
"""


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'main',
    'corsheaders',
    "cloudinary_storage",
    "cloudinary",
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.common.CommonMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



if DEBUG == True:
    STATIC_URL = "static/"
    
    MEDIA_URL = "media/"
    
    ALLOWED_HOSTS=['*']
    
    CORS_ALLOWED_ORIGINS = [
        
    ]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        os.path.join(BASE_DIR, "media"),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

    MEDIA_ROOT = os.path.join(BASE_DIR, "media_cdn")

    INTERNAL_IPS = [
        "127.0.0.1",
    ]

else:
    ALLOWED_HOSTS = ['*']
    CORS_ALLOWED_ORIGINS = [
        
    ]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "neondb",
            "USER": "foreverinc",
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": "ep-blue-violet-792186.us-east-2.aws.neon.tech",
            "PORT": "5432",
        }
    }

    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": "dnb8rethz",
        "API_KEY": "123456789",
        "API_SECRET": os.environ.get("API_SECRET"),
    }

    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

    STATIC_URL = "waanverse/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "redodevs@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USE_TLS = True

MESSAGE_TAGS = {
    messages.ERROR: "danger",
}
