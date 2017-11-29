from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^event/getName', views.GetName, name='event')
]