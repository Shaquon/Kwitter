from django.urls import path
from Kwitter.notifications.views import notification_view


urlpatterns = [
    path('notifications/', notification_view, name='notifications')
]
