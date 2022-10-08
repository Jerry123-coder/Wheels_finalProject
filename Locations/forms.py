from django import forms
from .models import UserTrip

class LocationForm(forms.ModelForm):
    pickL = forms.CharField(max_length=300, widget=forms.TextInput(attrs={
        'placeholder' : 'Pick Up Location'
    }))
    dropL = forms.CharField(max_length=300, widget=forms.TextInput(attrs={
        'placeholder' : 'Drop Off Location'
    }))
    
    class Meta:
        model = UserTrip
        fields = ['pickL','dropL']