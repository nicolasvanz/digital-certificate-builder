# Generated by Django 3.0 on 2020-03-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200314_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateautority',
            name='public_key',
            field=models.CharField(default='', max_length=999999),
        ),
        migrations.AlterField(
            model_name='certificateautority',
            name='private_key',
            field=models.CharField(default='', max_length=999999),
        ),
    ]