from django.urls import path
from .views import HomeView, SupplierDetailView, \
    SupplierCreateView, SupplierDeleteView, ClearDebtView, \
    SupplierUpdateView, ProductCreateView

app_name = 'ElectronicsNetwork'
urlpatterns = [
    path('suppliers/', HomeView.as_view(),
         name='suppliers'),
    path('supplier/<int:pk>/', SupplierDetailView.as_view(),
         name='supplier_info'),
    path('supplier/create/', SupplierCreateView.as_view(),
         name='supplier_create'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(),
         name='supplier_delete'),
    path('supplier/<int:pk>/edit/', SupplierUpdateView.as_view(),
         name='supplier_edit'),
    path('supplier/<int:pk>/clear-debt/', ClearDebtView.as_view(),
         name='clear_debt'),
    path('product/create/', ProductCreateView.as_view(),
         name='product_create')
]
