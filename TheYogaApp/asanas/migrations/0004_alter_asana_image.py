# Generated by Django 4.0.3 on 2022-04-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asanas', '0003_asana_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asana',
            name='image',
            field=models.CharField(default='', max_length=256),
        ),
    ]