# Generated by Django 5.0.7 on 2024-08-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='propertycategory',
            options={'verbose_name': 'Property Category', 'verbose_name_plural': 'Property Categories'},
        ),
        migrations.AlterModelOptions(
            name='propertytype',
            options={'verbose_name': 'Property Type', 'verbose_name_plural': 'Property Types'},
        ),
        migrations.AlterField(
            model_name='propertycategory',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
