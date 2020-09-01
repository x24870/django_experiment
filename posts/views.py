from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all()
    template_name = 'posts/post_list.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['currentTime'] = timezone.now()
        return context

    # def get_object(self):
    #     # Everytime get this object, set the updated field to current time
    #     obj = super().get_object()
    #     obj.updated = timezone.now()
    #     obj.save()
    #     return obj

def post_create(request):
    return HttpResponse("<h1>Retrun from post_create</h1>")

def post_update(request):
    return HttpResponse("<h1>Retrun from post_upadte</h1>")

def post_delete(request):
    return HttpResponse("<h1>Retrun from post_delete</h1>")