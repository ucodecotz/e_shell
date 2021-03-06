# Generated by Django 3.1.3 on 2020-12-12 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('create_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product Category',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('create_on', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Product Sub Category',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping address'},
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='user',
            new_name='customer',
        ),
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
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='session_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(max_length=30, null=True),
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
        migrations.AddField(
            model_name='shippingaddress',
            name='tin_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image'),
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('create_on', models.DateTimeField(default=django.utils.datetime_safe.datetime.now)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subcategory')),
            ],
            options={
                'verbose_name_plural': 'Product Sub sub Category',
            },
        ),
        migrations.CreateModel(
            name='OrderDeliveryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_order_at_station', models.CharField(max_length=200, null=True)),
                ('deliver_my_order', models.CharField(max_length=200, null=True)),
                ('insure_my_order', models.CharField(max_length=200, null=True)),
                ('same_day_delivery', models.CharField(max_length=200, null=True)),
                ('express_delivery', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='deliveryInfo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.orderdeliveryinfo'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.subsubcategory'),
        ),
    ]
