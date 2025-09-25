from django.shortcuts import render
from . import models
from . import utils
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

    movie.delete()

    return redirect('movies')


def random_movie(request):
    movie_list = list(models.UnseenMovies.objects.all())

    if movie_list:
        mov = utils.choice_random(movie_list)
    else:
        mov = None
    return render(request, 'home_app/visit/random_movie.html', {'movie': mov})

from django.shortcuts import render
import random
from .utils import get_series_list  # فرض کردیم تابع بالا در فایل utils.py هست

def random_series(request):
    series_list = get_series_list()  # گرفتن لیست سریال‌ها
    selected_series = random.choice(series_list) if series_list else None

    return render(request, 'home_app/visit/random_series.html', {'series': selected_series})
import random
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

# تابع استخراج سریال‌ها
def get_series_list():
    url = 'https://upside.ir/%D8%A8%D9%87%D8%AA%D8%B1%DB%8C%D9%86-%D8%B3%D8%B1%DB%8C%D8%A7%D9%84-%D9%87%D8%A7%DB%8C-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C/'
    response = requests.get(url)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    series_list = []

    titles = soup.find_all('h2')
    for title_tag in titles:
        main_title = title_tag.get_text(strip=True)
        
        table = title_tag.find_next('table')
        genre = year = seasons = imdb = episodes = avg_time = ''
        if table:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    header = cols[0].get_text(strip=True)
                    value = cols[1].get_text(strip=True)
                    if 'ژانر' in header:
                        genre = value
                    elif 'سال ساخت' in header:
                        year = value
                    elif 'تعداد فصل' in header:
                        seasons = value
                    elif 'IMDB' in header:
                        imdb = value
                    elif 'تعداد قسمت' in header:
                        episodes = value
                    elif 'متوسط زمان' in header:
                        avg_time = value

        # توضیحات
        desc_div = title_tag.find_next('div', class_='avia_textblock')
        description = ''
        if desc_div:
            paragraphs = desc_div.find_all('p')
            description = "\n".join(p.get_text(strip=True) for p in paragraphs)

        # لینک سریال
        link_tag = title_tag.find('a')
        link = link_tag['href'] if link_tag else None

        series_list.append({
            'title': main_title,
            'genre': genre,
            'year': year,
            'seasons': seasons,
            'episodes': episodes,
            'avg_time': avg_time,
            'imdb': imdb,
            'description': description,
            'link': link
        })

    return series_list

def choice_random(series_list):
    return random.choice(series_list) if series_list else None

def random_series_view(request):
    series_list = get_series_list()
    random_series = choice_random(series_list)
    context = {'series': random_series}
    return render(request, 'random_series.html', context)
