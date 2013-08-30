# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80, null=False)
    contents = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("list")


class PostForm(ModelForm):
    class Meta:
        model = Post