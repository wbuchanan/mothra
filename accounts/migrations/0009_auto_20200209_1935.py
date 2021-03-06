# Generated by Django 2.2.6 on 2020-02-09 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_seed_org_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='github_id',
            field=models.CharField(blank=True, max_length=39, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.Organization'),
        ),
    ]
