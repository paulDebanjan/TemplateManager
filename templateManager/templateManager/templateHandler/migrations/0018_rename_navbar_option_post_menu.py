# Generated by Django 4.1.7 on 2023-02-20 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0017_rename_posts_image_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='navbar_option',
            new_name='menu',
        ),
    ]
