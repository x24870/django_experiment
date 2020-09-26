from posts.models import Post
from posts.api.serializers import PostSerializer

from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.active_post()
    serializer_class = PostSerializer