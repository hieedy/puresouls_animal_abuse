# Generated by Django 3.2 on 2021-05-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20210515_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='myhospital',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]