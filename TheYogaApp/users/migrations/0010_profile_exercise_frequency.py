# Generated by Django 4.0.4 on 2022-07-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_diet'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='exercise_frequency',
            field=models.CharField(default='0', max_length=1),
        ),
    ]