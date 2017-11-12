from django.db import models


# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='slider_image')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "$s" % self.id


class Testimonials(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='testimonial_image')
    profession = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return "$s" % self.id