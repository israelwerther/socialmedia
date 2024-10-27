from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from socialmedia.accounts.apis import UserViewSet
from socialmedia.posts.apis import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

app_name = 'api'

schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version='v1',
        description="API - Mini Tweeter",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]