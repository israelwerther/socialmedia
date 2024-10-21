# socialmedia/posts/api_urls.py
from rest_framework.routers import DefaultRouter
from socialmedia.followers.views import FollowViewSet
from socialmedia.posts.views import PostViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('followers', FollowViewSet, basename='followers')

app_name = 'api'
urlpatterns = router.urls
