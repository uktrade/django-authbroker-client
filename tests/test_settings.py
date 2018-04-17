import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'tests'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SSO_BROKER_URL = 'https://sso.test.gov.uk/'
SSO_REDIRECT_URI = 'https://localhost/'
SSO_CLIENT_ID = '01234567890abcdefg'
SSO_CLIENT_SECRET = 'qwertyuioplkjhgfdsa'
SSO_AUTHENTICATION_TEMPLATE = 'auth.html'
