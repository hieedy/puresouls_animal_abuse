# Generated by Django 3.2 on 2021-05-11 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mybodyparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mycontactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=30)),
                ('suggestion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='mydiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('abstract', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='mydoctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='myhelp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=30)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='myhospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='mylaws',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='myngos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('website', models.URLField()),
                ('account_no', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='myregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='myreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=10)),
                ('dob', models.DateField(blank=True, null=True)),
                ('state', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='myvaccination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('approx_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='symtoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydiseases')),
            ],
        ),
        migrations.CreateModel(
            name='myreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='myexpertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_In', models.CharField(max_length=20)),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydoctors')),
            ],
        ),
        migrations.AddField(
            model_name='mydiseases',
            name='vaccine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.myvaccination'),
        ),
        migrations.CreateModel(
            name='mybookappointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.DateTimeField()),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydoctors')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.myuser')),
            ],
        ),
        migrations.CreateModel(
            name='doc_specialist_ids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydiseases')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydoctors')),
            ],
        ),
        migrations.CreateModel(
            name='disease_symtoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydiseases')),
                ('symptom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.symtoms')),
            ],
        ),
        migrations.CreateModel(
            name='bodypartdisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mybodyparts')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mydiseases')),
            ],
        ),
    ]
