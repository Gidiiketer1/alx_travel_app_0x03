from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'alx-secret-key'

DEBUG = True

ALLOWED_HOSTS = []


# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'django_celery_results',

    # Local apps
    'listings',
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


# =========================
# URL CONFIG
# =========================
ROOT_URLCONF = 'alx_travel_app.urls'


# =========================
# DATABASE
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_TZ = True


# =========================
# STATIC FILES
# =========================
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# EMAIL CONFIGURATION
# =========================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@alxtravel.com'


# =========================
# CELERY CONFIGURATION
# =========================
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'django-db'
