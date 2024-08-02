# Generated by Django 5.0.6 on 2024-08-02 13:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_apply_delete_aplay'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Apply_Job', to='job.job'),
            preserve_default=False,
        ),
    ]
