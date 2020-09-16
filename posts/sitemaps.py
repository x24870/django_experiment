from django.contrib.sitemaps import Sitemap
from posts.models import Post

class PostSitemap(Sitemap):
    priority = 0.5
    changefreq = "never"

    def items(self):
        return Post.objects.active_post()

    def lastmod(self, obj):
        return obj.updated