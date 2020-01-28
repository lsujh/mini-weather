from django import forms
from django.contrib.admin import widgets


class CityForm(forms.Form):
    name = forms.CharField(max_length=25)
    

class FilterForm(forms.Form):
    city = forms.CharField(max_length=25)
    data_from = forms.DateField(widget=widgets.AdminDateWidget)
    data_to = forms.DateField(widget=widgets.AdminDateWidget)
