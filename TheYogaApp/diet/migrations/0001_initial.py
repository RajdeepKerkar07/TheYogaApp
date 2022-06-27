# Generated by Django 4.0.4 on 2022-06-27 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tips', models.TextField()),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problems.problems')),
            ],
        ),
    ]
