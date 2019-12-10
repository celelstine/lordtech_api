from rest_framework.routers import DefaultRouter

from api.v1.views import (
    AirtimeRecievedViewSet,
    CashRecievedViewSet,
    ConfigurationViewSet,
    DataPlanViewSet,
    DataSalesViewSet,
    DataSalesSummaryViewSet,
    DataSubscriptionViewSet,
    ProductViewSet,
    SalesRepViewSet,
    SalesRepDataSubscriptionViewSet,
    UserViewSet,
    TradeViewSet,
    TradeSummaryViewSet
)

router = DefaultRouter()

router.register(r'airtime-recieved', AirtimeRecievedViewSet, base_name='airtime-recieved')  # noqa
router.register(r'salesrep', SalesRepViewSet, base_name='salesrep')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'config', ConfigurationViewSet, base_name='config')
router.register(r'dataplan', DataPlanViewSet, base_name='dataplan')
router.register(r'datasales', DataSalesViewSet, base_name='datasales')
router.register(r'datasales-summary', DataSalesSummaryViewSet, base_name='datasales-summary')  # noqa
router.register(r'sub', DataSubscriptionViewSet, base_name='sub')
router.register(r'salesrep-sub', SalesRepDataSubscriptionViewSet, base_name='salesrep-sub')  # noqa
router.register(r'product', ProductViewSet, base_name='product')
router.register(r'cash-recieved', CashRecievedViewSet, base_name='cash-recieved')  # noqa
router.register(r'trade', TradeViewSet, base_name='trade')  # noqa
router.register(r'trade-summary', TradeSummaryViewSet, base_name='trade-summary')  # noqa

urlpatterns = router.urls
