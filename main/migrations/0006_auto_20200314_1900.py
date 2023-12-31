# Generated by Django 3.0 on 2020-03-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200313_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateAutority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privete_key', models.CharField(max_length=999999)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='certificate',
            name='self_signed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='keypair',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
