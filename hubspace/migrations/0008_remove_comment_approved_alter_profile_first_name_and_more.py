# Generated by Django 4.2.4 on 2023-10-14 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubspace', '0007_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]