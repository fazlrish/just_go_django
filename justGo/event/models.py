from django.db import models

# Create your models here.
from django.utils import timezone


class Event(models.Model):

    dateTime = models.DateTimeField(blank=False, null=False, default=timezone.now())
    eventType = models.PositiveSmallIntegerField(blank=False, null=False)

