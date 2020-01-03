from datetime import datetime
from django.db.models import Sum
from django.utils.timezone import now
from django.db import transaction

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters

from config.authentication import IsAdminOnlyPermission

from api.v1.filters import ProfitFilter
from api.v1.serializers import (
    AirtimeRecievedSerializer,
    AirtimeRecievedGetSerializer,
    CashRecievedSerializer,
    CashRecievedGetSerializer,
    ConfigurationSerializer,
    DataPlanSerializer,
    DataPlanGetSerializer,
    DataSalesSerializer,
    DataSalesGetSerializer,
    DataSalesSummarySerializer,
    DataSubscriptionSerializer,
    DataSubscriptionGetSerializer,
    ProductSerializer,
    ProfitSerializer,
    SalesRepSerializer,
    SalesRepDataSubscriptionSerializer,
    SalesRepDataSubscriptionGetSerializer,
    TradeSerializer,
    TradeGetSerializer,
    TradeSummarySerializer
)

from sales.models import (
    AirtimeRecieved,
    CashRecieved,
    Configuration,
    DataPlan,
    DataSales,
    DataSalesSummary,
    DataSubscription,
    Product,
    Profit,
    SalesRep,
    SalesRepDataSubscription,
    Trade,
    TradeSummary
)


class ConfigurationViewSet(viewsets.ModelViewSet):
    """Manage configurations"""
    queryset = Configuration.objects.filter(is_active=True).order_by('id')
    serializer_class = ConfigurationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category', 'key', )

    def create(self, request):
        """customize create method to validate object category"""
        category = request.data.get('category', None)

        if category is None:
            return Response("Please a category",
                            status=status.HTTP_400_BAD_REQUEST)

        # validate the category
        categories = [r[0] for r in Configuration.CATEGORY_CHOICES]

        if category not in categories:
            return Response("Invalid category, choose one from: %s" % ','.join(categories),  # noqa
                            status=status.HTTP_400_BAD_REQUEST)

        return super(ConfigurationViewSet, self).create(request)


class SalesRepViewSet(viewsets.ModelViewSet):
    """manage sales representatives"""
    queryset = SalesRep.objects.filter(is_active=True).order_by('id')
    serializer_class = SalesRepSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'category',)

    def create(self, request):
        """customize create method to validate object category"""
        category = request.data.get('category', None)

        if category is None:
            return Response("Please a category",
                            status=status.HTTP_400_BAD_REQUEST)

        # validate the category
        categories = [r[0] for r in SalesRep.CATEGORY_CHOICES]

        if category not in categories:
            return Response("Invalid category, choose one from: %s" % ','.join(categories),  # noqa
                            status=status.HTTP_400_BAD_REQUEST)

        return super(SalesRepViewSet, self).create(request)


class ProductViewSet(viewsets.ModelViewSet):
    """manage product"""
    queryset = Product.objects.filter(is_active=True).order_by('id')
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'category',)

    def create(self, request):
        """customize create method to validate object category"""
        category = request.data.get('category', None)

        if category is None:
            return Response("Please a category",
                            status=status.HTTP_400_BAD_REQUEST)

        # validate the category
        categories = [r[0] for r in Product.CATEGORY_CHOICES]

        if category not in categories:
            return Response("Invalid category, choose one from: %s" % ','.join(categories),  # noqa
                            status=status.HTTP_400_BAD_REQUEST)

        return super(ProductViewSet, self).create(request)


class DataSubscriptionViewSet(viewsets.ModelViewSet):
    """manage DataSubscription"""
    queryset = DataSubscription.objects.filter(is_active=True).order_by('id')
    # serializer_class = DataSubscriptionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('network',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DataSubscriptionGetSerializer
        return DataSubscriptionSerializer


class DataPlanViewSet(viewsets.ModelViewSet):
    """manage Dataplan"""
    queryset = DataPlan.objects.filter(is_active=True).order_by('id')
    # serializer_class = DataPlanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('network', 'name',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DataPlanGetSerializer
        return DataPlanSerializer


def is_closed_record(model, pk, action='update'):
    try:
        obj = model.objects.get(pk=pk)
        if obj.is_closed is True:
            return Response('Can not %s a closed record' % action,
                            status=status.HTTP_400_BAD_REQUEST)
    except model.DoesNotExist:
        return Response('Record was not found',
                        status=status.HTTP_404_NOT_FOUND)

    return False


class SalesRepDataSubscriptionViewSet(viewsets.ModelViewSet):
    """manage sales rep DataSubscription"""
    queryset = SalesRepDataSubscription.objects.order_by('id')
    # serializer_class = SalesRepDataSubscriptionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sub', 'sales_rep', 'create_date', 'is_closed',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SalesRepDataSubscriptionGetSerializer
        return SalesRepDataSubscriptionSerializer

    def update(self, request, pk=None):
        is_closed = is_closed_record(SalesRepDataSubscription, pk)

        if is_closed is not False:
            return is_closed

        return super(SalesRepDataSubscriptionViewSet, self).update(
            request, pk=pk)

    def partial_update(self, request, *args, **Kwargs):
        pk = Kwargs['pk']
        is_closed = is_closed_record(SalesRepDataSubscription, pk)

        if is_closed is not False:
            return is_closed

        # call update but with partial
        Kwargs['partial'] = True
        return super(SalesRepDataSubscriptionViewSet, self).update(
            request,  *args, **Kwargs)

    def destroy(self, request, pk=None):
        is_closed = is_closed_record(SalesRepDataSubscription, pk, 'delete')

        if is_closed is not False:
            return is_closed

        return super(SalesRepDataSubscriptionViewSet, self).destroy(
            request, pk=pk)


class AirtimeRecievedViewSet(viewsets.ModelViewSet):
    """manage sales rep DataSubscription"""
    queryset = AirtimeRecieved.objects.order_by('id')
    serializer_class = AirtimeRecievedSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sales_rep', 'amount', 'create_date', 'is_closed',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AirtimeRecievedGetSerializer
        return AirtimeRecieved

    def update(self, request, pk=None):
        is_closed = is_closed_record(AirtimeRecieved, pk)

        if is_closed is not False:
            return is_closed

        return super(AirtimeRecievedViewSet, self).update(request, pk=pk)

    def partial_update(self, request, *args, **Kwargs):
        pk = Kwargs['pk']
        is_closed = is_closed_record(AirtimeRecieved, pk)

        if is_closed is not False:
            return is_closed

        # call update but with partial
        Kwargs['partial'] = True
        return super(AirtimeRecievedViewSet, self).update(
            request,  *args, **Kwargs)

    def destroy(self, request, pk=None):
        is_closed = is_closed_record(AirtimeRecieved, pk, 'delete')

        if is_closed is not False:
            return is_closed

        return super(AirtimeRecievedViewSet, self).destroy(request, pk=pk)


class DataSalesViewSet(viewsets.ModelViewSet):
    """manage sales rep Data sales"""
    queryset = DataSales.objects.order_by('id')
    # serializer_class = DataSalesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'sales_rep', 'amount', 'create_date', 'is_closed', 'is_direct_sales',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DataSalesGetSerializer
        return DataSalesSerializer

    def update(self, request, pk=None):
        is_closed = is_closed_record(DataSales, pk)

        if is_closed is not False:
            return is_closed

        return super(DataSalesViewSet, self).update(request, pk=pk)

    def partial_update(self, request, *args, **Kwargs):
        pk = Kwargs['pk']
        is_closed = is_closed_record(DataSales, pk)

        if is_closed is not False:
            return is_closed

        # call update but with partial
        Kwargs['partial'] = True
        return super(DataSalesViewSet, self).update(
            request,  *args, **Kwargs)

    def destroy(self, request, pk=None):
        is_closed = is_closed_record(DataSales, pk, 'delete')

        if is_closed is not False:
            return is_closed

        return super(DataSalesViewSet, self).destroy(request, pk=pk)


class DataSalesSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset to read and create (no update or delete) data sales summary
    """
    queryset = DataSalesSummary.objects.order_by('-create_date')
    serializer_class = DataSalesSummarySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'id', 'sales_rep', 'Start_airtime', 'sales_date',
        'Start_data', 'total_airtime_recieved', 'total_direct_Sales',
        'total_sub_made', 'expected_airtime', 'actual_airtime',
        'expected_data_balance', 'no_order_treated', 'outstanding',
        'is_closed',)

    @action(methods=['post'], detail=False)
    def close_shift(self, request, pk=None):
        """
        Close sales for a particular shift and create a summary of the sales
        """

        sales_rep_id = request.data.get('sales_rep', None)
        actual_airtime = request.data.get('actual_airtime', None)
        actual_data_balance = request.data.get('actual_data_balance', None)
        no_order_treated = request.data.get('no_order_treated', None)
        sales_date = request.data.get('sales_date', now())
        create = request.data.get('create', False)

        if sales_rep_id is None or actual_airtime is None or actual_data_balance is None or no_order_treated is None:  # noqa
            return Response("Please specfic values for: sales rep,"
                            " actual_airtime, actual_data_balance "
                            "and no_order_treated",
                            status=status.HTTP_400_BAD_REQUEST)
        # get the sales rep and ensure that she is a data sales rep
        try:
            sales_rep = SalesRep.objects.get(pk=sales_rep_id)

            if sales_rep.category != SalesRep.DATA:
                return Response("Invalid Sales Rep, should be  a data sales rep",  # noqa
                                status=status.HTTP_400_BAD_REQUEST)
        except SalesRep.DoesNotExist:
            return Response("Sales rep does not exist.",
                            status=status.HTTP_400_BAD_REQUEST)

        start_data = sales_rep.data_balance
        start_airtime = sales_rep.airtime_balance

        # calculate total airime received; that airtime recieved that are not closed   # noqa
        total_airtime_recieved = sales_rep.airtime_received.filter(
            is_closed=False).aggregate(Sum('amount'))['amount__sum'] or 0

        sales = sales_rep.sales.filter(is_closed=False)
        total_direct_sales = 0
        total_data_shared = 0
        income = 0

        for s in sales:
            if s.is_direct_sales is True:
                total_direct_sales += s.cost
            total_data_shared += s.total_mb
            income += s.cost

        # calculate total subscription made
        total_sub = sales_rep.subscriptions.filter(
            is_closed=False).aggregate(Sum('amount'))['amount__sum'] or 0

        total_airtime_used = 0
        total_mb_added = 0

        product = sales_rep.sales.last().data_plan.network

        # get total airtime used for subscription and data gained
        # if total_sub > 0:
        # the assumption is that a sales rep would hold only one product per shift  # noqa
        data_sub = product.datasubscription
        total_airtime_used = total_sub * data_sub.cost_per_sub
        total_mb_added = total_sub * data_sub.mb_per_sub

        expected_airtime = start_airtime + total_airtime_recieved - total_airtime_used  # noqa
        outstanding = actual_airtime - expected_airtime - total_direct_sales

        expected_data_balance = start_data + total_mb_added - total_data_shared
        outstanding_data_balance = actual_data_balance - expected_data_balance

        outstanding_data_cash = (data_sub.cost_per_sub * outstanding_data_balance) / data_sub.mb_per_sub  # noqa
        outstanding += outstanding_data_cash

        expenditure = (data_sub.cost_per_sub * total_data_shared) / data_sub.mb_per_sub   # noqa

        profit = income - expenditure

        if sales.count != 0:
            Profit.objects.create(amount=profit, product=product)

        summary = {
            'sales_date': sales_date,
            'sales_rep_id': sales_rep_id,
            'Start_airtime': start_airtime,
            'Start_data': start_data,
            'total_airtime_recieved': total_airtime_recieved,
            'total_direct_Sales': total_direct_sales,
            'total_sub_made': total_sub,
            'expected_airtime': expected_airtime,
            'actual_airtime': actual_airtime,
            'expected_data_balance': expected_data_balance,
            'actual_data_balance': actual_data_balance,
            'total_data_shared': total_data_shared,
            'no_order_treated': no_order_treated,
            'outstanding': outstanding,
            'is_closed': True
        }

        if create is False:
            return Response(summary)

        # close shift records
        with transaction.atomic():
            # close records
            sales_rep.airtime_balance = expected_airtime
            sales_rep.data_balance = expected_data_balance
            sales_rep.save()
            sales_rep.airtime_received.filter(is_closed=False).update(is_closed=True)  # noqa
            sales_rep.sales.filter(is_closed=False).update(is_closed=True)
            sales_rep.subscriptions.filter(is_closed=False).update(is_closed=True)  # noqa
            # TODO: create profit
            sales_summary = DataSalesSummary.objects.create(**summary)

            data = self.get_serializer_class()(sales_summary).data
            return Response(data, status=status.HTTP_201_CREATED)


class CashRecievedViewSet(viewsets.ModelViewSet):
    """manage sales rep DataSubscription"""
    queryset = CashRecieved.objects.order_by('id')
    serializer_class = CashRecievedSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sales_rep', 'amount', 'create_date', 'is_closed',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CashRecievedGetSerializer
        return CashRecievedSerializer

    def update(self, request, pk=None):
        is_closed = is_closed_record(CashRecieved, pk)

        if is_closed is not False:
            return is_closed

        return super(AirtimeRecievedViewSet, self).update(request, pk=pk)

    def partial_update(self, request, *args, **Kwargs):
        pk = Kwargs['pk']
        is_closed = is_closed_record(CashRecieved, pk)

        if is_closed is not False:
            return is_closed

        # call update but with partial
        Kwargs['partial'] = True
        return super(AirtimeRecievedViewSet, self).update(
            request,  *args, **Kwargs)

    def destroy(self, request, pk=None):
        is_closed = is_closed_record(CashRecieved, pk, 'delete')

        if is_closed is not False:
            return is_closed

        return super(AirtimeRecievedViewSet, self).destroy(request, pk=pk)


class TradeViewSet(viewsets.ModelViewSet):
    """manage sales rep giftcard sales"""
    queryset = Trade.objects.order_by('id')
    # serializer_class = TradeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'sales_rep', 'amount', 'create_date', 'is_closed', 'group', 'card',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TradeGetSerializer
        return TradeSerializer

    def update(self, request, pk=None):
        is_closed = is_closed_record(Trade, pk)

        if is_closed is not False:
            return is_closed

        return super(TradeViewSet, self).update(request, pk=pk)

    def partial_update(self, request, *args, **Kwargs):
        pk = Kwargs['pk']
        is_closed = is_closed_record(Trade, pk)

        if is_closed is not False:
            return is_closed

        # call update but with partial
        Kwargs['partial'] = True
        return super(TradeViewSet, self).update(
            request,  *args, **Kwargs)

    def destroy(self, request, pk=None):
        is_closed = is_closed_record(Trade, pk, 'delete')

        if is_closed is not False:
            return is_closed

        return super(TradeViewSet, self).destroy(request, pk=pk)


class TradeSummaryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset to read and create (no update or delete) data sales summary
    """
    queryset = TradeSummary.objects.order_by('-create_date')
    serializer_class = TradeSummarySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'id', 'total_cash_recieved', 'is_closed', 'total_cash_used',
        'sales_rep', 'balance',)

    @action(methods=['post'], detail=False)
    def close_shift(self, request, pk=None):
        """
        Close sales for a particular shift and create a summary of the sales
        """

        sales_rep_id = request.data.get('sales_rep', None)
        create = request.data.get('create', False)

        if sales_rep_id is None:
            return Response("Please specfic value for sales rep",
                            status=status.HTTP_400_BAD_REQUEST)
        # get the sales rep and ensure that he is a giftcard sales rep
        try:
            sales_rep = SalesRep.objects.get(pk=sales_rep_id)

            if sales_rep.category != SalesRep.GIFTCARD:
                return Response("Invalid Sales Rep, should be  a data sales rep",  # noqa
                                status=status.HTTP_400_BAD_REQUEST)
        except SalesRep.DoesNotExist:
            return Response("Sales rep does not exist.",
                            status=status.HTTP_400_BAD_REQUEST)

        Yuan_to_naira = 0
        # calculate profit
        try:
            Yuan_to_naira = Configuration.objects.get(key='Yuan_to_naira')
        except Configuration.DoesNotExist:
            return Response('Please add a value for config \'Yuan_to_naira\'')

        start_cash = sales_rep.cash_balance

        total_cash_recieved = sales_rep.cash_received.filter(
            is_closed=False).aggregate(Sum('amount'))['amount__sum'] or 0

        trades = sales_rep.trades.filter(is_closed=False)
        total_cash_used = 0
        income = 0

        for trade in trades:
            total_cash_used += trade.amount_paid
            income += trade.buying_rate * trade.amount

        balance = start_cash + total_cash_recieved - total_cash_used

        # create profit
        income *= int(Yuan_to_naira.value)
        profit = income - total_cash_used

        if trades.first() is not None:
            Profit.objects.create(amount=profit, product=trades.first().card)

        summary = {
            'sales_rep_id': sales_rep_id,
            'total_cash_recieved': total_cash_recieved,
            'total_cash_used': total_cash_used,
            'balance': balance,
            'is_closed': True
        }

        if create is False:
            return Response(summary)

        # close shift records
        with transaction.atomic():
            # close records
            sales_rep.cash_balance = balance
            sales_rep.save()
            sales_rep.cash_received.filter(is_closed=False).update(is_closed=True)  # noqa
            sales_rep.trades.filter(is_closed=False).update(is_closed=True)
            # TODO: create profit
            trade_summary = TradeSummary.objects.create(**summary)

            data = self.get_serializer_class()(trade_summary).data
            return Response(data, status=status.HTTP_201_CREATED)


class ProfitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    readonly Viewset to read profit
    """
    queryset = Profit.objects.order_by('-sales_date')
    serializer_class = ProfitSerializer
    permission_classes = (IsAdminOnlyPermission,)
    filter_class = ProfitFilter

    def list(self, request):
        params = request.query_params
        sales_date = params.get('sales_date__date', None)
        sales_to_date = params.get('sales_date__date__lt', None)
        sales_from_date = params.get('sales_date__date__gt', None)

        if not sales_date and not (sales_from_date and sales_to_date):
            return super(ProfitViewSet, self).list(request)

        qs = self.filter_queryset(self.get_queryset())
        if sales_to_date is not None and sales_from_date is not None:
            sales_from_date = datetime.strptime(sales_from_date, "%Y-%m-%d")
            sales_to_date = datetime.strptime(sales_to_date, "%Y-%m-%d")
            interval_in_days = (sales_to_date-sales_from_date).days
            date_aggregate = ''

            if interval_in_days < 1:
                return Response('start date can not be ahead of end date',
                                status=status.HTTP_400_BAD_REQUEST)

            if interval_in_days <= 30:
                # get aggregate by day
                date_aggregate = 'sales_date__day'
            elif interval_in_days <= (7 * 20):
                # get aggregate by week
                date_aggregate = 'sales_date__week'
            elif interval_in_days <= 365:
                # get aggregate by month
                date_aggregate = 'sales_date__month'
            else:
                # get aggregate by year
                date_aggregate = 'sales_date__year'

            profits = qs.values(
                    'product', date_aggregate).order_by(
                        date_aggregate).annotate(total=Sum('amount'))
        elif sales_date is not None:
            profits = qs.values(
                    'product', 'sales_date').order_by(
                        'product').annotate(total=Sum('amount'))

        return Response(list(profits))
