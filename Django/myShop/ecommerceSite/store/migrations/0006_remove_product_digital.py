# Generated by Django 3.1.1 on 2020-09-20 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
