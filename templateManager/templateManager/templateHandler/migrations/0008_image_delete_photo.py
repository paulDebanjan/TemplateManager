# Generated by Django 4.1.7 on 2023-02-19 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templateHandler', '0007_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='postsImages/')),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='templateHandler.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]