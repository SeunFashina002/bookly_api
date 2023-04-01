from unicodedata import category
from django.db import models


from datetime import datetime


# Create your models here.

class BooksCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.URLField()
    alt = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    cover_image = models.URLField()
    alt = models.CharField(max_length=200, default='')
    book_url = models.URLField()
    category = models.ManyToManyField(BooksCategory)
    created_at = models.DateTimeField(auto_now_add=True)

class FeaturedBooks(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    cover_image = models.URLField()
    alt = models.CharField(max_length=200, default='')
    book_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


