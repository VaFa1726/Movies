from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)  

    poster = models.ImageField(upload_to="movies/", blank=True, null=True)


    def __str__(self):
        return self.title
class Movies_watched(models.Model):
    title=models.CharField(max_length=225)
    genre=models.CharField(max_length=100,blank=True)
class Unseen_movies(models.Model):
    title=models.CharField(max_length=225)
    genre=models.CharField(max_length=100,blank=True)
    
