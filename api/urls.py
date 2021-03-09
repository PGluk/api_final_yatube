from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
)

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='post')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')
v1_router.register('group', GroupViewSet, basename='group')
v1_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
