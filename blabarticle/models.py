from typing import Iterable
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category (models.Model):
    title = models.CharField(max_length = 256,)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class Article (models.Model):
    topic = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=500, null=False)
    status_choice = {'Sports' : 'Sports',
                     'Business' : 'Business',
                     'Politics' : 'Politics'}
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=False)
    published_category = models.CharField(max_length=256, choices=status_choice, null=True, blank=False)
    slug = models.CharField(max_length=256, null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        return super().save(self, *args, **kwargs)

    def __str__(self):
        return self.topic