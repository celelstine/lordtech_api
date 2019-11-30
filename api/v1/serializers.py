from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name',
            'last_name',
        )
        extra_kwargs = {
            'username': {
                'allow_null': False, 'required': True, 'allow_blank': False
            },
        }
