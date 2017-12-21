# Create your models here.
from django.db import models
from django.db.models import ManyToManyField
from django.utils import timezone


#ToDo Look at time zone
from authentication.models import BaseUser


class Event(models.Model):

    user = ManyToManyField(BaseUser)
    name = models.CharField(blank=False, null=False, max_length=128)
    describe = models.TextField(max_length=600)
    type = models.PositiveSmallIntegerField(blank=False, null=False)
    status = models.PositiveSmallIntegerField(blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False, default=timezone.now())
    end_time = models.DateTimeField(blank=False, null=False, default=timezone.now())

class Place(models.Model):

    name = models.CharField(blank=False, null=False, max_length=128)
    lat = models.FloatField(blank=False, null=False)
    lng = models.FloatField(blank=False, null=False)
    event = models.ManyToManyField(Event)