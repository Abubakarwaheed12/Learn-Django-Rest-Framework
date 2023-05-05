# Generated by Django 4.2.1 on 2023-05-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('father_name', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Our Students',
            },
        ),
    ]
