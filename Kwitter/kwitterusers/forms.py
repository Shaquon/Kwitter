from django import forms
from Kwitter.kwitterusers.models import KwitterUser


class NewUserForm(forms.Modelsform):
    class Meta:
        model = KwitterUser
        fields = ['user']
