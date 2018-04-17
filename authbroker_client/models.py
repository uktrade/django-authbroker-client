import uuid
from django.db import models
from django.auth.models import User


TOKEN_TYPES = (
    ('Bearer', 'Bearer'),
)


class Credentials(models.Model):
    """
    A credentials model to hold a user's SSO tokens and relevant data.
    This model would be installed if the app is included in the INSTALLED_APPS
    settings variable. It is only required for backends that manage a relationship
    between SSO and a local user.
    """
    user = models.OneToOneField(User, primary_key=True, editable=False, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=50, null=True, blank=True)
    refresh_token = models.CharField(max_length=50, null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    scope = models.TextField(null=True, blank=True)
    token_type = models.CharField(max_length=50, null=True, blank=True, choices=TOKEN_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Credentials for {self.user.email}"

    @staticmethod
    def for_user(user):
        """
        Return a credentials object for a user.
        """
        try:
            return Credentials.objects.get(user=user)
        except Credentials.DoesNotExist:
            return None
