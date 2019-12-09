from django.db import models
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from sales.models import (
    DataSubscription,
    SalesRep
)


class SalesRepDataSubscription(BaseAppModelMixin):
    """class for data plan"""

    sub = models.ForeignKey(DataSubscription, on_delete=models.CASCADE)
    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.DATA},
        related_name='subscriptions')
    amount = models.PositiveIntegerField(null=False, blank=False)
    cost = models.PositiveIntegerField(null=True, blank=True)
    is_closed = models.BooleanField(default=False)

    def clean(self):
        # ensure that the data sub for recorded for only data sales reps
        if self.sales_rep.category != SalesRep.DATA:
            raise ValidationError(
                'Invalid sales rep, only data sales reps are allowed')

        # should not allow update when a record has been closed
        if self.create_date:
            obj = SalesRepDataSubscription.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        # auto calculate cost
        self.cost = self.amount * self.sub.cost_per_sub
        super(SalesRepDataSubscription, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%s by  %s" % (self.sub, self.sales_rep)

    class Meta:
        verbose_name = 'Sales Rep Data Subscription'
        verbose_name_plural = 'Sales Rep Data Subscriptions'
