from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register(r'v1/posts/[?P<post_id>\d+]/comments', CommentViewSet, basename='comments')
router.register('v1/groups', GroupViewSet)
router.register('v1/follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
