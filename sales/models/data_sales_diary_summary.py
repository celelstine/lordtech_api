from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .salesrep import SalesRep


class DataSalesSummary(BaseAppModelMixin):
    """class for data sales summary"""
    sales_date = models.DateTimeField(
        null=False,
        blank=False,
        default=now
    )
    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.DATA},
        related_name='summaries')
    Start_airtime = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        default=0.0,
        null=False,
        blank=False
    )
    Start_data = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        default=0.0,
        null=False,
        blank=False
    )
    total_airtime_received = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    total_direct_Sales = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    total_sub_made = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    expected_airtime = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    actual_airtime = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    expected_data_balance = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    actual_data_balance = models.FloatField(
        default=0,
        null=False,
        blank=False
    )
    total_data_shared = models.FloatField(
        null=False,
        blank=False
    )
    no_order_treated = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    outstanding = models.FloatField(
        default=0.0,
        null=False,
        blank=False
    )
    is_closed = models.BooleanField(default=False)
    resend_data = models.FloatField(
        default=0.0,
        null=True,
        blank=True
    )

    def clean(self):
        # ensure that the data sub for recorded for only data sales reps
        if self.sales_rep.category != SalesRep.DATA:
            raise ValidationError(
                'Invalid sales rep, only data sales reps are allowed')

        # should not allow update when a record has been closed
        if self.create_date:
            obj = DataSalesSummary.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        super(DataSalesSummary, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "Sales summary for %s on %s" % (
            self.sales_rep, self.sales_date)

    class Meta:
        verbose_name = 'Data Sales Summary'
        verbose_name_plural = 'Data Sales Summaries'
