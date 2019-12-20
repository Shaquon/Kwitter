"""Kwitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Kwitter.authentication.urls import urlpatterns as authurls
from Kwitter.kweets.urls import urlpatterns as kweeturls
from Kwitter.kwitterusers.urls import urlpatterns as kwitteruserurls
from Kwitter.notifications.urls import urlpatterns as notificationurls

from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet
from Kwitter.notifications.models import Notifications


admin.site.register(KwitterUser)
admin.site.register(Kweet)
admin.site.register(Notifications)

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += authurls

urlpatterns += notificationurls

urlpatterns += kweeturls

urlpatterns += kwitteruserurls
