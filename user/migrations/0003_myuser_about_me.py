# Generated by Django 5.1.1 on 2024-10-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_myuser_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='about_me',
            field=models.TextField(blank=True, verbose_name='Обо мне'),
        ),
    ]
