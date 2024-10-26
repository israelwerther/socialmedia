from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from socialmedia.accounts.forms import UserCreationForm
from socialmedia.accounts.models import User, Follow
from socialmedia.accounts.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        follow_user = self.get_object()
        current_user = request.user

        if follow_user == current_user:
            return Response({"detail": "A user cannot follow himself."}, status=400)

        if Follow.objects.filter(follower=current_user, following=follow_user).exists():
            return Response({"detail": "You already follow this user."}, status=400)

        Follow.objects.create(follower=current_user, following=follow_user)

        return Response({"detail": "Now following this user."}, status=201)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        unfollow_user = self.get_object()
        current_user = request.user

        follow = Follow.objects.filter(follower=current_user, following=unfollow_user).first()
        if not follow:
            return Response({"detail": "You do not follow this user."}, status=400)

        follow.delete()

        # verificar pq não está aparecendo resposta ao deixar de seguir
        return Response({"detail": "Unfollowed this user."}, status=204)



class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
