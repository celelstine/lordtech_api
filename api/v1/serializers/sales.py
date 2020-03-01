from rest_framework import serializers

from sales.models import (
    AirtimeReceived,
    CashReceived,
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
    TradeGroup,
    TradeSummary
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


class DataSubscriptionGetSerializer(DataSubscriptionSerializer):

    class Meta(DataSubscriptionSerializer.Meta):
        depth = 1


class DataPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataPlan
        fields = '__all__'


class DataPlanGetSerializer(serializers.ModelSerializer):

    class Meta(DataPlanSerializer.Meta):
        depth = 1


class SalesRepDataSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SalesRepDataSubscription
        fields = '__all__'


class SalesRepDataSubscriptionGetSerializer(serializers.ModelSerializer):

    class Meta(SalesRepDataSubscriptionSerializer.Meta):
        depth = 2


class AirtimeReceivedSerializer(serializers.ModelSerializer):

    class Meta:
        model = AirtimeReceived
        fields = '__all__'


class AirtimeReceivedGetSerializer(serializers.ModelSerializer):

    class Meta(AirtimeReceivedSerializer.Meta):
        depth = 1


class DataSalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSales
        fields = '__all__'


class DataSalesGetSerializer(DataSubscriptionSerializer):

    class Meta(DataSalesSerializer.Meta):
        depth = 2


class DataSalesSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSalesSummary
        fields = '__all__'
        depth = 1


class CashReceivedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CashReceived
        fields = '__all__'


class CashReceivedGetSerializer(CashReceivedSerializer):

    class Meta(CashReceivedSerializer.Meta):
        depth = 1


class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trade
        fields = '__all__'


class TradeGetSerializer(TradeSerializer):

    class Meta(TradeSerializer.Meta):
        depth = 1


class TradeSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = TradeSummary
        fields = '__all__'
        depth = 1


class ProfitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profit
        fields = '__all__'
        depth = 1


class TradeGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradeGroup
        fields = '__all__'