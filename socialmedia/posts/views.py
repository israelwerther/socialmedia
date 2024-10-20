from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if user in post.dislikes.all():
            post.dislikes.remove(user)

        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)

        if user in post.dislikes.all():
            post.dislikes.remove(user)
        else:
            post.dislikes.add(user)

        serializer = self.get_serializer(post)
        return Response(serializer.data)
