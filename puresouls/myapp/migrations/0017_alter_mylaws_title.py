# Generated by Django 3.2.3 on 2021-05-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_myngos_opening_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mylaws',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
