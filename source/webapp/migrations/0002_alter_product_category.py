# Generated by Django 4.1.3 on 2022-11-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Разное'), ('vegetables', 'Овощи'), ('fruits', 'Фрукты'), ('drinks', 'Напитки')], default='Разное', max_length=40, verbose_name='Категория'),
        ),
    ]