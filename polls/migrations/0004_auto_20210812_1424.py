# Generated by Django 3.2.6 on 2021-08-12 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210812_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='userid',
            new_name='IDwlgns',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='password',
            new_name='passwordwlgns',
        ),
    ]
