# Generated by Django 4.2.5 on 2023-09-27 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CubeSat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributes',
            name='category_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CubeSat.categories'),
        ),
        migrations.AlterField(
            model_name='attributesvalues',
            name='attribute_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CubeSat.attributes'),
        ),
        migrations.AlterField(
            model_name='attributesvalues',
            name='product_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CubeSat.products'),
        ),
        migrations.AlterField(
            model_name='products',
            name='category_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CubeSat.categories'),
        ),
    ]