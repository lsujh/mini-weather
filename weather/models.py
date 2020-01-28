from django.db import models


class ExistingData(models.Model):
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=10)
    main = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    icon = models.CharField(max_length=10)
    base = models.CharField(max_length=25)
    temp = models.CharField(max_length=10)
    pressure = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
    temp_min = models.CharField(max_length=10)
    temp_max = models.CharField(max_length=10)
    visibility = models.CharField(max_length=10)
    wind_speed = models.CharField(max_length=10)
    clouds_all = models.CharField(max_length=10)
    data = models.DateTimeField(auto_now_add=True)
