from django.db import models
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .salesrep import SalesRep


class AirtimeRecieved(BaseAppModelMixin):
    """class for airtime recieved by sales rep"""

    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.DATA},)
    amount = models.PositiveIntegerField(null=False, blank=False)
    is_closed = models.BooleanField(default=False)

    def clean(self):
        # ensure that the data sub for recroded for only data sales reps
        if self.sales_rep.category != SalesRep.DATA:
            raise ValidationError(
                'Invalid sales rep, only data sales reps are allowed')

        # should not allow update when a record has been closed
        if self.create_date is not None:
            obj = AirtimeRecieved.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        super(AirtimeRecieved, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%s -  %s" % (self.amount, self.sales_rep)

    class Meta:
        verbose_name = 'Airtime Recieved'
        verbose_name_plural = 'Airtime Recieved'
