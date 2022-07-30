from django.contrib import admin
from django.urls import path


from .views import ItemAddView,ItemListView

urlpatterns = [
    path('ItemAdd/',ItemAddView, name = 'AddItem'),
    path('ItmeList/',ItemListView, name = 'ListItem'),
]

