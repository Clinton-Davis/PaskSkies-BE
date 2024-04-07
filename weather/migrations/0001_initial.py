# Generated by Django 5.0.4 on 2024-04-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('pressure', models.FloatField()),
                ('humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_deg', models.FloatField()),
                ('rain_h1', models.FloatField(blank=True, null=True)),
                ('snow_h1', models.FloatField(blank=True, null=True)),
                ('clouds_all', models.FloatField()),
                ('weather_main', models.TextField(max_length=90)),
                ('cloud_cover_percentage', models.FloatField()),
            ],
        ),
    ]