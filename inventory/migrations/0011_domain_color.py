# Generated by Django 3.0.3 on 2020-02-14 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20200214_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
