from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField(read_only=True)
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'following', 'followers', 'urls']

    def get_following(self, obj):
        following_users = obj.following.all()
        following_list = []

        for user in following_users:
            following_list.append({
                'id': user.id,
                'username': user.username
            })

        return following_list

    def get_followers(self, obj):
        followers_users = obj.followers.all()
        followers_list = []

        for user in followers_users:
            followers_list.append({
                'id': user.id,
                'username': user.username
            })

        return followers_list

