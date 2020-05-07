from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .salesrep import SalesRep


class TradeSummary(BaseAppModelMixin):
    """class for summary of giftcard trade by sales rep"""

    sales_date = models.DateField(
        null=False,
        blank=False,
        default=now
    )
    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.GIFTCARD},
        related_name='trade_summaries')
    total_cash_received = models.FloatField(
        default=0.0,
        null=False,
        blank=False
    )
    total_cash_used = models.FloatField(
        default=0.0,
        null=False,
        blank=False
    )
    balance = models.FloatField(
        default=0.0,
        null=False,
        blank=False
    )
    # actual_balance = models.IntegerField(
    #     default=0,
    #     null=True,
    #     blank=True
    # )
    # outstanding = models.IntegerField(
    #     default=0,
    #     null=False,
    #     blank=False
    # )
    is_closed = models.BooleanField(default=False)

    def clean(self):
        # ensure that only giftcard sales rep have access to cash
        if self.sales_rep.category != SalesRep.GIFTCARD:
            raise ValidationError(
                'Invalid sales rep, only giftcard sales reps are allowed')

        # should not allow update when a record has been closed
        if self.create_date is not None:
            obj = TradeSummary.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        super(TradeSummary, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "Sales summary for %s on %s" % (
            self.sales_rep, self.sales_date)

    class Meta:
        verbose_name = 'Trade Sales Summary'
        verbose_name_plural = 'Trade Sales Summaries'
