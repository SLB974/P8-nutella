# Generated by Django 3.2.9 on 2022-04-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('off', '0002_alter_favorite_replacement_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fiber2',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=7),
        ),
    ]
