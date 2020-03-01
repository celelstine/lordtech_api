from django.db import models

from utils.model_mixins import BaseAppModelMixin


class TradeGroup(BaseAppModelMixin):
    """class for trade group"""

    NAIRA = 'naira'
    YUAN = 'yuan'

    CURRENCY_CHOICES = [
        (NAIRA, 'naira'),
        (YUAN, 'yuan'),
    ]
    name = models.CharField(blank=True, null=True, unique=True, max_length=20)
    balance = models.PositiveIntegerField(null=False, blank=False, default=0)
    selling_currency = models.CharField(
        max_length=20,
        choices=CURRENCY_CHOICES,
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(default=True)
