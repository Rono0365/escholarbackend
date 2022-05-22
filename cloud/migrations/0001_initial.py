# Generated by Django 4.0.2 on 2022-04-22 00:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no homework', max_length=100)),
                ('deadline', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('day_taught', models.CharField(max_length=100)),
                ('time_taught', models.CharField(max_length=100)),
                ('time_duration', models.CharField(max_length=100)),
                ('place_taught', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('teacher', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, default='', max_length=100)),
                ('adm_no', models.CharField(blank=True, default='', max_length=100)),
                ('School', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cloud.school')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_no', models.CharField(blank=True, default='', max_length=100)),
                ('Class', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cloud.class')),
                ('School', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cloud.school')),
                ('Subjects', models.ManyToManyField(default='', to='cloud.Subject')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['adm_no'],
            },
        ),
    ]