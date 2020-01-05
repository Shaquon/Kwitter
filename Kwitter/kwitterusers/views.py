from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout

from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet

from django.views.generic import ListView
from django.views.generic.detail import DetailView

# from Kwitter.kwitterusers.forms import NewUserForm


# @login_required
# def user_profile_view(request, id):
#     html = "user.htm"

#     user = request.user

#     kwitteruser = KwitterUser.objects.get(pk=id)

#     kweets = Kweet.objects.filter(user=kwitteruser)[::-1]

#     kweet_count = len(kweets)

#     follow_count = len(kwitteruser.followers.all())

#     if user.is_authenticated:
#         loggedin_user = KwitterUser.objects.get(user=user)
#         is_followed = loggedin_user.followers.filter(
#             pk=kwitteruser.pk).exists()
#         is_my_user_page = loggedin_user.id == kwitteruser.id

#         return render(request, html, {
#             'kwitteruser': kwitteruser,
#             'kweets': kweets,
#             'is_followed': is_followed,
#             'is_my_user_page': is_my_user_page,
#             'kweet_count': kweet_count,
#             'followcount': follow_count
#         })

class user_detail_view(DetailView):
    model = KwitterUser
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def user_detail_view(request, id):
#     html = 'user_detail.htm'

#     kwitteruser = KwitterUser.objects.get(pk=id)

#     kweets = Kweet.objects.filter(user=kwitteruser)[::-1]

#     kweetcount = len(kweets)

#     followcount = len(kwitteruser.followers.all())

#     is_my_user_page = False

#     is_followed = False

#     if request.user.is_authenticated:
#         loggedinuser = KwitterUser.objects.get(user=request.user)

#         is_followed = loggedinuser.followers.filter(pk=kwitteruser.pk).exists()

#         is_my_user_page = loggedinuser.id == kwitteruser.id

#     return render(request, html, {
#         'kwitteruser': kwitteruser,
#         'kweets': kweets,
#         'is_followed': is_followed,
#         'is_my_user_page': is_my_user_page,
#         'kweetcount': kweetcount,
#         'followcount': followcount})


# class based view
class users_list_view(ListView):
    model = KwitterUser
    template_name = "kwitteruser_list.html"

# def users_list_view(request):
#     html = 'userslist.htm'

#     users = KwitterUser.objects.all()

#     return render(request, html, {'users': users})


@login_required
def follow_user_view(request, id):
    user = request.user
    kwitteruser = KwitterUser.objects.get(user=user)

    user_followed = KwitterUser.objects.get(pk=id)

    kwitteruser.followers.add(user_followed)
    kwitteruser.save()
    return HttpResponseRedirect(reverse('userdetail', args=(id,)))


@login_required
def unfollow_user_view(request, id):
    user = request.user
    kwitteruser = KwitterUser.objects.get(user=user)
    user_unfollowed = KwitterUser.objects.get(pk=id)
    if kwitteruser.id == user_unfollowed.id:
        return HttpResponseRedirect(reverse('userdetail', args=(id,)))
    kwitteruser.followers.remove(user_unfollowed)
    kwitteruser.save()
    return HttpResponseRedirect(reverse('userdetail', args=(id,)))
