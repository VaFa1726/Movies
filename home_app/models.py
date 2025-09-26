# models.py - اپ فیلم‌ها
from django.db import models
from django.conf import settings
import os

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)  
    poster = models.ImageField(upload_to="movies/", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class MoviesWatched(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="watched/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} watched by"

class UnseenMovies(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to="unseen/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} not watched"