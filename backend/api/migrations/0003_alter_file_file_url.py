# Generated by Django 5.0.6 on 2024-08-03 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_file_file_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_url',
            field=models.URLField(max_length=2000),
        ),
    ]
