from rest_framework import serializers

from socialmedia.accounts.forms import UserCreationForm
from .models import User, Follow

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField(read_only=True)
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'following', 'followers', 'urls']

    def get_following(self, obj):
        following_users = Follow.objects.filter(follower=obj).select_related('following')
        following_list = [
            {
                'id': follow.following.id,
                'username': follow.following.username
            }
            for follow in following_users
        ]
        return following_list

    def get_followers(self, obj):
        followers_users = Follow.objects.filter(following=obj).select_related('follower')
        followers_list = [
            {
                'id': follow.follower.id,
                'username': follow.follower.username
            }
            for follow in followers_users
        ]
        return followers_list

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation')

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        data['password1'] = data['password']
        data['password2'] = data['password_confirmation']
        form = UserCreationForm(data=data)
        if not form.is_valid():
            raise serializers.ValidationError(form.errors)

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
