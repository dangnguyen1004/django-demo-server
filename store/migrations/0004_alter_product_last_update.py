# Generated by Django 3.2.6 on 2021-08-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]