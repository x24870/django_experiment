from django.urls import path
from django.conf.urls import include

from .views import index, ChatRoom

app_name = 'chat'

urlpatterns = [
    path('', index, name='index'),
    # path('chatroom/', ChatRoom.as_view(), name='chat_room')
] 