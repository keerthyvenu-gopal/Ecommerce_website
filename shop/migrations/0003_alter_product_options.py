# Generated by Django 3.2 on 2021-12-08 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
