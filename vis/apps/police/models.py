from django.db import models
from django.contrib.auth.models import User


class PCC(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return self.slug

    class Meta:
        verbose_name = u'PCC'
        verbose_name_plural = u'PCCs'

