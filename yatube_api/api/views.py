from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets

from posts.models import Follow, Group, Post
from api.permissions import AuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        AuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        AuthorOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )

    def getting_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer) -> None:
        post = self.getting_post()
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self) -> list:
        post = self.getting_post()
        return post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'user__username')

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)

    def get_queryset(self) -> list:
        return Follow.objects.filter(user=self.request.user)
