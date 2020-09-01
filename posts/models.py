from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    label = models.ManyToManyField(Label)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

