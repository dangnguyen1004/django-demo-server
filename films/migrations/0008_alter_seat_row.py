# Generated by Django 3.2.6 on 2021-08-14 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_actor_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='row',
            field=models.CharField(max_length=255),
        ),
    ]
