from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy

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

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')

    def get(self, *args, **kwargs):
        raise Http404

def post_create(request):
    return HttpResponse("<h1>Retrun from post_create</h1>")

def post_update(request):
    return HttpResponse("<h1>Retrun from post_upadte</h1>")
