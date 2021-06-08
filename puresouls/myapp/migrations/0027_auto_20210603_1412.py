# Generated by Django 3.2.3 on 2021-06-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20210603_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybookappointment',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mybookappointment',
            name='app_status',
            field=models.CharField(choices=[('P', 'Pending'), ('NA', 'Not Approved'), ('A', 'Approved')], default='P', max_length=2),
        ),
    ]