from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django_filters import rest_framework as filters

from api.v1.serializers import (
    SalesRepSerializer,
    ConfigurationSerializer
)

from sales.models import (
    SalesRep,
    Configuration
)


class ConfigurationViewSet(viewsets.ModelViewSet):
    """You can handle every authentication and user management on your account """ # noqa
    queryset = Configuration.objects.filter(is_active=True)
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
    """You can handle every authentication and user management on your account """ # noqa
    queryset = SalesRep.objects.filter(is_active=True)
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
