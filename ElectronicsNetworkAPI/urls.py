from .apps import ElectronicsnetworkapiConfig
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet

app_name = ElectronicsnetworkapiConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
urlpatterns = [] + router.urls
