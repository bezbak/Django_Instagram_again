# Generated by Django 3.2.19 on 2023-05-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]
