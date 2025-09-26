from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form_add/', views.form_add, name='form_add'),
    path('add_movie/', views.add_movie, name='add_movie'), 
    path('movies/', views.movies, name='movies'),
    path('whatched/', views.whatched, name='whatched'),
    path('unseen/', views.unseen, name='unseen'),
    path('random/',views.random_movie,name='random_movie'),
    path('random/',views.random_movie,name='random_movie_from_mylist'),
    path('advanced/',views.random_series_view,name='Advanced'),
    path('all_movie/',views.all_and_random_series_view,name='all'),
    path('search/', views.search_view, name='search_results'), 
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'), 
]
