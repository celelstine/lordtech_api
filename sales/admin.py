from django.contrib import admin

from .models import (
    AirtimeRecieved,
    Configuration,
    DataPlan,
    DataSubscription,
    Product,
    SalesRep,
    SalesRepDataSubscription,
)


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    fields = ('id', 'key', 'value', 'category', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('create_date', 'modify_date')
    search_fields = ['key', 'id']


@admin.register(DataSubscription)
class DataSubscriptionAdmin(admin.ModelAdmin):
    fields = (
        'id', 'network', 'mb_per_sub', 'cost_per_sub',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('create_date', 'modify_date')
    search_fields = ['network', 'id']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'category', 'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('create_date', 'modify_date')
    search_fields = ['name', 'id']


@admin.register(SalesRep)
class SalesRepAdmin(admin.ModelAdmin):
    fields = (
        'id', 'name', 'category', 'cash_balance', 'airtime_balance',
        'create_date', 'modify_date')
    list_display = fields
    readonly_fields = ('create_date', 'modify_date')
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
