from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import \
    LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .forms import SupplierForm, ProductForm
from .models import Supplier
from django.views.generic import \
    ListView, DetailView, View, CreateView, DeleteView, UpdateView


# Create your views here.
class HomeView(ListView):
    model = Supplier
    template_name = 'ElectronicsNetwork/supplier_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = Supplier.objects.all()
        return context


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'ElectronicsNetwork/supplier_info.html'
    context_object_name = 'supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplierCreateView(LoginRequiredMixin,
                         PermissionRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'ElectronicsNetwork/supplier_create.html'
    permission_required = 'ElectronicsNetwork.add_supplier'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ElectronicsNetwork:supplier_info',
                       kwargs={'pk': self.object.pk})


class SupplierUpdateView(LoginRequiredMixin,
                         PermissionRequiredMixin,
                         UpdateView):
    model = Supplier
    permission_required = 'ElectronicsNetwork.change_supplier'
    form_class = SupplierForm
    template_name = 'ElectronicsNetwork/supplier_create.html'
    success_url = reverse_lazy('ElectronicsNetwork:suppliers')


class SupplierDeleteView(LoginRequiredMixin,
                         PermissionRequiredMixin,
                         DeleteView):
    model = Supplier
    template_name = 'ElectronicsNetwork/supplier_delete.html'
    permission_required = 'ElectronicsNetwork.delete_supplier'
    success_url = reverse_lazy('ElectronicsNetwork:suppliers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductCreateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        CreateView):
    model = Supplier
    form_class = ProductForm
    template_name = 'ElectronicsNetwork/product_create.html'
    permission_required = 'ElectronicsNetwork.add_product'

    def get_success_url(self):
        return reverse('ElectronicsNetwork:supplier_create')


class ClearDebtView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        supplier = get_object_or_404(Supplier, pk=kwargs['pk'])
        supplier.debt_to_supplier = 0
        supplier.save()
        return redirect('ElectronicsNetwork:supplier_info', pk=supplier.pk)
