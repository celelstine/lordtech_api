from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name',
            'last_name', 'role', 'is_admin', 'is_superuser',
        )
        extra_kwargs = {
            'username': {
                'allow_null': False, 'required': True, 'allow_blank': False
            },
        }
        read_only_fields = ['is_admin']

    is_admin = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    def get_role(self, user):
        return user.get_role_display()

    def get_is_admin(self, user):
        return user.is_superuser
