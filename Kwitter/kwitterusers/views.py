from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout

from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kwitterusers.forms import AddUserForm


def index(request):
    pass


def add_kweet(request):
    pass


def add_like(request):


def remove_like(request):
    pass

def kweet(request):
    pass