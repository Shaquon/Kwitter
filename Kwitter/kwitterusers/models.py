from django.db import models
from django.contrib.auth.models import User


class KwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username
