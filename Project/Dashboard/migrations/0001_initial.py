# Generated by Django 4.0.3 on 2022-03-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File_Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=30)),
                ('my_file', models.FileField(upload_to='FileUploads')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
