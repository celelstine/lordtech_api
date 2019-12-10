from rest_framework import serializers

from sales.models import (
    AirtimeRecieved,
    CashRecieved,
    Configuration,
    DataPlan,
    DataSales,
    DataSalesSummary,
    DataSubscription,
    Product,
    SalesRep,
    SalesRepDataSubscription,
    Trade
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


class DataSalesSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSalesSummary
        fields = '__all__'


class CashRecievedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashRecieved
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = '__all__'
