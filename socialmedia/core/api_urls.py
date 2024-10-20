# socialmedia/posts/api_urls.py
from rest_framework.routers import DefaultRouter
from socialmedia.posts.views import PostViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
app_name = 'api'
urlpatterns = router.urls
