# Generated by Django 5.0.6 on 2024-06-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
