from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import SimpleSearchForm, ProductForm
from webapp.models import Product


class ProductList(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    ordering = ('product_title', 'category')
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = self.model.objects.filter(residual__gt=0)
        if self.search_value:
            queryset = queryset.filter(
                Q(product_title__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class ProductDetail(DetailView):

    template_name = 'product/product_view.html'
    context_key = 'product'
    model = Product


class ProductCreate(CreateView):

    template_name = 'product/create.html'
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        self.project = form.save()
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):

    template_name = 'product/delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('index')
