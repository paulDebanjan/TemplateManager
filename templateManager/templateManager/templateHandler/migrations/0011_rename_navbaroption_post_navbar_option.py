# Generated by Django 4.1.7 on 2023-02-19 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0010_alter_post_pragraphone_alter_post_pragraphtwo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='NavbarOption',
            new_name='navbar_option',
        ),
    ]
