# Generated by Django 4.2.5 on 2023-09-27 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Покупатели',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('Junior manager', 'Junior Manager'), ('Senior manager', 'Senior Manager')], default='Junior manager', max_length=30)),
                ('is_manager', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Deleted', 'Deleted')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('formed_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.customer')),
                ('moderator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.employer')),
            ],
            options={
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='CubeSat/static/images/')),
                ('category_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.categories')),
            ],
            options={
                'verbose_name_plural': 'Детали',
            },
        ),
        migrations.CreateModel(
            name='OrdersToProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CubeSat.products')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CubeSat.orders')),
            ],
        ),
        migrations.CreateModel(
            name='AttributesValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField()),
                ('attribute_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.attributes')),
                ('product_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.products')),
            ],
        ),
        migrations.AddField(
            model_name='attributes',
            name='category_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CubeSat.categories'),
        ),
    ]