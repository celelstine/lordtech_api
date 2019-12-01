from rest_framework import viewsets
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


class SalesRepViewSet(viewsets.ModelViewSet):
    """You can handle every authentication and user management on your account """ # noqa
    queryset = SalesRep.objects.filter(is_active=True)
    serializer_class = SalesRepSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'category')
