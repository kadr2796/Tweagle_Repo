# Generated by Django 3.2.4 on 2021-06-06 22:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landingpage', '0005_rename_body_post_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Report',
        ),
    ]
