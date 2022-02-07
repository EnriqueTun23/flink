import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    market_values = ArrayField(models.CharField(max_length=100), size=50)
