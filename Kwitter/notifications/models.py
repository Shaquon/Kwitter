from django.db import models
from Kwitter.kwitterusers.models import KwitterUser
from Kwitter.kweets.models import Kweet


class Notifications(models.Model):
    kweet = models.ForeignKey(
        Kweet, related_name='notification_kweet',
        on_delete=models.CASCADE)
    kwitter_user = models.ForeignKey(KwitterUser, related_name='notification_user', on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"to:{self.kwitter_user} - {self.tweet.message_input} - from: {self.tweet.kwitter_user.user}"