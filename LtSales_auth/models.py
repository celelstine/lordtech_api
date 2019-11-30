from datetime import datetime, timedelta

import jwt

from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from utils.model_mixins import BaseAppModelMixin


class User(AbstractUser, BaseAppModelMixin):
    """custom user model to extend Django model"""

    DATA = 'da'
    GIFTCARD = 'gc'

    ROLE_CHOICES = [
        (DATA, 'Data Accountant'),
        (GIFTCARD, 'GIFTCARD Accountant'),
    ]

    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        blank=False,
        null=False
    )

    def get_refresh_token(self):
        """get refresh token for user if it exist else create one"""
        if not hasattr(self, 'refresh_token'):
            key = get_random_string(length=19)
            RefreshToken.objects.create(user=self, key=key)

        return self.refresh_token


class RefreshToken(BaseAppModelMixin):
    """Refrsh token for longer user session"""
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='refresh_token')
    key = models.CharField(unique=True, max_length=255)

    def generate_access_token(self):
        """generates a fresh access token"""
        key = get_random_string(length=19)
        self.key = key
        self.save()

        # create new access token
        expired_at = datetime.utcnow() + timedelta(days=1)
        access_token = jwt.encode(
            {'exp': expired_at, 'user_id': str(self.user_id)},
            settings.SECRET_KEY, algorithm='HS256'
        )

        result = {
            "expired_at": expired_at,
            "access_token": access_token,
            "refresh_token": key
        }

        return result
