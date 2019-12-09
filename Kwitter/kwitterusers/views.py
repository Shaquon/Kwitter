from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout

from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet
from Kwitter.kwitterusers.forms import AddUserForm


def user_profile_view(request, id):
    html = "user.htm"

    user = request.user

    kwitteruser = KwitterUser.objects.get(pk=id)

    kweets = Kweet.objects.filter(user=kwitteruser)[::-1]

    kweet_count = len(kweets)

    follow_count = len(kwitteruser.followed.all())

    if user.is_authenticated:
        loggedin_user = KwitterUser.objects.get(user=user)
        is_followed = loggedin_user.followed.filter(
            pk=kwitteruser.pk).exists()
        is_my_user_page = loggedin_user.id == kwitteruser.id

        return render(request, html, {
            'kwitteruser': kwitteruser,
            'kweets': kweets,
            'is_followed': is_followed,
            'is_my_user_page': is_my_user_page,
            'kweet_count': kweet_count,
            'followcount': follow_count
        })


def follow_user_view(request, id):
    user = request.user
    kwitteruser = KwitterUser.objects.get(user=user)
    user_followed = KwitterUser.objects.get(pk=id)
    kwitteruser.followed.add(user_followed)
    kwitteruser.save()
    return HttpResponseRedirect(reverse('userdetail', args=(id,)))


def unfollow_user_view(request, id):
    user = request.user
    kwitteruser = KwitterUser.objects.get(user=user)
    user_unfollowed = KwitterUser.objects.get(pk=id)
    if kwitteruser.id == user_unfollowed.id:
        return HttpResponseRedirect(reverse('userdetail', args=(id,)))
    kwitteruser.followed.remove(user_unfollowed)
    kwitteruser.save()
    return HttpResponseRedirect(reverse('userdetail', args=(id,)))

    # def all_users(request):
    #     html = 'all_users.htm'

    #     users = KwitterUser.objects.all()

    #     return render(request, html, {'users': users})
