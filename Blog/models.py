from django.db import models
from django.conf import settings

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Posts Categories"

class BlogPosts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='blog_images')
    category = models.ForeignKey(PostCategory, blank=True, null=True, default=None)
    tag = models.CharField(max_length=32, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "$s" % self.id

    def get_absolute_url(self):
        return "%s" % self.id

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


class PostComment(models.Model):
    post = models.ForeignKey(BlogPosts, related_name='comments', blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=64, blank=True, null=True)
    message = models.TextField()
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Post Comment"
        verbose_name_plural = "Posts Comments"