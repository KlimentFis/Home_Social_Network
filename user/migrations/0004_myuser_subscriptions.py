# Generated by Django 5.1.1 on 2024-10-17 20:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_myuser_about_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='user_subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
