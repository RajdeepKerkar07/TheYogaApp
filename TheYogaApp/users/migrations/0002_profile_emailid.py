# Generated by Django 4.0.3 on 2022-04-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emailId',
            field=models.EmailField(default='abc@gmail.com', max_length=256),
        ),
    ]
