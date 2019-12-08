from django.urls import path

from Kwitter.kwitterusers.views import index_view, add_kweet_view, add_like_view, remove_like_view


kweetpatterns = [
    path('index/',index_view ,name='home'),
    path('addkweet/', add_kweet_view, name='addkweet'),
    path('addlike/', add_like_view,name='addlike'),
    path('removelike/',remove_like_view, name='removelike' )
]