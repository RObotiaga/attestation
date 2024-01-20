from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'country',
                    'supplier_url', 'debt_to_supplier')
    list_filter = ('country', 'type', 'city',)
    search_fields = ('country', 'name', 'supplier',
                     'creation_time', 'street',)
    actions = ['reset_debt']

    @admin.action(description="Обнулить задолженность")
    def reset_debt(self, request, queryset):
        queryset.update(debt_to_supplier=0)

    def supplier_url(self, obj):
        if obj.supplier:
            url = reverse('admin:ElectronicsNetwork_supplier_change',
                          args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier)
        else:
            return "N/A"

    supplier_url.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    list_filter = ('name', 'model', 'release_date')
    search_fields = ('name', 'model', 'release_date')
