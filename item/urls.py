from django.contrib import admin
from django.urls import path


from .views import ItemAddView,ItemListView, ItemDeleteView,ItemUpdateView

urlpatterns = [
    path('ItemAdd/',ItemAddView, name = 'AddItem'),
    path('ItmeList/',ItemListView, name = 'ListItem'),
    path('ItemDelete/<int:id>', ItemDeleteView, name='DeleteItem'),
    path('ItemUpdate/<int:id>',ItemUpdateView , name='UpdateItem'),
]

