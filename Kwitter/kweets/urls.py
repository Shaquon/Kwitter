from django.urls import path
from Kwitter.kweets.views import index_view, add_kweet_view, kweet_detail_view


urlpatterns = [
    path('home/', index_view, name='home'),
    path('addkweet/', add_kweet_view, name='addkweet'),
    path('kweetdetail/<int:id>/', kweet_detail_view, name='kweetdetail')
    # path('addlike/', add_like_view, name='addlike'),
    # path('removelike/',remove_like_view, name='removelike')
]
