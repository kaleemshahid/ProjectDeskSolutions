# Generated by Django 3.1.1 on 2020-11-14 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True, verbose_name='Address'),
        ),
    ]
