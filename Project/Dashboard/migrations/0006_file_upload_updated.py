# Generated by Django 4.0.3 on 2022-03-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_alter_file_upload_user_specific'),
    ]

    operations = [
        migrations.AddField(
            model_name='file_upload',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
