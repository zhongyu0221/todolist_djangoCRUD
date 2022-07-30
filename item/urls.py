from django.contrib import admin
from django.urls import path

from item.views import ItemListView,ItemAddView

urlpatterns = [
    path('ItemAdd/',ItemAddView, name = 'AddItem'),
    path('ItmeList/',ItemListView, name = 'ListItem'),
]

