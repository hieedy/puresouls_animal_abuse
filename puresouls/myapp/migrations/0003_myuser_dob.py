# Generated by Django 3.2 on 2021-05-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_myuser_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]