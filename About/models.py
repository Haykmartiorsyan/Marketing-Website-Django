from django.db import models

# Create your models here.
class AboutBgColor(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Item Background Color"
        verbose_name_plural = "Item Background Color"


class AboutItems(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='about_items')
    color = models.ForeignKey(AboutBgColor, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "About Item"
        verbose_name_plural = "About Items"

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "$s" % self.id


class OurCustomers(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    profession = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='customers_image')
    facebook_profile = models.URLField(blank=True, null=True, default=None)
    twitter_profile = models.URLField(blank=True, null=True, default=None)
    linkedin_profile = models.URLField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Our Customers"

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "$s" % self.id
