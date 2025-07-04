# Generated by Django 5.2.3 on 2025-06-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=100)),
                ('flight', models.CharField(max_length=100)),
                ('source_city', models.CharField(max_length=100)),
                ('departure_time', models.CharField(max_length=100)),
                ('cls', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('days_left', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'pridiction_request',
            },
        ),
    ]
