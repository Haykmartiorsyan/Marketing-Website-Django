from django.db import models


# Create your models here.
class CaseCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name.replace(' ', '_')

    class Meta:
        verbose_name = "Case Category"
        verbose_name_plural = "Cases Categories"


class CaseItems(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='case_images')
    category = models.ForeignKey(CaseCategory, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    def __unicode__(self):
        return self.category.replace(' ', '_')

    class Meta:
        verbose_name = "Case Item"
        verbose_name_plural = "Cases Items"