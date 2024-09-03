from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Member
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_members(request):
    mymembers = Member.objects.all().values()
    return render(request, 'allmembers.html', {'mymembers':mymembers})
    # template = loader.get_template('myFirst.html')
    # return HttpResponse(template.render())

def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    # return render(request, 'details.html', {'mymember':mymember})
    template = loader.get_template('details.html')
    context = {'mymember':mymember}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def members(request):
    members = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {'members':members}
    return HttpResponse(template.render(context, request))

def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/members/')
    else:
        form =UserCreationForm()

    template = loader.get_template('signup.html')
    context = {'form':form}
    return HttpResponse(template.render(context, request))

def loginView(request):
    if request.method == 'POST':    
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/members/')
    else:
        form = AuthenticationForm()
    template = loader.get_template('login.html')
    context = {'form':form}
    return HttpResponse(template.render(context, request))