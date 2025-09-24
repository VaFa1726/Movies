from django.contrib import admin
from .models import Movie,Movies_watched,Unseen_movies
# Register your models here.
admin.site.register(Movie)
admin.site.register(Movies_watched)
admin.site.register(Unseen_movies)
