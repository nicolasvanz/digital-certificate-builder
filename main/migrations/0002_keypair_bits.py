# Generated by Django 3.0 on 2020-03-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='keypair',
            name='bits',
            field=models.IntegerField(default=0),
        ),
    ]
