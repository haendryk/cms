# Generated by Django 5.0.7 on 2024-07-28 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0008_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('soft_delete', models.BooleanField(default=False)),
                ('institutional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmsapp.institucional')),
            ],
        ),
    ]
