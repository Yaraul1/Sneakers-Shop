from django.shortcuts import render
from django.views.generic import View
from .models import *

def contact(request):
    context = 'shopcontact/contact.html'
    return render(request, context)
