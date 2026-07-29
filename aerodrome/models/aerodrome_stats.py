from django.db import models


class AerodromeStats(models.Model):
    """Counts total number of aerodromes created."""
    total = models.IntegerField()
    id = models.IntegerField(primary_key=True, default=1)
