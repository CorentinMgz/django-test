# Generated by Django 3.2.5 on 2021-11-09 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='licence_place',
            new_name='licence_plate',
        ),
        migrations.AlterField(
            model_name='driver',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
