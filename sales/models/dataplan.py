from django.db import models
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from sales.models import Product


class DataPlan(BaseAppModelMixin):
    """class for data plan"""

    network = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        limit_choices_to={'category': Product.DATA})
    name = models.CharField(max_length=50, blank=False, null=False)
    mb = models.PositiveIntegerField(null=False, blank=False)
    cost = models.PositiveIntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def clean(self):
        # ensure that the data plan are for data product
        if self.network.category != Product.DATA:
            raise ValidationError(
                'Invalid category, valid value should be %s' % Product.DATA)

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        super(DataPlan, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%s subscription for %s" % (self.name, self.network.name)

    class Meta:
        verbose_name = 'Data Plan'
        verbose_name_plural = 'Data Plan'
        unique_together = ('network', 'name')
