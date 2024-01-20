from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .permissions import IsActive
from ElectronicsNetwork.models import Supplier
from ElectronicsNetworkAPI.serializers import SupplierSerializer


# Create your views here.
class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', ]
