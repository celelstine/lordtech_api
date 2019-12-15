from django.db import models
from django.utils.timezone import now

from utils.model_mixins import BaseAppModelMixin

from .product import Product


class Profit(BaseAppModelMixin):
    """class for profit per product per sales shift"""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='profits')
    amount = models.IntegerField(null=False, blank=False)
    sales_date = models.DateTimeField(
        null=False,
        blank=False,
        default=now
    )

    def __str__(self):
        """customize the string representation"""
        return "profit of %d for %s on %s" % (
            self.amount, self.product, self.create_date)

    class Meta:
        verbose_name = 'Profit'
        verbose_name_plural = 'Profit'
