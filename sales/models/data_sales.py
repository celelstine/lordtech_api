from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .dataplan import DataPlan
from .salesrep import SalesRep


class DataSales(BaseAppModelMixin):
    """class for data sales"""

    sales_date = models.DateField(
        null=False,
        blank=False,
        default=now
    )
    data_plan = models.ForeignKey(
        DataPlan,
        on_delete=models.CASCADE,
        related_name='sales'
        )
    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.DATA},
        related_name='sales')
    amount = models.PositiveIntegerField(null=False, blank=False)
    cost = models.FloatField(null=False, blank=True)
    total_mb = models.FloatField(null=False, blank=True)
    is_direct_sales = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    resend = models.BooleanField(default=False)


    def clean(self):
        # ensure that the data sub for recorded for only data sales reps
        if self.sales_rep.category != SalesRep.DATA:
            raise ValidationError(
                'Invalid sales rep, only data sales reps are allowed')

        # should not allow update when a record has been closed
        if self.create_date:
            obj = DataSales.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        # auto calculate cost
        self.cost = self.amount * self.data_plan.cost
        self.total_mb = self.amount * self.data_plan.mb
        super(DataSales, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%d of  %s sold by %s" % (
            self.amount, self.data_plan, self.sales_rep)

    class Meta:
        verbose_name = 'Data Sales'
        verbose_name_plural = 'Data Sales'
