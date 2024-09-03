from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def index(request):
    items = Item.objects.filter(created_by=request.user)
    template = loader.get_template('index.html')
    context = {'items':items}
    return HttpResponse(template.render(context, request))

