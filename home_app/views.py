from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    return render(request,'home_app/home.html')
def form_add(request):
    return render(request,'home_app/add_movie.html')
def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        release_year = request.POST.get('release_year')
        status = True if request.POST.get('status') == 'on' else False

        # ساخت فیلم
        models.Movie.objects.create(
            title=title,
            description=description,
            genre=genre,
            release_year=release_year,
            status=status
        )

        if status: 
            models.Movies_watched.objects.create(title=title, genre=genre)
            return render(request, 'home_app/whatched.html', context={'whatchs': models.Movies_watched.objects.all()})
        else: 
            models.Unseen_movies.objects.create(title=title, genre=genre)
            return render(request, 'home_app/unseen.html', context={'whatchs': models.Unseen_movies.objects.all()})

    return render(request, 'home_app/home.html')
