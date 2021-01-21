# Generated by Django 3.1.4 on 2021-01-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapi', '0007_auto_20210118_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(upload_to='brand_logos/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_images/'),
        ),
    ]