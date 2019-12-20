from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet
from Kwitter.kweets.forms import AddKweetForm
from Kwitter.notifications.models import Notifications
from django.contrib.auth.models import User
from Kwitter.kweets.models import Kweet

import re


@login_required
def index_view(request):
    html = "index.htm"

    user = request.user

    kwitteruser = KwitterUser.objects.get(user=user)

    notifications = Notifications.objects.filter(kwitter_user=user.kwitteruser)
    notification_count = len(notifications)

    followed_kweets = kwitteruser.followers.all()

    user_kweets = Kweet.objects.filter(user=kwitteruser)

    total_tweets = Kweet.objects.none()
    for each_user in kwitteruser.followers.all():
        total_tweets = total_tweets | Kweet.objects.filter(user=each_user) 

    total_tweets = total_tweets | user_kweets
    total_ordered = total_tweets.order_by('-post_time')

    # user_and_follower_kweets = followed_kweets | user_kweets
    # ordered_kweets = user_and_follower_kweets.order_by('-post_time')

    followed = list(followed_kweets)

    follow_count = len(followed)

    return render(request, html, {
        'kwitteruser': kwitteruser,
        'follow_count': follow_count,
        'followed': followed,
        'kweets': total_ordered,
        'notification_count': notification_count
    })


@login_required
def add_kweet_view(request):
    html = 'generic_form.htm'

    if request.method == 'POST':
        user = request.user

        form = AddKweetForm(request.POST)

        kweet = form.save()

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
                    Notifications.objects.create(
                        kwitter_user=receiver,
                        kweet=kweet,
                        not_viewed=True
                    )
        return HttpResponseRedirect(reverse('home'))

    form = AddKweetForm()
    return render(request, html, {'form': form})


@login_required
def kweet_detail_view(request, id):
    html = 'kweet_detail.htm'

    kweet = Kweet.objects.get(pk=id)

    return render(request, html, {'kweet': kweet})


# def add_like_view(request):
#     pass


# def remove_like_view(request):
#     pass
