from django import forms
from .models import Event

class EventForm(forms.Form):
    datetime_event = forms.DateTimeField(label ="datetime_event" , required=True)
    title = forms.CharField(label = "title")
    location = forms.DateField(label ="location" , required=True)
    price = forms.FloatField(label = "price")
    fname = forms.CharField(label = "fname", required=True)
    lname = forms.CharField(label = "lname", required=True)
    eaddress = forms.EmailField(label = "eaddress")
    tel = forms.IntegerField(label = "tel", required=True)
    num_of_people = forms.IntegerField(label = "num_of_people", required=True)
