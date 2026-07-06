from django.db import models


class Aerodrome(models.Model):
    icao_code = models.CharField(max_length=4, unique=True)
    name = models.TextField()
    city = models.TextField()
