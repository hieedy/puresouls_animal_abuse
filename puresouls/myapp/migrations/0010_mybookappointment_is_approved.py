# Generated by Django 3.2 on 2021-05-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210514_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybookappointment',
            name='is_approved',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
