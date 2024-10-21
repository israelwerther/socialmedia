from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField(read_only=True)
    follower = serializers.StringRelatedField()
    followed = serializers.StringRelatedField()

    class Meta:
        model = Follow
        fields = ['follower', 'followed', 'created_at', 'urls']
