# Generated by Django 4.1.7 on 2023-02-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='postsImages/'),
        ),
    ]