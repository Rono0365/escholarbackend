# Generated by Django 4.0.2 on 2022-04-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Class',
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(to='cloud.Student'),
        ),
        migrations.AddField(
            model_name='homework',
            name='Class',
            field=models.ManyToManyField(to='cloud.Class'),
        ),
    ]