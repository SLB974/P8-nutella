# Generated by Django 3.2.9 on 2021-12-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('off', '0006_auto_20211204_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='carbo',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
    ]
