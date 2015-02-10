from django.db import models


class GlossaryItem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug


class Helpline(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    phone = models.CharField(max_length=18)
    url = models.URLField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.name
