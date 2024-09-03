from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Item, Category 
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    template = loader.get_template('items.html')
    context = {
            'items':items,
            'querry':query,
            'categories':categories,
            'category_id':int(category_id),
            }
    return HttpResponse(template.render(context, request))

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    template = loader.get_template('details.html')
    context = {
        'item':item,
        'related_item':related_item,       
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'details.html', { 'item':item })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    template = loader.get_template('form.html')
    context = {
        'form':form,
        'title':'New item'
        }
    return HttpResponse(template.render(context, request))

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST,request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    template = loader.get_template('form.html')
    context = {
        'form':form,
        'title':'Edit',
        }
    return HttpResponse(template.render(context, request))


def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')