# Generated by Django 3.1.3 on 2020-11-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201128_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
