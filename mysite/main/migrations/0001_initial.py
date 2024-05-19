# Generated by Django 5.0.6 on 2024-05-15 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('img', models.ImageField(upload_to='home_imaes', verbose_name='product image')),
                ('about', models.TextField(verbose_name='Product about')),
                ('slug', models.SlugField(unique=True, verbose_name='Product slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_prod', to='main.category')),
            ],
        ),
    ]