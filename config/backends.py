import logging
import jwt

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions


User = get_user_model()
LOGGER = logging.getLogger(__name__)


class AccessTokenBackend(authentication.BaseAuthentication):
    """
    Authenticate against access token
    """

    def authenticate(self, request):
        """get the use via api key"""
        auth = request.META.get('HTTP_AUTHORIZATION', '').split()
        if auth == []:
            return None

        if len(auth) != 2:
            raise exceptions.AuthenticationFailed(
                'Invalid authorization header.')
        access_token = auth[1]

        try:
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('user_id', None)
            if user_id is None:
                raise exceptions.AuthenticationFailed(
                    'Invalid Token, please login/signup')
            user = User.objects.get(pk=user_id)
            return (user, None)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'Expired access token; pleae use refresh token to get a valid token')  # noqa
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                'Invalid Token, please login/signup')
        except Exception:
            raise exceptions.AuthenticationFailed('Unknown error')

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
