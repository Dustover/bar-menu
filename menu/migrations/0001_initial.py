# Generated by Django 3.2.25 on 2024-04-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category', models.CharField(max_length=50, verbose_name='Категория')),
                ('item_name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('item_ingredients', models.TextField(blank=True, max_length=500, verbose_name='Ингридиенты')),
                ('item_mass', models.CharField(blank=True, max_length=50, verbose_name='Масса/объём')),
                ('item_price', models.IntegerField(verbose_name='Цена')),
                ('item_in_stock', models.BooleanField(verbose_name='В наличии')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
