from django.db import models


class Trip(models.Model):
    country = models.CharField(max_length=30)
    departure = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.departure.title()}-{self.destination.title()}"
