from django.db import models
from django.contrib.auth.models import User
import os

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)  
    poster = models.ImageField(upload_to="movies/", blank=True, null=True)

    def __str__(self):
        return self.title

    def poster_url(self):
        """برمی‌گرداند مسیر عکس اگر موجود باشد"""
        if self.poster and os.path.isfile(self.poster.path):
            return self.poster.url
        return None  # یا مسیر یک عکس پیش‌فرض
class MoviesWatched(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="whatched/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} watched"  # self.title به Movie اشاره دارد


class UnseenMovies(models.Model):
    title = models.CharField(max_length=200)

    poster = models.ImageField(upload_to="unseen/", blank=True, null=True)
    

    def __str__(self):
        return f"{self.title} not watched"

