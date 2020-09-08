from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostDeleteView,
    PostCreateView,
    PostUpdateView,
    UserPostListView
    )

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('user_post_list/', UserPostListView.as_view(), name='user_post_list'),
] 