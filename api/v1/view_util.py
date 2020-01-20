"""utilility functions for views"""
from rest_framework import status
from rest_framework.response import Response


def failed_login():
    return Response('Wrong username or password.',
                    status=status.HTTP_401_UNAUTHORIZED)


def forbidden():
    return Response('Retrieve action not allowed.',
                    status=status.HTTP_403_FORBIDDEN)


def coming_up_soon():
    return Response('coming up soon!!!',
                    status=status.HTTP_503_SERVICE_UNAVAILABLE)
