# Generated by Django 5.0.2 on 2024-03-10 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fasesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fases',
            name='created_at',
        ),
    ]
