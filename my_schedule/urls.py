from django.urls import path
from . import views

app_name = 'my_schedule'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
] 