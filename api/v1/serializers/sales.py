from rest_framework import serializers

from sales.models import (
    Configuration,
    SalesRep
)


class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration
        fields = '__all__'


class SalesRepSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesRep
        fields = '__all__'
