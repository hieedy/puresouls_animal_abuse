# Generated by Django 3.2.3 on 2021-05-27 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_remove_mylaws_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myanimal_disease',
            old_name='name',
            new_name='category_id',
        ),
    ]