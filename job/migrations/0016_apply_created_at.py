# Generated by Django 5.0.6 on 2024-08-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0015_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]