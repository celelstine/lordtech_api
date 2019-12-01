from django.db import models
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from sales.models import Product


class DataSubscription(BaseAppModelMixin):
    """class for subscription by sales rep"""

    network = models.OneToOneField(
        Product,
        on_delete=models.CASCADE)
    mb_per_sub = models.PositiveIntegerField(null=False, blank=False)
    cost_per_sub = models.PositiveIntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def clean(self):
        # ensure that the sub are for data product
        if self.network.category != Product.DATA:
            raise ValidationError(
                'Invalid category, valid value should be %s' % Product.DATA)

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        super(DataSubscription, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%s - subscription" % self.network.name

    class Meta:
        verbose_name = 'Data Subscription'
        verbose_name_plural = 'Data Subscriptions'
