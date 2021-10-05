# Generated by Django 3.2.7 on 2021-10-05 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0002_rename_memberships_membership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='price_monthly',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='price_quarterly',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='price_yearly',
        ),
    ]
