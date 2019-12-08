from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from Kwitter.authentication.forms import LoginForm

def login_view(request):

    html = generic_form;

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valiD():
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

    form = Login_form()
    return render(request, html, {'form': form, 'page': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
