# Generated by Django 2.2.6 on 2019-11-05 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Domain')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Subject')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
