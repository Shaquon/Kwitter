from django.urls import path
from Kwitter.kweets.views import add_kweet_view, kweet_detail_view


urlpatterns = [
    path('addkweet/', add_kweet_view, name='addkweet'),
    path('kweetdetail', kweet_detail_view, name='kweetdetail'),
    # path('addlike/', add_like_view, name='addlike'),
    # path('removelike/',remove_like_view, name='removelike')
]
