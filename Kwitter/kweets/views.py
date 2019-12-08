from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet
from Kwitter.kweets.forms import AddTweetForm
from Kwitter.notifications.models import Notification
from django.contrib.auth.models import User

import re


def add_kweet_view(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        kweet = form.save()

        user = request.user
        kwitterUser = KwitterUser.objects.get(user=user)
        kweet.user = kwitterUser
        kweet.save()
        message = kweet.message_input

        notified_users = re.findall(r'@(\S*)', message)
        if notified_users:
            all_users = User.objects.all()
            all_usernames = [user.username for user in all_users]
            for notified_user in notified_users:
                if notified_user in all_usernames:
                    receiver_user = User.objects.get(username=notified_user)
                    receiver = KwitterUser.objects.get(user=receiver_user)
                    Notification.objects.create(
                        receiver=receiver,
                        kweet=kweet,
                        not_viewed=True
                    )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddTweetForm()
    return render(request, html, {'form': form})


def kweet_detail_view(request):
    html = 'kweet_detail.html'

    kweet = Kweet.ojects.get(pk=id)

    return render(request, html, {'tweet': kweet})


def add_like_view(request):
    pass


def remove_like_view(request):
    pass
