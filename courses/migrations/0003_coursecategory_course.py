# Generated by Django 5.0.1 on 2024-02-06 08:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория курса',
                'verbose_name_plural': 'Категории курсов',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название курса')),
                ('description', models.TextField(default=True, verbose_name='Описание курса')),
                ('theme', models.CharField(default=None, max_length=100, verbose_name='Тема курса')),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Авторы курса')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.coursecategory')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
