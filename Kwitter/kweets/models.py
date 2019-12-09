from django.db import models 
from django.utils import timezone
from Kwitter.kwitterusers import KwitterUser


class Kweet(models.Model):
    user = models.ForeignKey(KwitterUser, on_delete=models.CASCADE, blank=True, null=True)
    message_body = models.CharField(max_length=250)
    post_time = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(KwitterUser, related_name='likes')

    def __self__(self):
        return self.message_body



