# Generated by Django 4.1.7 on 2023-04-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0021_homedesign_logocolor_homedesign_websitecommit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homedesign',
            name='webSiteNameSize',
            field=models.IntegerField(null=True),
        ),
    ]