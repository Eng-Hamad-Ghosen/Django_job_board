# Generated by Django 5.0.6 on 2024-07-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]