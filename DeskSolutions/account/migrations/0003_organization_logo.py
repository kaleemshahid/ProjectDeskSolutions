# Generated by Django 3.1.3 on 2020-12-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201115_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
