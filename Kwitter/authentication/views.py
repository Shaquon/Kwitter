from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.authentication.forms import LoginForm
from Kwitter.kwitterusers.forms import NewUserForm
from django.contrib.auth.models import User
from django.forms import ValidationError
# from django.contrib.auth.decorators import login_required


def login_view(request):

    html = 'generic_form.htm'
    page = 'login'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home'))
            )

    form = LoginForm()
    return render(request, html, {'form': form, 'page': page})


def register_user_view(request):
    html = 'generic_form.htm'
    page = 'register'
    if request.method == "POST":

        form = NewUserForm(request.POST)

        current_user = request.user
        # already_a_user = User.objects.filter(username=current_user)

        # if already_a_user.exists():
        #     raise form.ValidationError("That user is already taken")

        if form.is_valid():

            data = form.cleaned_data
    
            u = User.objects.create_user(
                username=data['username'],
                password=data['password'])

            KwitterUser.objects.create(user=u)

            login(request, u)
            return HttpResponseRedirect(reverse('home'))
    form = NewUserForm()

    return render(request, html, {'form': form, 'page': page})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
