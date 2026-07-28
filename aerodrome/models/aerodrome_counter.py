from pydantic import BaseModel
from django.db import models


class AerodromeCounter(BaseModel):
    """Counts total number of aerodromes created."""
    total = models.IntegerField()
    id = models.IntegerField(primary_key=True, default=1)
