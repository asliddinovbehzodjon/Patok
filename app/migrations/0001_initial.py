# Generated by Django 4.1.1 on 2022-10-04 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=600, verbose_name='Company name')),
                ('age', models.CharField(max_length=600, verbose_name='Age')),
                ('phone', models.CharField(max_length=600, verbose_name='Phone')),
                ('salary', models.CharField(max_length=600, verbose_name='Salary')),
                ('address', models.CharField(max_length=600, verbose_name='Address')),
                ('contact_time', models.CharField(max_length=600, verbose_name='Contact Time')),
                ('work_time', models.CharField(max_length=600, verbose_name='Work time')),
                ('requirements', models.CharField(max_length=600, verbose_name='Requirements')),
            ],
            options={
                'verbose_name': 'Ish beruvchi ',
                'verbose_name_plural': 'Ish beruvchilar ',
                'db_table': 'Ish beruvchilar ',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('age', models.CharField(max_length=600, verbose_name='Age')),
                ('phone', models.CharField(max_length=600, verbose_name='Phone')),
                ('job', models.CharField(max_length=600, verbose_name='Job')),
                ('salary', models.CharField(max_length=500, verbose_name='Salary')),
                ('address', models.CharField(max_length=600, verbose_name='Address')),
                ('about', models.CharField(max_length=600, verbose_name='About')),
                ('contact_time', models.CharField(max_length=600, verbose_name='Contact Time')),
                ('aim', models.CharField(max_length=600, verbose_name='Aim')),
            ],
            options={
                'verbose_name': 'Ishchi ',
                'verbose_name_plural': 'Ishchilar ',
                'db_table': 'Ishchilar',
            },
        ),
    ]