# Generated by Django 3.2.6 on 2021-08-13 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_auto_20210813_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='show',
        ),
        migrations.AddField(
            model_name='ticket',
            name='show',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='films.show'),
            preserve_default=False,
        ),
    ]
