# Generated by Django 5.0.6 on 2024-06-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Port Time', 'Port Time')], default='', max_length=15),
            preserve_default=False,
        ),
    ]