# Generated by Django 4.0.3 on 2022-04-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asanas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asana',
            name='duration',
            field=models.TimeField(default='00:00'),
        ),
    ]