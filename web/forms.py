from django import forms
from .models import Expence,Income




class ExpenceForm (forms.Form):
    token = forms.CharField(required=True)
    amount =forms.IntegerField(required=True)
    text = forms.CharField(required=False)
    date = forms.DateTimeField(required=False)
