from django.conf.urls import url

from authentication.views import BaseUserCreate, index

urlpatterns = [

    url(r'^/', index, name='index'),
    url(r'^create/', BaseUserCreate.as_view(), name='baseUserCreate')
]