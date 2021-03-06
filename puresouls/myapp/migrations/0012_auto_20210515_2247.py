# Generated by Django 3.2 on 2021-05-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210515_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='myhospital',
            name='opening_hours',
            field=models.CharField(default='24*7', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myhospital',
            name='specialization',
            field=models.CharField(default='Dogs', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myhospital',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
