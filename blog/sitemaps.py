from django.contrib.sitemaps import Sitemap

from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    def items(self):
        return Post.objects.filter(published=True)
    def lastmod(self, obj):
        return obj.published_date