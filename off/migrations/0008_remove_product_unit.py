# Generated by Django 3.2.9 on 2021-12-04 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off', '0007_alter_product_carbo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unit',
        ),
    ]