# Generated by Django 3.0.3 on 2020-02-14 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_profile_products'),
        ('inventory', '0009_auto_20200212_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usage',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Profile'),
        ),
    ]