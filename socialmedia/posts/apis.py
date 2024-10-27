from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsPostOwner
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        if not user.is_superuser:
            queryset = queryset.filter(
                Q(user__in=user.following.values('following')) | Q(user=user)
            ).order_by('-created_at')
        
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(content__icontains=search_query)
            )

        return queryset

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated, IsPostOwner]
        return super().get_permissions()

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

    @action(detail=False, methods=['get'])
    def feed(self, request):        
        posts = self.get_queryset()
        page = self.paginate_queryset(posts)

        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
