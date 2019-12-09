from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.v1.serializers import (
    AirtimeRecievedSerializer,
    ConfigurationSerializer,
    DataPlanSerializer,
    DataSalesSerializer,
    DataSubscriptionSerializer,
    ProductSerializer,
    SalesRepSerializer,
    SalesRepDataSubscriptionSerializer,
)

from sales.models import (
    AirtimeRecieved,
    Configuration,
    DataPlan,
    DataSales,
    DataSubscription,
    Product,
    SalesRep,
    SalesRepDataSubscription
)


class ConfigurationViewSet(viewsets.ModelViewSet):
    """Manage configurations"""
    queryset = Configuration.objects.filter(is_active=True).order_by('id')
    serializer_class = ConfigurationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category', 'key')

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
    filter_fields = ('name', 'category')

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
    filter_fields = ('name', 'category')

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
    serializer_class = DataSubscriptionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('network',)


class DataPlanViewSet(viewsets.ModelViewSet):
    """manage Dataplan"""
    queryset = DataPlan.objects.filter(is_active=True).order_by('id')
    serializer_class = DataPlanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('network', 'name')


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
    serializer_class = SalesRepDataSubscriptionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sub', 'sales_rep', 'create_date', 'is_closed')

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
    filter_fields = ('sales_rep', 'amount', 'create_date', 'is_closed')

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
    serializer_class = DataSalesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'sales_rep', 'amount', 'create_date', 'is_closed', 'is_direct_sales')

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