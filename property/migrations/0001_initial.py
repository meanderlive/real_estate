# Generated by Django 5.0.7 on 2024-08-02 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.propertytype')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('bedroom', models.PositiveIntegerField()),
                ('bathroom', models.PositiveIntegerField()),
                ('living_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='property_images/')),
                ('property_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.propertycategory')),
                ('property_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.propertytype')),
            ],
        ),
    ]
