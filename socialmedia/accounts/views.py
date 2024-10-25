from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from socialmedia.accounts.forms import UserCreationForm
from socialmedia.accounts.models import User
from socialmedia.accounts.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        follow = self.get_object()
        current_user = request.user

        if follow == current_user:
            return Response({"detail": "A user cannot follow himself."}, status=400)

        if current_user.following.filter(id=follow.id).exists():
            return Response({"detail": "You already follow this user."}, status=400)

        current_user.following.add(follow)

        serializer = self.get_serializer(current_user)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        unfollow = self.get_object()
        current_user = request.user

        if not current_user.following.filter(id=unfollow.id).exists():
            return Response({"detail": "You do not follow this user."}, status=400)

        current_user.following.remove(unfollow)

        serializer = self.get_serializer(current_user)
        return Response(serializer.data)


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
