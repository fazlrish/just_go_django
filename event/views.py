from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView

from event.models import Event


class EventCreate(CreateView):
    model = Event
    template_name = 'event/event_create.html'
    fields = [
        'name',
        'describe',
        'type',
        'status',
        'start_time',
        'end_time'
    ]

class EventUpdate(UpdateView):
    model = Event
    template_name = 'event/event_update.html'
    fields = [
        'name',
        'describe',
        'type',
        'status',
        'start_time',
        'end_time'
    ]