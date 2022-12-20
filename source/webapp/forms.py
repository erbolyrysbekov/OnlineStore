from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_title', 'description', 'category', 'residual', 'price']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['product_title'] == cleaned_data['description']:
            raise ValidationError('Поля наименование продукта и описание не должны повторяться!')
        return cleaned_data


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=40, required=False, label='Найти')
