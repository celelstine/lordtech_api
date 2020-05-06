from django.db import models
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .salesrep import SalesRep
from .product import Product
from .trade_group import TradeGroup


class Trade(BaseAppModelMixin):
    """class for giftcard trade by sales rep"""

    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.GIFTCARD},
        related_name='trades')
    trade_group = models.ForeignKey(
        TradeGroup,
        blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='trades')
    card = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        limit_choices_to={'category': Product.GIFTCARD},
        related_name='trades')
    selling_rate = models.PositiveIntegerField('Selling rate (Yuan)',
                                               blank=True, null=True)
    buying_rate = models.FloatField('Buying rate (Naira)',
                                    blank=True, null=True)
    amount = models.PositiveIntegerField(null=False, blank=False)
    amount_paid = models.FloatField(null=True, blank=True)
    order_id = models.CharField(
        blank=True, null=True, max_length=20, unique=True)
    is_closed = models.BooleanField(default=False)

    def clean(self):
        # ensure that only giftcard sales rep have access to cash
        if self.sales_rep.category != SalesRep.GIFTCARD:
            raise ValidationError(
                'Invalid sales rep, only giftcard sales reps are allowed')

        # ensure that the product is a giftcard
        if self.card.category != Product.GIFTCARD:
            raise ValidationError(
                'Invalid product, only giftcard product are allowed')

        # should not allow update when a record has been closed
        if self.create_date is not None:
            obj = Trade.objects.values('is_closed').get(
                pk=self.pk)
            if obj['is_closed'] is True:
                raise ValidationError('Can update a closed record')
    
    @property
    def is_valid(self):
        # we are only checking for nullable fields that are required
        return True if self.selling_rate and self.buying_rate and self.trade_group else False


    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        # auto calculate amount_paid
        if self.buying_rate:
            self.amount_paid = self.amount * self.buying_rate
        super(Trade, self).save(*args, **kwargs)

    def __str__(self):
        """customize the string representation"""
        return "%d of  %s sold by %s" % (
            self.amount, self.card, self.sales_rep)

    class Meta:
        verbose_name = 'Trade'
        verbose_name_plural = 'Trades'
