from django.contrib.sitemaps.views import sitemap
from . import sitemaps

from django.urls import path
from .sitemaps import PostSitemap

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
    path('sitemap.xml', sitemap, {'sitemaps': {'posts': PostSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
] 