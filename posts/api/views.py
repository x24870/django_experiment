from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.active_post()
    serializer_class = PostSerializer
    permission_classes = (
        IsAuthenticated,
        )