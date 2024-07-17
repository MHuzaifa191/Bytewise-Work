from django import forms 

from .models import Participant

class RegForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']