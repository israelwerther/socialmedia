import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.username
    
    @property
    def urls(self):
        return {
            "follow": reverse("api:users-follow", kwargs={ "pk": self.id }),
            "unfollow": reverse("api:users-unfollow", kwargs={ "pk": self.id }),
        }
