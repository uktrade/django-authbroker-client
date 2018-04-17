from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from . import SSO_AUTHENTICATION_TEMPLATE
from .client import get_login_url, get_access_token, get_profile


class SSOAuthView(TemplateView):
    template_name = SSO_AUTHENTICATION_TEMPLATE

    def success_callback(self, auth_data=None):
        """
        To be implemented  by an extending View object.
        This method receives the result of the SSO authentication process, including
        all access token and profile data.
        This method is meant to return either a redirect or a rendering
        of a template.
        By default, it returns a redirect to root (`/`)
        """
        return redirect('/')

    def get(self, request, *args, **kwargs):
        error = request.GET.get('error')
        error_description = request.GET.get('error_description')
        code = request.GET.get('code')
        # If no error or code provided, redirect to the SSO login url
        if not error and not code:
            return redirect(get_login_url())
        elif code:  # if code is provided, exchange it for a token
            _token = get_access_token(code)
            if _token:
                profile = get_profile(_token.get('access_token'))
                # collect token and profile data into one dict
                auth_data = {**profile, **_token}
                # if implemented by extending View, the callback gets the auth data generated
                return self.success_callback(auth_data=auth_data)
            else:
                return redirect(get_login_url())
        return render(request, self.template_name, {
            'error': error,
            'error_description': error_description,
            'profile': profile
        })
