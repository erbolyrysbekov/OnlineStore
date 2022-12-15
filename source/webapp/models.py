from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = [("other", "Разное"), ("vegetables", "Овощи"), ("fruits", "Фрукты"), ("drinks", "Напитки")]


# Create your models here.

class Product(models.Model):
    product_title = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][1],
                                verbose_name="Категория")
    residual = models.PositiveIntegerField(verbose_name="Остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")

    def get_absolute_url(self):
        return reverse('product_view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.id}) {self.product_title}'


class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.CharField(max_length=50, default='Unknown', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='comments',
                                verbose_name='Статья')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.pk}. {self.text[:20]}'
