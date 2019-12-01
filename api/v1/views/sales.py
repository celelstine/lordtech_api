from rest_framework import viewsets
from django_filters import rest_framework as filters

from api.v1.serializers import (
    ConfigurationSerializer
)

from sales.models import (
    Configuration
)


class ConfigurationViewSet(viewsets.ModelViewSet):
    """You can handle every authentication and user management on your account """ # noqa
    queryset = Configuration.objects.filter(is_active=True)
    serializer_class = ConfigurationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('category', 'key')
