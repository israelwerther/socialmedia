from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    urls = serializers.JSONField(read_only=True)
    user = serializers.CharField(source='user.username', read_only=True) 
    like_count = serializers.ReadOnlyField()
    dislike_count = serializers.ReadOnlyField()
    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'created_at', 'like_count', 'dislike_count', 'urls')
        # read_only_fields = ['id', 'user', 'created_at']