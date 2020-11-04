from django.urls import re_path

from .consumers import ChatComsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatComsumer.as_asgi())
]