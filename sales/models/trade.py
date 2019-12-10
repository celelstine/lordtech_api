from django.db import models
from django.core.exceptions import ValidationError

from utils.model_mixins import BaseAppModelMixin

from .salesrep import SalesRep
from .product import Product


class Trade(BaseAppModelMixin):
    """class for giftcard trade by sales rep"""

    sales_rep = models.ForeignKey(
        SalesRep,
        on_delete=models.CASCADE,
        limit_choices_to={'category': SalesRep.GIFTCARD},
        related_name='trades')
    group = models.CharField(blank=True, null=True, max_length=50)
    card = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        limit_choices_to={'category': Product.GIFTCARD},
        related_name='trades')
    selling_rate = models.PositiveIntegerField('Selling rate (Yuan)',
                                               blank=False, null=False)
    buying_rate = models.PositiveIntegerField('Buying rate (Naira)',
                                              blank=False, null=False)
    amount = models.PositiveIntegerField(null=False, blank=False)
    amount_paid = models.PositiveIntegerField(null=True, blank=True)
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

    def save(self, *args, **kwargs):
        # ensure that the clean method is call on every save
        self.clean()
        # auto calculate cost
        self.amount_paid = self.amount * self.buying_rate
        super(Trade, self).save(*args, **kwargs)
