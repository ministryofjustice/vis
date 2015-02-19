from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PCC(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pcc_detail', kwargs={'slug': self.slug})

    def natural_key(self):
        return self.slug

    class Meta:
        verbose_name = u'PCC'
        verbose_name_plural = u'PCCs'

