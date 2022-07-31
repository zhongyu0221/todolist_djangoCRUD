# Generated by Django 4.0.6 on 2022-07-31 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField(max_length=200)),
                ('Create_Date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('Due_Date', models.DateField()),
            ],
        ),
    ]
