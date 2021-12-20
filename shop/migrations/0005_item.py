# Generated by Django 3.2 on 2021-12-08 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_cartlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quan', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cartlist')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]
