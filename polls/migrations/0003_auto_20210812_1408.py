# Generated by Django 3.2.6 on 2021-08-12 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='pw',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='id',
            new_name='userid',
        ),
    ]