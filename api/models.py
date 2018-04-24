from django.db import models
from django.utils import timezone


class Weather(models.Model):
    city = models.CharField(max_length=200)
    last_update = models.DateTimeField(
            default=timezone.now)

    def update(self):
        self.last_update = timezone.now()
        self.save()

    def __str__(self):
        return self.city