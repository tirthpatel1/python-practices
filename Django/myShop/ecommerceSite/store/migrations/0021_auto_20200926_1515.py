# Generated by Django 3.1.1 on 2020-09-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20200926_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]