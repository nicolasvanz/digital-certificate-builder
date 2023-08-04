# Generated by Django 3.0 on 2020-03-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_keypair_ident'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_key', models.CharField(max_length=999999)),
                ('public_key', models.CharField(max_length=999999)),
                ('bits', models.IntegerField(default=0)),
                ('subject', models.CharField(max_length=999999)),
                ('serial_number', models.CharField(max_length=999999)),
                ('issuer', models.CharField(max_length=999999)),
            ],
        ),
        migrations.AddField(
            model_name='keypair',
            name='used',
            field=models.IntegerField(default=-1),
        ),
    ]