from django.shortcuts import render, loader
from django.http import HttpResponse
from .forms import Options
# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))


