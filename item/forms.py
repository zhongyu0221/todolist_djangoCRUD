from .models import Item
from django.forms import ModelForm


#Create the Form class
class ItemForm(ModelForm):
    class Meta:

        form = Item
        Fields = ['Title',
                  'Details']




#Create a add item form

# Create a update item form