from django.contrib.auth import get_user_model

from rest_framework import permissions

User = get_user_model()


class IsAdminOnly(permissions.BasePermission):
    """authorization for only admin users"""

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False


class UserViewSetPermission(permissions.BasePermission):
    """permission config for the user route"""

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        elif view.action in ['login', 'refresh_token']:
            return True
        elif view.action in ['list', 'create']:
            return request.user.is_authenticated and request.user.is_superuser
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:  # noqa
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        if view.action == 'retrieve':
            return obj == request.user or request.user.is_superuser
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_superuser
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False
