# Generated by Django 4.0.5 on 2022-06-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_profile_projects_profile_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='projects',
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.project'),
        ),
    ]
