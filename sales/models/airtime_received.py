from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .salesrep import SalesRep


class AirtimeReceived(BaseAppModelMixin):
    """class for airtime Received by sales rep"""

    date = models.DateField(
        null=False,
        blank=False,
        default=now
    )
    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.DATA},
        related_name='airtime_received')
    amount = models.FloatField(null=False, blank=False)
    is_closed = models.BooleanField(default=False)

    def clean(self):
        # ensure that the data sub for recorded for only data sales reps
        if self.sales_rep.category != SalesRep.DATA:
            raise ValidationError(
                'Invalid sales rep, only data sales reps are allowed')

        # should not allow update when a record has been closed
        if self.create_date is not None:
            obj = AirtimeReceived.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        super(AirtimeReceived, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%s -  %s" % (self.amount, self.sales_rep)

    class Meta:
        verbose_name = 'Airtime Received'
        verbose_name_plural = 'Airtime Received'
