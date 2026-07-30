from django.db import models
from django.core.validators import MinValueValidator


class Runway(models.Model):
    '''
    Class for info on aeroddrome runways

    len: int - total length of a runway in meters
    code: str - 2 to 3 char code consisting of two digits and one letter L,C or R (optional)
    aerodrome: Aerodrome - aerodrome object where the runway is located
    '''
    class Meta:
        unique_together = [('aerodrome', 'code')]

    len = models.IntegerField(validators=[MinValueValidator(10)])
    code = models.CharField(max_length=3)

    aerodrome = models.ForeignKey('aerodrome.Aerodrome',
                                  on_delete=models.CASCADE,
                                  blank=False,
                                  null=False,
                                  related_name='runways')

    def __str__(self):
        return f'Runway {self.code}, length:{self.len}'
