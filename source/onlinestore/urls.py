"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import ProductList, ProductDetail, ProductUpdate, ProductCreate, ProductDelete,\
    AddCartItem, CartList, CartDelete, OrderCreate, CartDeleteOne

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductList.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_view'),
    path('product/<int:pk>/add_to_cart/', AddCartItem.as_view(), name='add_to_cart'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
    path('cart/', CartList.as_view(), name='cart_index'),
    path('cart/<int:pk>/delete/', CartDelete.as_view(), name='cart_delete'),
    path('order/', OrderCreate.as_view(), name='order_create'),
    path('cart/<int:pk>/delete_one/', CartDeleteOne.as_view(), name='cart_delete_one'),

]
