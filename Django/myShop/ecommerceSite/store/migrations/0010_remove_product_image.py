# Generated by Django 3.1.1 on 2020-09-23 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
