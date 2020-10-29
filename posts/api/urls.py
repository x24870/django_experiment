from django.conf.urls import include 
from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.api import views

# DefaultRouter url reference:
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = DefaultRouter()
router.register(r'', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]