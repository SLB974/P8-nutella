# Generated by Django 3.2.9 on 2021-11-26 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('off', '0003_rename_favorites_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic_small_url',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='pic_thumb_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
