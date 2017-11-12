from django.db import models


# Create your models here.
class ServiceBgColor(models.Model):
    index = models.IntegerField(default=1)

    def __str__(self):
        return "%s" % self.index

    class Meta:
        verbose_name = "Item Background Color"
        verbose_name_plural = "Items Background Colors"


class ServiceItems(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    short_description = models.TextField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='about_items')
    color = models.ForeignKey(ServiceBgColor, blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Service Item"
        verbose_name_plural = "Services Items"

    def __str__(self):
        return "%s" % self.title

    def __unicode__(self):
        return "$s" % self.id