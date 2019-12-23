from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from api.v1.serializers import UserSerializer
from config.authentication import UserViewSetPermission
from api.v1.view_util import (
    coming_up_soon,
    failed_login
)

from LtSales_auth.models import RefreshToken
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """You can handle every authentication and user management on your account """ # noqa
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = (UserViewSetPermission,)

    def create(self, request):
        """create a new user; this route is only accessible to admins
        ```{
            "username": "",
            "role": ''
        }```
        """
        username = request.data.get('username', None)
        role = request.data.get('role', None)

        if username is None or role is None:
            return Response("Please a username and role",
                            status=status.HTTP_400_BAD_REQUEST)

        # validate the role
        roles = [r[0] for r in User.ROLE_CHOICES]

        if role not in roles:
            return Response("Invalid role, choose one from: %s" % ','.join(roles),  # noqa
                            status=status.HTTP_400_BAD_REQUEST)

        # create new user
        (u, created) = User.objects.get_or_create(
            username=username,
            defaults={'email': username, 'is_staff': True, 'role': role}
        )

        if not created:
            return Response('User with username: %s already exist' % username,
                            status=status.HTTP_400_BAD_REQUEST)
        # generate random password
        password = User.objects.make_random_password()
        u.set_password(password)
        u.save()

        response = {
            'username': username,
            'password': password,
            'role': role
        }

        return Response(response, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def login(self, request, pk=None):
        """login route, via username and password"""
        # check if user is already login
        # we check the type as the route is not protected, so we might get a type of AnonymousUser # noqa
        if request.user.is_authenticated:
            return Response("Hey, you have an active session already. "
                            "If you still want to login; please logout first.",
                            status=status.HTTP_400_BAD_REQUEST)

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username is None or password is None:
            return Response("Please provide both username and password.",
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = self.queryset.get(username=username)
            if not user.check_password(password):
                return failed_login()

            refresh_token = user.get_refresh_token()
            response = refresh_token.generate_access_token()
            response.update({
                'username': username, 'role': user.get_role_display()})
            return Response(response)
        except User.DoesNotExist:
            return failed_login()

    @action(methods=['post'], detail=False)
    def logout(self, request, pk=None):
        """logout a user, simply delete the token attached to the user"""
        user = request.user
        if hasattr(self, 'refresh_token'):
            user.refresh_token.delete()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def refresh_token(self, request):
        """
        get new access token with a refresh token, please do not pass refresh
        token as an authorization header. Pass it as a header: Refresh-Token
        """
        refresh_token_key = request.headers.get('Refresh-Token', None)

        if refresh_token_key is None:
            return Response("Could not fetch refresh token from request,"
                            "Please pass token in request header with key: "
                            "Refresh-Token",
                            status=status.HTTP_400_BAD_REQUEST)

        # get token and generate refresh token
        try:
            refresh_token = RefreshToken.objects.get(key=refresh_token_key)
            auth = refresh_token.generate_access_token()
            return Response(auth)
        except RefreshToken.DoesNotExist:
            return Response('Invalid refresh token; please login',
                            status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def reset_password(self, request):
        """
        reset a user's password, only accessible to admin
        """
        username = request.data.get('username', None)

        if username is None:
            return Response('Please provide the username that you want to reset',  # noqa
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            u = self.queryset.get(username=username)

            # generate random password
            password = User.objects.make_random_password()
            u.set_password(password)
            u.save()

            response = {
                'username': username,
                'password': password,
            }
            return Response(response)
        except User.DoesNotExist:
            return Response('User with username: %s does not exist' % username,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        return coming_up_soon()

    def partial_update(self, request, pk=None, *args, **kwargs):
        return coming_up_soon()

    def destroy(self, request, pk=None):
        return coming_up_soon()
