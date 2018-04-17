from django.test import TestCase
from unittest import mock
from django.conf import settings
from authbroker_client.client import (
    get_login_url, get_access_token, get_profile, SSO_ENDPOINTS
)
import requests


def mocked_access_token(*args, **kwargs):
    class MockResponse:
        status_code = 200

        def json(self):
            return {
                'access_token': '01234567890abcdefg',
                'refresh_token': 'qwerty',
            }
    return MockResponse()


def mocked_get_profile(*args, **kwargs):
    class MockResponse:
        status_code = 200

        def json(self):
            return {
                'email': 'harel@harelmalka.com',
                'first_name': 'Harel',
                'last_name': 'Malka',
            }
    return MockResponse()


class ClientTest(TestCase):
    def test_get_login_endpoint(self):
        login_url = get_login_url()
        expected = (
            f"{settings.SSO_BROKER_URL}{SSO_ENDPOINTS['authorize']}?redirect_uri="
            f"{settings.SSO_REDIRECT_URI}&client_id={settings.SSO_CLIENT_ID}"
            f"&client_secret={settings.SSO_CLIENT_SECRET}"
            f"&response_type=code"
        )
        assert login_url == expected


    @mock.patch('requests.post', side_effect=mocked_access_token)
    def test_access_token(self, *args):
        auth_data = get_access_token('code')
        assert auth_data['access_token'] == '01234567890abcdefg'


    @mock.patch('requests.get', side_effect=mocked_get_profile)
    def test_profile(self, *args):
        profile = get_profile('token')
        assert profile['first_name'] == 'Harel'
        assert profile['last_name'] == 'Malka'
