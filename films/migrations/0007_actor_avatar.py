# Generated by Django 3.2.6 on 2021-08-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='avatar',
            field=models.CharField(default='https://picsum.photos/100/100', max_length=255),
            preserve_default=False,
        ),
    ]
