# Generated by Django 4.1.7 on 2023-02-20 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0012_rename_post_image_post_rename_images_post_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='templateHandler.post'),
        ),
    ]
