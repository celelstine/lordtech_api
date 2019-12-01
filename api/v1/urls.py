from rest_framework.routers import DefaultRouter

from api.v1.views import (
    ConfigurationViewSet,
    ProductViewSet,
    SalesRepViewSet,
    UserViewSet,
)

router = DefaultRouter()

router.register(r'salesrep', SalesRepViewSet, base_name='salesrep')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'config', ConfigurationViewSet, base_name='config')
router.register(r'product', ProductViewSet, base_name='product')
urlpatterns = router.urls
