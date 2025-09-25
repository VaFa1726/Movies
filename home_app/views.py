from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    return render(request,'home_app/home.html')
def form_add(request):
    return render(request,'home_app/add_movie.html')
from django.shortcuts import redirect

def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        poster = request.FILES.get('poster')
        status = True if request.POST.get('status') == 'on' else False

        release_year = int(release_year) if release_year else None

        movie, created = models.Movie.objects.get_or_create(
            title=title,
            defaults={
                'description': description,
                'genre': genre,
                'release_year': release_year,
                'poster': poster,
                'status': status,
            }
        )

        if created:  
            if status:
                models.MoviesWatched.objects.create(title=movie, poster=poster)
                return redirect('whatched')   
            else:
                models.UnseenMovies.objects.create(title=movie, poster=poster)
                return redirect('unseen')    
        else:
            return render(request, 'home_app/add_movie.html', {'error': 'این فیلم قبلاً اضافه شده است.'})

    return render(request, 'home_app/add_movie.html')


def movies(request):
    return render(request,'home_app/visit/movies.html',context={'movies':models.Movie.objects.all()})
def whatched(request):
    return render(request,'home_app/visit/whatched.html',context={'movies':models.MoviesWatched.objects.all()})
def unseen(request):
    return render(request,'home_app/visit/unseen.html',context={'movies':models.UnseenMovies.objects.all()})
from django.shortcuts import get_object_or_404, redirect

def delete_movie(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id)

    models.MoviesWatched.objects.filter(title=movie).delete()
    models.UnseenMovies.objects.filter(title=movie).delete()

    # حالا خود فیلم رو حذف کن
    movie.delete()

    return redirect('movies')
