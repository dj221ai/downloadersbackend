# Generated by Django 4.0.4 on 2022-05-13 11:04

import backendapis.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileDownloaderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sheet_name', models.CharField(blank=True, max_length=255, null=True)),
                ('xcel_file', models.FileField(blank=True, null=True, upload_to=backendapis.models.upload_to)),
            ],
        ),
    ]