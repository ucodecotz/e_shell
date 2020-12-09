# Generated by Django 3.1.3 on 2020-12-09 04:27

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201208_0758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='address2',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='TIN_no',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='payment_option',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='region',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
