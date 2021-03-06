from django.contrib import admin
from .models import Post, Label

class PoseModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated', 'timestamp']
    list_filter = ['updated', 'timestamp']
    class Meta:
        model = Post


# Register your models here.	# Register your models here.
admin.site.register(Post, PoseModelAdmin) 
admin.site.register(Label) 