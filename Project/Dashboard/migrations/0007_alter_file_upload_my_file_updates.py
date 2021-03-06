# Generated by Django 4.0.3 on 2022-03-26 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0006_file_upload_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='my_file',
            field=models.FileField(upload_to='F'),
        ),
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
