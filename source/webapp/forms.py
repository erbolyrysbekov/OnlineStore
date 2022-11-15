from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    product_title = forms.CharField(max_length=60, required=True, label='Наименование продукта')
    description = forms.CharField(max_length=2000, required=False, label='Описание', widget=widgets.Textarea)
    category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES, initial=CATEGORY_CHOICES[0][1], label='Категория')
    residual = forms.CharField(max_length=60, required=True, label='Остаток')
    email = forms.CharField(max_length=60, required=True, label='Цена')

