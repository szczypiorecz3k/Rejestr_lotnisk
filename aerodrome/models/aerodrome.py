from django.core.validators import RegexValidator
from django.db import models


class Aerodrome(models.Model):
    """Class for basic aerodrome info

    icao_code: str - 4 letter aerodrome code, must be unique
    name: str - full aerodrome name
    city: str - location of the aerodrome or nearest big city"""

    icao_code = models.CharField(
        max_length=4, unique=True, validators=[RegexValidator(r'^[A-Za-z]{4}$')]
    )
    name = models.TextField()
    city = models.TextField()

    def save(self, *args, **kwargs):
        self.icao_code = self.icao_code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.icao_code
