# Generated by Django 5.1a1 on 2024-07-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_main_pecase_school_pecase_uni_pecase'),
    ]

    operations = [
        migrations.CreateModel(
            name='school_pecase_fem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
                ('rank', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('range', models.IntegerField()),
                ('normalized_freq', models.FloatField()),
                ('normalized_range', models.FloatField()),
                ('sex', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='school_pecase_man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
                ('rank', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('range', models.IntegerField()),
                ('normalized_freq', models.FloatField()),
                ('normalized_range', models.FloatField()),
                ('sex', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='uni_pecase_fem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
                ('rank', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('range', models.IntegerField()),
                ('normalized_freq', models.FloatField()),
                ('normalized_range', models.FloatField()),
                ('sex', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='uni_pecase_man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
                ('rank', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('range', models.IntegerField()),
                ('normalized_freq', models.FloatField()),
                ('normalized_range', models.FloatField()),
                ('sex', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='uni_pecase_mf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
                ('rank', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('range', models.IntegerField()),
                ('normalized_freq', models.FloatField()),
                ('normalized_range', models.FloatField()),
                ('sex', models.TextField()),
            ],
        ),
    ]
