from django.conf.urls import url

from event.views import EventCreate
from . import views

urlpatterns = [

    url(r'^create/', EventCreate.as_view(), name='event')
]