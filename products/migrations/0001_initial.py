# Generated by Django 3.2.3 on 2021-05-29 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_buy', models.DateTimeField()),
            ],
            options={
                'db_table': 'bill',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'laptop',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'monitor',
            },
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'pc',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description_general', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='resouce')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Type_peripheral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'type_peripheral',
            },
        ),
        migrations.CreateModel(
            name='Peripheral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('link_website', models.CharField(max_length=300)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('type_peripherals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.type_peripheral')),
            ],
            options={
                'db_table': 'peripheral',
            },
        ),
        migrations.CreateModel(
            name='Pc_character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphic_card', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=50)),
                ('refrigeration', models.CharField(max_length=100)),
                ('monitors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.monitor')),
                ('pcs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.pc')),
                ('peripherals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.peripheral')),
            ],
            options={
                'db_table': 'pc_character',
            },
        ),
        migrations.AddField(
            model_name='pc',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.CreateModel(
            name='Monitor_character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('hz', models.CharField(max_length=100)),
                ('quality', models.CharField(max_length=100)),
                ('monitors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.monitor')),
            ],
            options={
                'db_table': 'monitor_character',
            },
        ),
        migrations.AddField(
            model_name='monitor',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.CreateModel(
            name='Laptops_character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphic_card', models.CharField(max_length=100)),
                ('keyboard', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('storage', models.CharField(max_length=50)),
                ('warranty', models.CharField(max_length=100)),
                ('laptops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.laptop')),
            ],
            options={
                'db_table': 'laptops_character',
            },
        ),
        migrations.AddField(
            model_name='laptop',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('price', models.IntegerField(verbose_name='Price')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.bill')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_order', to='products.products')),
            ],
            options={
                'db_table': 'detail',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.AddField(
            model_name='bill',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.customer'),
        ),
    ]