# Generated by Django 4.0.3 on 2022-03-20 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0002_remove_file_upload_id_file_upload_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_upload',
            name='user_specific',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]