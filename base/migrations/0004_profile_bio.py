# Generated by Django 4.0.5 on 2022-06-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_profile_projects_profile_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=60, null=True),
        ),
    ]
