# Generated by Django 5.0.7 on 2024-07-28 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('DOC', 'Documents'), ('ART', 'Articles'), ('VID', 'Videos'), ('AUD', 'Audios'), ('IMG', 'Images'), ('SER', 'Services')], max_length=3)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('cite', models.CharField(blank=True, max_length=250, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='publications/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('institutional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.institucional')),
            ],
        ),
    ]
