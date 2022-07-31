from django.shortcuts import render, redirect
from django.views import View
from .models import Item
from django.http import HttpResponse
from django import forms
from .forms import ItemForm
# Create your views here.

def ItemListView (request):#done testing
    obj = Item.objects.all()
    print('check obj:',obj)
    context = {
        'obj':obj
    }

    return render(request,"ListItem.html",context)




def ItemAddView (request):
    form = ItemForm()
    context = {
        'form' : form
    }

    if request.method == 'POST':
        form = ItemForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
        else:
            form = ItemForm()

    return render(request,'Additem.html',context)



def ItemDeleteView(request,id):
    obj = Item.objects.get(id = id)
    obj.delete()

    return redirect('ListItem')

def ItemUpdateView (request,id):
    obj = Item.objects.get(id = id)
    form = ItemForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ListItem')

    context = {
        "object":obj,
        "form":form
    }

    return render(request, 'UpdateItem.html', context)