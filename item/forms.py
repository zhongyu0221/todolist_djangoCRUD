from .models import Item
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from datetime import date

#Create the Form class
class ItemForm(ModelForm):
    class Meta:

        model = Item
        fields = "__all__"




#validation!!!
# the clean funcion title MUST match the field name!!!!!!
    def clean_Due_Date(self,*args,**kwargs):
        Due_Date = self.cleaned_data['Due_Date']
        now = date.today()
        print(now)
        if Due_Date < now:
            raise forms.ValidationError ('You cannot record a past event')
            print('validation error')
        return Due_Date




