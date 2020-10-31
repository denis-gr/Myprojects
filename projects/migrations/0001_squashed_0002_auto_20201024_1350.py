# Generated by Django 3.1.2 on 2020-10-31 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('projects', '0001_initial'), ('projects', '0002_auto_20201024_1350')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начат')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Окончен')),
                ('soft_deadline', models.DateField(blank=True, null=True, verbose_name='Мягкий дедлайн')),
                ('hard_deadline', models.DateField(blank=True, null=True, verbose_name='Жесткий дедлайн')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
