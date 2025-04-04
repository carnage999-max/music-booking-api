# Generated by Django 5.1.7 on 2025-04-02 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='organizerprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Bio'),
        ),
        migrations.AddField(
            model_name='organizerprofile',
            name='social_links',
            field=models.JSONField(blank=True, null=True, verbose_name='Social Links'),
        ),
        migrations.AddField(
            model_name='organizerprofile',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website URL'),
        ),
        migrations.AlterField(
            model_name='artistprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artist_profile', to=settings.AUTH_USER_MODEL, verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('artist', 'Artist'), ('organizer', 'Organizer'), ('admin', 'Admin')], max_length=10, verbose_name='User type'),
        ),
    ]
