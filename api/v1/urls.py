from rest_framework.routers import DefaultRouter

from api.v1.views import (
    UserViewSet,
    ConfigurationViewSet
)

router = DefaultRouter()

router.register(r'user', UserViewSet, base_name='user')
router.register(r'config', ConfigurationViewSet, base_name='config')
urlpatterns = router.urls
