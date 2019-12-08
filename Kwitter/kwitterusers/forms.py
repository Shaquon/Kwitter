from django import forms
from Kwitter.kweets.models import Kweet

class NewKweetForm(forms.Modelsform):
    class Meta:
        model = Kweet
        fields = ['message_input']