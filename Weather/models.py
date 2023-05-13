from django.db import models
from django.core.exceptions import ValidationError


class WeatherKiev(models.Model):

    date = models.CharField(max_length=50, default='')
    temperature_day = models.CharField(max_length=10, default='')
    temperature_night = models.CharField(max_length=10, default='')
    weather_description = models.TextField(default='', blank=True)


class ParserSetting(models.Model):

    STATUS = (
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    )

    update_time = models.TimeField(default='09:00')
    status = models.CharField(max_length=20, choices=STATUS, default='done')
