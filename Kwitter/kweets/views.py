from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet
from Kwitter.kweets.forms import AddKweetForm
from Kwitter.notifications.models import Notifications
from django.contrib.auth.models import User
from Kwitter.kweets.models import Kweet

import re

# class based views below


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


# class based view
@method_decorator(login_required, name='dispatch')
class add_kweet_view(CreateView):
    template_name = 'generic_form.htm'
    form = AddKweetForm
    model = Kweet
    fields = ['message_input']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = KwitterUser.objects.get(user=self.request.user)
        self.object.save()
        create_notification(self.object)
        return HttpResponseRedirect(reverse('home'))


def create_notification(tweet):
    notified_users = re.findall(r'@(\S*)', tweet.message_input)
    all_users = User.objects.all()
    all_usernames = [user.username for user in all_users]
    for notified_user in notified_users:
        if notified_user in all_usernames:
            receiver_user = User.objects.get(username=notified_user)
            receiver = KwitterUser.objects.get(user=receiver_user)
            Notifications.objects.create(
                kwitter_user=receiver,
                kweet=tweet,
                not_viewed=True
            )


# class based view
class kweet_detail_view(DetailView):
    template_name = 'kweet_detail.html'
    model = Kweet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # kweet = Kweet.objects.get(pk=id)
        return context




# def add_like_view(request):
#     pass


# def remove_like_view(request):
#     pass
