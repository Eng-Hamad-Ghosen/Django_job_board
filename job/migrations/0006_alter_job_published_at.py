# Generated by Django 5.0.6 on 2024-06-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_remove_job_published_job_experience_job_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
