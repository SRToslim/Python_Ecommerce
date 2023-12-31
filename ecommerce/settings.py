"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)%8#gcf9mx6=hhk_j_sgv+w8+t#qhfw%-6i7#i^6u)j(y+d*i5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Customs
    'userauth',
    'home',
    'dashboard',
    'products',
    'web_settings',

    # Third Party
    'taggit',
    'ckeditor',
    'captcha',
    'fontawesomefree',
    'rosetta',
    'active_link',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'web_settings.context_processor.default',
                'products.context_processors.default',
                'userauth.context_processors.default',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'userauth.backend.UsernameOrEmail',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

AUTH_USER_MODEL = 'userauth.User'

RECAPTCHA_PUBLIC_KEY = '6Lf8000nAAAAALe8vorkf7tCfMWUbxy-fr0xFGjn'
RECAPTCHA_PRIVATE_KEY = '6Lf8000nAAAAANGgdAppvkBrF6zo9FETrnCkUZs_'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

JAZZMIN_SETTINGS = {
    'site_title': 'Lavender',
    "site_header": 'Online',

    'site_brand': 'Lavender Online',
    'site_logo': 'favicon.png',
    'login_logo': 'logo.png',
    # "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": 'favicon.png',
    'copyright': ' - <a href="https://github.com/srtoslim" target="_blank">SRToslim</a>',
    # "user_avatar": 'request.user.image.url',
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index"},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Website", "url": "http://127.0.0.1:8000", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "userauth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "products"},
    ],
    'search_model': 'userauth.User',
    'welcome_sign': 'Welcome to Lavender Online',
    'use_google_fonts_cdn': True,
    'icons': {
        'account.emailaddress': 'fas fa-at',
        'auth.group': 'fas fa-layer-group',
        'products.brand': 'far fa-registered',
        'products.category': 'fas fa-list',
        'products.product': 'fab fa-product-hunt',
        'sites.site': 'fas fa-globe',
        'socialaccount.socialaccount': 'far fa-user-circle',
        'taggit.tag': 'fas fa-tags',
        'userauth.profile': 'far fa-id-badge',
        'userauth.user': 'fas fa-users',
        'web_settings.currency': 'fas fa-lira-sign',
    },
    'default_icon_parents': 'fas fa-chevron-circle-right',
    "default_icon_children": "fas fa-circle",
}

JAZZMIN_UI_TWEAKS = {
    "accent": "accent-info",
    "navbar_fixed": True,
    "footer_fixed": True,
    "sidebar_fixed": True,
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'support@helpbazar.com'
EMAIL_HOST_USER = 'srtoslim@gmail.com'
EMAIL_HOST_PASSWORD = 'yauwavpnsreektgr'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.lavendersuperstore.com.bd'
# EMAIL_FROM = 'support@lavendersuperstore.com.bd'
# EMAIL_HOST_USER = 'support@lavendersuperstore.com.bd'
# EMAIL_HOST_PASSWORD = 'EZ!0h~P]N$!&TpS[V{'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


PASSWORD_RESET_TIMEOUT = 14400

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'all',
    }
}

SMS_API_TOKEN = 'jh0fiy2s-gdgcf1ui-5sk0ungx-3spvr5ml-1dnofs8z'
SMS_SID = 'LAVENDERAPI'
SMS_URL = 'https://smsplus.sslwireless.com/api/v3/send-sms'
