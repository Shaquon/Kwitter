from django import forms 

from Kwitter.kweets.models import Kweet


class AddTweetForm(forms.ModelForm):
    class Meta:
        model = Kweet
        fields = ['message_input']