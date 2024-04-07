from django.db import models

# lat: 52.654903 Long: -7.246403


class WeatherDataHourly(models.Model):
    date = models.DateTimeField()
    temp = models.FloatField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    feels_like = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    rain_h1 = models.FloatField(null=True, blank=True)
    snow_h1 = models.FloatField(null=True, blank=True)
    clouds_all = models.FloatField()
    weather_main = models.TextField(max_length=90)

    def __str__(self):
        return self.date_time.strftime("%Y-%m-%d %H:%M:%S")
