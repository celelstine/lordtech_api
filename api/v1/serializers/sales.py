from rest_framework import serializers

from sales.models import (
    AirtimeRecieved,
    Configuration,
    DataPlan,
    DataSales,
    DataSubscription,
    Product,
    SalesRep,
    SalesRepDataSubscription,
)


class ConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Configuration
        fields = '__all__'


class SalesRepSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesRep
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class DataSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSubscription
        fields = '__all__'


class DataPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataPlan
        fields = '__all__'


class SalesRepDataSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesRepDataSubscription
        fields = '__all__'


class AirtimeRecievedSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirtimeRecieved
        fields = '__all__'


class DataSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSales
        fields = '__all__'
