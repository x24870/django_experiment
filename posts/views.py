from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.utils import timezone
from django.urls import reverse_lazy
from django import forms
from django.contrib import messages

from .models import Post
from .forms import PostFrom

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

class PostCreateView(CreateView):
    form_class = PostFrom
    template_name = 'posts/post_create.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['title'] = 'Default Title'
        return initial

class PostUpdateView(UpdateView):
    form_class = PostFrom
    template_name = 'posts/post_update.html'

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = PostFrom(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # NOTE: If following 2 condition is met, form.save_m2m() is required.
            # 1. Using form.save(commit=False)
            # 2. There is ManyToMany field in the model
            form.save_m2m()
            messages.success(request, 'Update post successfully.')
            return redirect(post.get_absolute_url())
        return render(request, self.template_name, {'from': form})
        messages.error(request, 'Update post fail!\n Please check your data.')

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = PostFrom(instance=post)
        context = {'form': form}
        return render(request, self.template_name, context)
        
