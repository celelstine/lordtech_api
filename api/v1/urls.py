from rest_framework.routers import DefaultRouter

from api.v1.views import (
    AirtimeReceivedViewSet,
    # block_io_webhook,
    CashReceivedViewSet,
    ConfigurationViewSet,
    DataPlanViewSet,
    DataSalesViewSet,
    DataSalesSummaryViewSet,
    DataSubscriptionViewSet,
    ProductViewSet,
    ProfitViewSet,
    SalesRepViewSet,
    SalesRepDataSubscriptionViewSet,
    UserViewSet,
    TradeViewSet,
    TradeGroupViewSet,
    TradeSummaryViewSet
)

router = DefaultRouter()

router.register(
    r'airtime-received', AirtimeReceivedViewSet, base_name='airtime-received')
router.register(r'salesrep', SalesRepViewSet, base_name='salesrep')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'config', ConfigurationViewSet, base_name='config')
router.register(r'dataplan', DataPlanViewSet, base_name='dataplan')
router.register(r'datasales', DataSalesViewSet, base_name='datasales')
router.register(
    r'datasales-summary', DataSalesSummaryViewSet,
    base_name='datasales-summary')
router.register(r'sub', DataSubscriptionViewSet, base_name='sub')
router.register(
    r'salesrep-sub', SalesRepDataSubscriptionViewSet, base_name='salesrep-sub')
router.register(r'product', ProductViewSet, base_name='product')
router.register(
    r'cash-received', CashReceivedViewSet, base_name='cash-received')
router.register(r'trade', TradeViewSet, base_name='trade')
router.register(
    r'trade-summary', TradeSummaryViewSet, base_name='trade-summary')
router.register(r'profit', ProfitViewSet, base_name='profit')
router.register(r'trade-group', TradeGroupViewSet, base_name='trade-group')


urlpatterns = [
    # path(r'webhook/block-io/', block_io_webhook, name='block-io-webhook'),
]

urlpatterns += router.urls
