# Generated by Django 3.1.7 on 2021-03-08 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_group_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
