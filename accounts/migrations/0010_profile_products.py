# Generated by Django 3.0.3 on 2020-02-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20200212_2203'),
        ('accounts', '0009_auto_20200209_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(through='inventory.Usage', to='inventory.Product'),
        ),
    ]
