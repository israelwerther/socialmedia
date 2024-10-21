from django.conf import settings
from django.db import models
from django.urls import reverse

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"
    
    @property
    def urls(self):
        return {
            "follow": reverse("api:followers-follow", kwargs={"pk": self.followed.id}),
            "unfollow": reverse("api:followers-unfollow", kwargs={"pk": self.followed.id}),
        }
