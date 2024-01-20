from django import forms
from .models import Supplier, Product


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'type', 'email', 'country', 'city',
                  'street', 'house_number', 'products', 'supplier', ]

    def clean(self):
        cleaned_data = super().clean()
        type = cleaned_data.get('type')
        supplier = cleaned_data.get('supplier')

        if type == 'factory' and supplier:
            raise forms.ValidationError(
                "Для типа 'Завод' не указывайте поставщика.")
        elif type != 'factory' and not supplier:
            raise forms.ValidationError(
                "Укажите поставщика.")


class ProductForm(forms.ModelForm):
    release_date = forms.DateTimeField(widget=forms.widgets.DateInput(
        attrs={'type': 'datetime-local'}))

    class Meta:
        model = Product
        fields = ['name', 'model', 'release_date']
