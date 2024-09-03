from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def testing(request):
    template = loader.get_template('try.html')
    fruits = {
        'apple', 'banana', 'cherry'
    }
    context = {
        'fruits':fruits,   
    }
    return HttpResponse(template.render(context, request))
