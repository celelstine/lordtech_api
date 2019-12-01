from django.contrib import admin

from .models import (
    Configuration,
    DataPlan,
    DataSubscription,
    Product,
    SalesRep
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
