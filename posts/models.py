from django.db import models
from django.shortcuts import reverse
from django.conf import settings

class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PostManager(models.Manager):
    def user_post(self, user):
        return super(PostManager, self).filter(user=user)

class Post(models.Model):
    title = models.CharField(max_length=120, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField(blank=True)
    draft = models.BooleanField(default=False, blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    label = models.ManyToManyField(Label)

    objects = PostManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.pk})

