from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from item.models import Category, Item
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login,logout

# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)[0:6]
    template = loader.get_template('index.html')
    context = {
        'items':items,
        'categories':categories,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    template = loader.get_template('signup.html')
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()

    template = loader.get_template('login.html')
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def logoutView(request):
    logout(request)
    return redirect('/')