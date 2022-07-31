from django.shortcuts import render
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



