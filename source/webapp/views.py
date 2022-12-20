from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product
from webapp.forms import ProductForm
from django.views.generic import View, TemplateView




class IndexView(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.exclude(residual=0).order_by('product_title', 'category')
        return render(request, 'product/index.html', {'products': products})


class ProductView(TemplateView):
    template_name = 'product/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, pk=kwargs.get('pk'))
        return context


def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product/create.html', {'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)

        if form.is_valid():
            new_product = Product.objects.create(
                product_title=form.cleaned_data['product_title'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                residual=form.cleaned_data['residual'],
                price=form.cleaned_data['price'],
            )
            return redirect('index')
        else:
            return render(request, 'product/create.html', {'form': form})


def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'product_title': product.product_title,
            'description': product.description,
            'category': product.category,
            'residual': product.residual,
            'price': product.price,
        })
        return render(request, 'product/update.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product_title = form.cleaned_data['product_title']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.residual = form.cleaned_data['residual']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
        else:
            return render(request, 'product/update.html', context={'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'product/delete.html', {'product': product})
    elif request.method == "POST":
        product.delete()
        return redirect('index')
