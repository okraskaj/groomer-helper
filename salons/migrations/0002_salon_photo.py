# Generated by Django 2.0 on 2018-01-17 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='photo',
            field=models.ImageField(default='salons/None/no-img.png', upload_to='salons/'),
        ),
    ]
