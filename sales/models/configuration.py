from django.db import models

from utils.model_mixins import BaseAppModelMixin


class Configuration(BaseAppModelMixin):
    """class for general configurations"""

    DATA = 'da'
    GIFTCARD = 'gc'
    ALL = 'all'

    CATEGORY_CHOICES = [
        (DATA, 'Data'),
        (GIFTCARD, 'GIFTCARD'),
        (ALL, 'all'),
    ]

    key = models.CharField(max_length=50, blank=False, null=False)
    value = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False,
        default=ALL
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('category', 'key')
