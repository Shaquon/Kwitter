from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout

from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kwitterusers.forms import AddUserForm


# def index_view(request):
#     html = 'index.html'
#     user=request.user
#     kwitteruser=KwitterUser.objects.get(user=user)


def add_user_view(request):
    html = 'newuser.html'
    logged_in_user = KwitterUser.objects.get(user=request.user)

    if request.method == "POST":
        form = Kweet