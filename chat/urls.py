from django.urls import path
from django.conf.urls import include

from .views import home_page, ChatRoom

app_name = 'chat'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('chatroom/', ChatRoom.as_view(), name='chat_room')
] 