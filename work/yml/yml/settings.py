"""
Django settings for yml project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5cf3*cvng4@e7w-+d()n3&_w6pz&351kohn5&%@$v3%0$uedu7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['39.105.162.163','localhost']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_crontab',
    'django.contrib.staticfiles',
    'rest_framework',
    'secondtime',
    'Wordprocessing',
    'fileupload',
    'captcha',
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

ROOT_URLCONF = 'yml.urls'

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

WSGI_APPLICATION = 'yml.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mshd',
        'USER': 'root',     # 用户名，可以自己创建用户
        'PASSWORD': '121511',  # 密码
        'HOST': '39.105.162.163',  # mysql服务所在的主机ip
        'PORT': '3306',         # mysql服务端口
        'OPTIONS': {"init_command": "SET storage_engine=MyISAM"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


TEMPLATES_DIR=(
    os.path.join(BASE_DIR,'templates')
)

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
BASE_PATH=os.path.join(BASE_PATH,'../')

STATICFILES_DIRS = (
    os.path.join(BASE_PATH, 'static/'),
)

CRONJOBS = [
    # 分 时 日 月 周      命令
<<<<<<< HEAD
    ('*/20 * * * *', 'secondtime.timework.timeWorkWriteFileToDb','>> ~/data.txt')
]
=======
    ('*/20 * * * *', 'secondtime.timework.timeWorkWriteFileToDb','>> ~/data.txt'),
    ('*/20 * * * *', 'secondtime.timework.backupDb','>> ~/db.log'),
    

]
>>>>>>> ea648a2f0ab27435d98896c2cc76ce2c9ee9e811
