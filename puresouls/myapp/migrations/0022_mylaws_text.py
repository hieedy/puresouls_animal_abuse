# Generated by Django 3.2.3 on 2021-05-25 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20210522_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='mylaws',
            name='text',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
