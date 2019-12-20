from django import forms
from Kwitter.kwitterusers.models import KwitterUser


class NewUserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = KwitterUser
        fields = ['username', 'password']
