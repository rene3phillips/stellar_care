import environ
import os
from pathlib import Path

# Load environmental variables
env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent
env_file_path = BASE_DIR / '.env'
if os.path.exists(env_file_path):
        environ.Env.read_env(env_file_path)

# Basic settings
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG') 
ALLOWED_HOSTS = [] 

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # Required by allauth, supports multiple sites/domains (site_id = 1)

    # Third-party
    'rest_framework',
    'drf_spectacular',
    'allauth', # allauth base app
    'allauth.account', # handles user registration, login, logout, etc.
    'allauth.socialaccount', # enables social authentication
    'allauth.socialaccount.providers.google', # adds Google as an authentication method
    'django_filters',

    # Local apps
    'records.apps.RecordsConfig',
]

SITE_ID = 1 # Required by allauth

# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # Allows login using username and password via the Django admin
    'allauth.account.auth_backends.AuthenticationBackend', # Enables allauth to handle authentication using email, social, etc.
)

# ACCOUNT_EMAIL_REQUIRED = True # email required for signup and login
ACCOUNT_LOGIN_METHODS = {'email'} # New
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*'] # New
# ACCOUNT_USERNAME_REQUIRED = False  
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional' 
LOGIN_REDIRECT_URL = '/' # will redirect to /records/ due to project urls.py
ACCOUNT_LOGOUT_REDIRECT_URL = '/' 
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True 
ACCOUNT_SESSION_REMEMBER = True 

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID'),
            'secret': env('GOOGLE_CLIENT_SECRET'),
            'key': '' 
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

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # required by allauth
]

# Templates
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

# URLs & WSGI
ROOT_URLCONF = 'stellar_care.urls'
WSGI_APPLICATION = 'stellar_care.wsgi.application'

# Database
DATABASES = {
    'default': env.db()
}

# Password validation
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

# REST framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # Uses Django sessions to authenticate users
        'rest_framework.authentication.SessionAuthentication',
        # Use for Postman testing
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # By default, it requires users to be logged in to view an API endpoint
        'rest_framework.permissions.IsAuthenticated',
    ], 
    'DEFAULT_FILTER_BACKENDS': [
        # Enables filtering, search, and ordering of API results with queries
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    # Enables pagination using page numbers
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # Sets default number of items per page
    'PAGE_SIZE': 10,  
    # Uses drf_spectacular to create schema documentation
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema', 
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'