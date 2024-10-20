import uuid
from django.urls import reverse
from django.db import models
from django.conf import settings

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='disliked_posts', blank=True)

    def __str__(self):
        return f'Post by {self.user.username} at {self.created_at}'
    
    @property
    def like_count(self):
        return self.likes.count()
    
    @property
    def dislike_count(self):
        return self.dislikes.count()

    @property
    def urls(self):
        return {
            "like": reverse("api:posts-like", kwargs={ "pk": self.id }),
            "dislike": reverse("api:posts-dislike", kwargs={ "pk": self.id }),
        }

    class Meta:
        ordering = ['-created_at']