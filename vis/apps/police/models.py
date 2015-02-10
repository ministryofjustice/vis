from django.db import models


class PCC(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    content = models.TextField()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug

    class Meta:
        verbose_name = u'PCC'
        verbose_name_plural = u'PCCs'
