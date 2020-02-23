# Generated by Django 3.0.3 on 2020-02-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20200222_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]