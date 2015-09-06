"""
Django settings for schedule project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3o5f5^m7)!z3=a!hqy2fe!m)=x6qag2nnih6bgi)k@d9#*5jd+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'crispy_forms',
    'registration',
    'timetable',
    'messageboard',
    'approval',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'schedule.urls'

WSGI_APPLICATION = 'schedule.wsgi.application'

AUTH_USER_MODEL = 'registration.MyUser'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#login settings
LOGIN_REDIRECT_URL = '/schedule/userpage'
LOGIN_URL='/accounts/login/'

# Template directory settings
TEMPLATE_DIRS=[os.path.join(BASE_DIR,'templates')]

#static files settings
STATIC_PATH= os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS=[STATIC_PATH,]

STATIC_ROOT=os.path.join(BASE_DIR,'static_root')

MEDIA_URL= '/media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')

#crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'