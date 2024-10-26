from rest_framework import serializers
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

