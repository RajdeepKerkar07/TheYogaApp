# Generated by Django 4.0.4 on 2022-07-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_alter_diet_problem'),
        ('users', '0008_remove_profile_diet_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='diet',
            field=models.ManyToManyField(to='diet.diet'),
        ),
    ]
