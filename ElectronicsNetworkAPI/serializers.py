from ElectronicsNetwork.models import Supplier
from rest_framework import serializers


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        read_only_fields = ('debt_to_supplier', 'creation_time')
        fields = '__all__'
