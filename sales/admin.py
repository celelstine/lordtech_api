from django.contrib import admin

from .models import (
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


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    fields = ('id', 'key', 'value', 'category', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['key', 'id']


@admin.register(DataSubscription)
class DataSubscriptionAdmin(admin.ModelAdmin):
    fields = (
        'id', 'network', 'mb_per_sub', 'cost_per_sub',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['network', 'id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'category', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['name', 'id']


@admin.register(SalesRep)
class SalesRepAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'category', 'cash_balance', 'airtime_balance',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['name', 'id']


@admin.register(DataPlan)
class DataPlanAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'network', 'mb', 'cost',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['name', 'id']


@admin.register(SalesRepDataSubscription)
class SalesRepDataSubscriptionAdmin(admin.ModelAdmin):
    fields = (
        'id', 'sub', 'sales_rep', 'amount', 'cost', 'is_closed',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['id', 'is_closed']

    def get_queryset(self, request):
        return super(SalesRepDataSubscriptionAdmin, self).get_queryset(
            request).order_by('-create_date')


@admin.register(AirtimeRecieved)
class AirtimeRecievedAdmin(admin.ModelAdmin):
    fields = (
        'id', 'sales_rep', 'amount', 'is_closed',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['id', 'amount', 'is_closed']

    def get_queryset(self, request):
        return super(AirtimeRecievedAdmin, self).get_queryset(
            request).order_by('-create_date')


@admin.register(DataSales)
class DataSalesAdmin(admin.ModelAdmin):
    fields = (
        'id', 'data_plan', 'sales_rep', 'amount', 'cost', 'total_mb',
        'is_direct_sales', 'is_closed', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date', 'cost', 'total_mb')
    search_fields = ['id', 'amount', 'is_closed', 'cost']

    def get_queryset(self, request):
        return super(DataSalesAdmin, self).get_queryset(
            request).order_by('-create_date')


@admin.register(DataSalesSummary)
class DataSalesSummaryAdmin(admin.ModelAdmin):
    fields = (
        'id', 'sales_date', 'sales_rep', 'Start_airtime', 'Start_data',
        'total_airtime_recieved', 'total_direct_Sales', 'total_sub_made',
        'expected_airtime', 'actual_airtime', 'expected_data_balance',
        'actual_data_balance', 'total_data_shared', 'no_order_treated',
        'outstanding', 'is_closed', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = fields
    search_fields = [
        'id', 'sales_date', 'is_closed', 'outstanding', 'no_order_treated']

    def get_queryset(self, request):
        return super(DataSalesSummaryAdmin, self).get_queryset(
            request).order_by('-sales_date')


@admin.register(CashRecieved)
class CashRecievedAdmin(admin.ModelAdmin):
    fields = (
        'id', 'sales_rep', 'amount', 'is_closed',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['id', 'amount', 'is_closed']

    def get_queryset(self, request):
        return super(CashRecievedAdmin, self).get_queryset(
            request).order_by('-create_date')


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    fields = (
        'id', 'sales_rep', 'card', 'group', 'selling_rate', 'buying_rate',
        'amount', 'amount_paid', 'is_closed', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = ['id', 'amount', 'is_closed']

    def get_queryset(self, request):
        return super(TradeAdmin, self).get_queryset(
            request).order_by('-create_date')


@admin.register(TradeSummary)
class TradeSummaryAdmin(admin.ModelAdmin):
    fields = (
        'id', 'sales_rep', 'total_cash_recieved', 'total_cash_used',
        'balance',  'is_closed', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('id', 'create_date', 'modify_date')
    search_fields = [
        'id', 'sales_rep', 'total_cash_recieved', 'total_cash_used',
         'balance', 'is_closed', 'create_date']

    def get_queryset(self, request):
        return super(TradeSummaryAdmin, self).get_queryset(
            request).order_by('-create_date')


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    fields = (
        'id', 'product', 'amount','sales_date', 'create_date', 'modify_date', )
    list_display = fields
    readonly_fields = fields
    search_fields = ['id', 'product', 'amount']

    def get_queryset(self, request):
        return super(ProfitAdmin, self).get_queryset(
            request).order_by('-create_date')
