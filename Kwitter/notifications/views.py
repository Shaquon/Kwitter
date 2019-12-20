from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.notifications.models import Notifications


@login_required
def notification_view(request):
    html = "notifications.htm"

    user = request.user

    kwitteruser = KwitterUser.objects.get(user=user)

    notifications = Notifications.objects.filter(kwitter_user=kwitteruser)

    new_notifications = [
        notification for notification in notifications
        if notification.not_viewed][::-1]

    for new_notification in new_notifications:
        new_notification.not_viewed = False
        new_notification.save()

    return render(request, html, {
        'new_notifications': new_notifications,
        'kwitteruser': kwitteruser
    })
