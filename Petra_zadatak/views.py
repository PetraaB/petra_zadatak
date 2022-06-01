from django.shortcuts import render
from django.views.generic import ListView
from .models import Karte

# Create your views here.

class home(ListView):
    template_name = 'generic_cms/home.html'
    model = Karte
    ordering = ['-vrijeme']
    context_object_name = "karte"