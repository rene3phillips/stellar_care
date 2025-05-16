import environ
import os
from pathlib import Path

# Initialize environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
env_file_path = BASE_DIR / '.env'
if os.path.exists(env_file_path):
        environ.Env.read_env(env_file_path)

# Quick-start development settings - unsuitable for production
# See [https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)

# SECURITY WARNING: keep the secret key used in production secret!
# Raises Django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: Never commit your actual SECRET_KEY to version control. Ensure your .env file is in .gitignore.

# SECURITY WARNING: don't run with debug turned on in production!
# Reads value from .env file, falls back to False if not set
DEBUG = env.bool('DEBUG') 

ALLOWED_HOSTS = [] # Keep empty for now, will configure later

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Required by allauth
    'django.contrib.sites', 
    # Records app
    'records.apps.RecordsConfig', 
    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Providers
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1 # Required by sites framework

LOGIN_REDIRECT_URL = 'records:patient_list'
# LOGOUT_REDIRECT_URL = 'records:patient_list'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False # Or True, depending on your model needs
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Or 'username' or 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional' # Or 'mandatory' or 'none'
LOGIN_REDIRECT_URL = '/' # URL to redirect to after login (e.g., home page)
ACCOUNT_LOGOUT_REDIRECT_URL = '/' # URL to redirect to after logout
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True # Optional
# ACCOUNT_SESSION_REMEMBER = True # Optional

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': '' # Keep empty
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'stellar_care.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'stellar_care.wsgi.application'

# Database
# [https://docs.djangoproject.com/en/5.2/ref/settings/#databases](https://docs.djangoproject.com/en/5.2/ref/settings/#databases)
# Uses DATABASE_URL from .env file
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db()
}

# Password validation
# [https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators](https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators)
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
# [https://docs.djangoproject.com/en/5.2/topics/i18n/](https://docs.djangoproject.com/en/5.2/topics/i18n/)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# [https://docs.djangoproject.com/en/5.2/howto/static-files/](https://docs.djangoproject.com/en/5.2/howto/static-files/)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # This points to the 'static' folder at the project root
]

# Default primary key field type
# [https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field](https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'