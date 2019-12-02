from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.v1.serializers import (
    ConfigurationSerializer,
    DataPlanSerializer,
    DataSubscriptionSerializer,
    ProductSerializer,
    SalesRepSerializer,
    SalesRepDataSubscriptionSerializer,
)

from sales.models import (
    Configuration,
    DataPlan,
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


class SalesRepDataSubscriptionViewSet(viewsets.ModelViewSet):
    """manage sales rep DataSubscription"""
    queryset = SalesRepDataSubscription.objects.filter(
        is_active=True).order_by('id')
    serializer_class = SalesRepDataSubscriptionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('sub', 'sales_rep', 'create_date')
