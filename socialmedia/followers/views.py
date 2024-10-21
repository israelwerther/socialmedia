from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from socialmedia.followers.serializers import FollowSerializer
from .models import Follow

User = get_user_model()

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        followed_user = get_object_or_404(User, pk=pk)
        follower_user = request.user

        if follower_user.following.filter(followed=followed_user).exists():
            return Response({"message": "Already following this user."})

        Follow.objects.create(follower=follower_user, followed=followed_user)
        return Response({"message": "Followed successfully."})

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        followed_user = get_object_or_404(User, pk=pk)
        follower_user = request.user

        follow_instance = Follow.objects.filter(follower=follower_user, followed=followed_user).first()
        if follow_instance:
            follow_instance.delete()
            return Response({"message": "Unfollowed successfully."})

        return Response({"message": "You are not following this user."})
