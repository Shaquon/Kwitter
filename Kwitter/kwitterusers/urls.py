from django.urls import path

from Kwitter.kwitterusers.views import unfollow_user_view, follow_user_view, user_detail_view, users_list_view


urlpatterns = [
    path('user/<int:id>/', user_detail_view, name='userdetail'),
    path('follow/<int:id>/', follow_user_view, name='addkweet'),
    path('unfollow/<int:id>/', unfollow_user_view, name='unfollow'),
    path('userslist/', users_list_view, name='userslist')
]
