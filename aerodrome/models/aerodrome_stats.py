from django.db import models


class AerodromeStats(models.Model):
    """Counts total number of aerodromes created."""

    total = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True, default=1)
