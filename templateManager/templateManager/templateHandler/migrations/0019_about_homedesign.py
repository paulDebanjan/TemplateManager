# Generated by Django 4.1.7 on 2023-04-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0018_rename_navbar_option_post_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webSiteName', models.CharField(max_length=75)),
                ('backbroundImage', models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='homePageImage/')),
                ('navbaColor', models.CharField(default='000000', max_length=6)),
                ('navbaHoverColor', models.CharField(default='F50057', max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
