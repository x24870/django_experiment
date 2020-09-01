from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostDeleteView

app_name = 'posts'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('update/', views.post_update, name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
] 