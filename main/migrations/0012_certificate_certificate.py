# Generated by Django 3.0 on 2020-03-14 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_certificate_self_signed'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='certificate',
            field=models.CharField(default='', max_length=999999),
        ),
    ]
