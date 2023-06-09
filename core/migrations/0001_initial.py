# Generated by Django 4.2.1 on 2023-06-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('position', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('thumbnail', models.ImageField(upload_to='logo/')),
                ('contact_num', models.IntegerField()),
                ('available', models.BooleanField()),
                ('email_add', models.EmailField(max_length=254)),
                ('job_type', models.ManyToManyField(to='core.jobtype')),
            ],
        ),
    ]
