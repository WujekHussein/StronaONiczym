# Generated by Django 5.1.6 on 2025-02-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
