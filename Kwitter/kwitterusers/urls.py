from django.urls import path

from Kwitter.kwitterusers.views import user_profile_view, unfollow_user_view, follow_user_view


urlpatterns = [
    path('profile/', user_profile_view, name='profile'),
    path('follow/', follow_user_view, name='addkweet'),
    path('unfollow', unfollow_user_view, name='unfollow')
]