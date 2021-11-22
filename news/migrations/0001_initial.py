# Generated by Django 3.2.9 on 2021-11-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
