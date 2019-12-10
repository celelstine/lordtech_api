from django.db import models

from utils.model_mixins import BaseAppModelMixin


class SalesRep(BaseAppModelMixin):
    """class for sales rep"""

    DATA = 'da'
    GIFTCARD = 'gc'

    CATEGORY_CHOICES = [
        (DATA, 'Data'),
        (GIFTCARD, 'GIFTCARD'),
    ]

    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(default=True)
    cash_balance = models.IntegerField(default=0)
    airtime_balance = models.IntegerField(default=0)
    data_balance = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Sales Rep'
        verbose_name_plural = 'Sales Reps'
        unique_together = ('category', 'name')

    def __str__(self):
        """customize the string representation"""
        return "%s (department %s)" % (self.get_category_display(), self.name)
