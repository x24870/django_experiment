from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    # ViewSet built-in functions: list, create, retrieve, update, partial_update, destroy
    queryset = Post.objects.active_post()
    serializer_class = PostSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     )

    def get_permissions(self):
        print(f'Requst action: {self.action}')
        if self.action in ('create', 'update', 'partial_update', 'destroy'):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    def list(self, request, **kwargs):
        posts = Post.objects.active_post()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, **kwargs):
        user = get_object_or_404(get_user_model(), pk=request.data.get('user'))
        post = Post.objects.create(
            title = request.data.get('title'),
            user = user,
            content = request.data.get('content'),
            draft = request.data.get('draft'),
        )
        post.label.set(request.data.get('label'))

        serializer = PostSerializer(post)
        print(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)