from django.conf import settings
from .version import __version__
__author__ = 'Harel Malka'


# The broker to use for Staff SSO
SSO_BROKER_URL = getattr(settings, 'SSO_BROKER_URL')
# The full url and path to redirect to after each authentication step
SSO_REDIRECT_URI = getattr(settings, 'SSO_REDIRECT_URI')
# The SSO client id
SSO_CLIENT_ID = getattr(settings, 'SSO_CLIENT_ID')
# The SSO client secret
SSO_CLIENT_SECRET = getattr(settings, 'SSO_CLIENT_SECRET')
# path to a template to use to display any resulting errors from the SSO process
SSO_AUTHENTICATION_TEMPLATE = getattr(settings, 'SSO_AUTHENTICATION_TEMPLATE', 'authentication.html')


required_vars = [SSO_BROKER_URL, SSO_REDIRECT_URI, SSO_CLIENT_ID, SSO_CLIENT_SECRET]
if not all([bool(var) for var in required_vars]):
    raise NotImplementedError(f"{', '.join(required_vars)} are required in settings")
