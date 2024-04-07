import csv
import django
import os
from datetime import datetime

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "psback.settings")
django.setup()

from weather.models import WeatherDataHourly  # Import your model
from django.utils.dateparse import parse_datetime

# Path to your CSV file
csv_file_path = "2009-2024-kil-hist-weather-data.csv"


def load_data():
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Correctly processing the date by splitting and taking the first part
            row["dt_iso_clean"] = row["dt_iso"].split("+")[0]
            date = parse_datetime(row["dt_iso_clean"])
            if not date:
                print(f"Skipping row due to invalid date: {row}")
                continue

            WeatherDataHourly.objects.create(
                date=date,
                temp=float(row["temp"]),
                min_temp=float(row["temp_min"]),
                max_temp=float(row["temp_max"]),
                feels_like=float(row["feels_like"]),
                pressure=float(row["pressure"]),
                humidity=float(row["humidity"]),
                wind_speed=float(row["wind_speed"]),
                wind_deg=float(row["wind_deg"]),
                rain_h1=row.get("rain_h1"),
                snow_h1=row.get("snow_h1"),
                clouds_all=float(row["clouds_all"]),
                weather_main=row["weather_main"],
            )


if __name__ == "__main__":
    load_data()
