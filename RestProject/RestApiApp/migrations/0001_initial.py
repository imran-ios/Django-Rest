# Generated by Django 3.0.5 on 2021-05-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=100)),
                ('customerEmail', models.EmailField(max_length=254)),
                ('customerMobileNo', models.IntegerField(max_length=15)),
                ('customerAddress', models.CharField(max_length=200)),
            ],
        ),
    ]
