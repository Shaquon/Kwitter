from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.authentication.forms import LoginForm
from Kwitter.kwitterusers.forms import NewUserForm
# from django.contrib.auth.decorators import login_required


def login_view(request):

    html = 'generic_form.html'

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
                request.GET.get('next', reverse('hompage'))
            )

    form = LoginForm()
    return render(request, html, {'form': form, 'page': form})


def register_user_view(request):
    html = 'generic_html'

    if request.method == "POST":
        form = NewUserForm()
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(username=data['username'], password=data['password'])
            KwitterUser.objects.create(user=u, bio=data['bio'])
            login(request, u)
            return HttpResponseRedirect(reverse('homepage'))
    form = NewUserForm()

    return render(request, html, {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
