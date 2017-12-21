from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from authentication.models import BaseUser

def index(request):
    return render(request=request, template_name='authentication/base.html')


class BaseUserCreate(CreateView):
    model = BaseUser
    success_url = '/authentication/'
    template_name = 'authentication/baseUser_create.html'
    fields = [
        'username',
        'email',
        'password'
    ]