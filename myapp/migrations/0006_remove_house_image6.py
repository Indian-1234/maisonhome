# Generated by Django 4.1.7 on 2023-05-05 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_image_house_image1_house_image2_house_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='image6',
        ),
    ]