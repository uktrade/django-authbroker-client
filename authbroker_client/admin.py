from django.contrib import admin
from .models import Credentials


class CredentialsInline(admin.StackedInline):
    model = Credentials
    can_delete = False
    verbose_name_plural = 'user credentials'


class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Credentials, CredentialsAdmin)
