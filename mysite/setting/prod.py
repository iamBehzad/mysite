from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-85lm3kyv&^(%bqfez7pmit7prqs9vg+u3n!@=!5+yfbt0@or(@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

#INSTALLED_APPS = []

# site framework
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': BASE_DIR /'my-db',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

#CSRF_COOKIE_SECURE = True