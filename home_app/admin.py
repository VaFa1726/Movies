from django.contrib import admin
from .models import Movie,MoviesWatched,UnseenMovies
# Register your models here.
admin.site.register(Movie)
admin.site.register(MoviesWatched)
admin.site.register(UnseenMovies)
