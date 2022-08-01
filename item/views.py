from django.shortcuts import render, redirect
from django.views import View
from .models import Item
from django.http import HttpResponse
from django import forms
from .forms import ItemForm
from calendar import HTMLCalendar
import calendar, datetime
from datetime import date
# Create your views here.

def ItemListView (request):#done testing
    obj = Item.objects.all()

   # adding a calendar here
#     month_number = list(calendar.month_name).index(month) #convert month from name to number
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    cal = HTMLCalendar().formatmonth(current_year,current_month)


    context = {
        'obj':obj,
        'cal':cal,

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