import random
import requests
from bs4 import BeautifulSoup
def choice_random(list_movie):
    movie=random.choice(list_movie)
    return movie


def get_series_list():
    url = 'https://www.technolife.com/blog/best-series-of-all-time/'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"خطا در دریافت صفحه! وضعیت: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    toc_items = soup.select('.toc__listItem a')

    if not toc_items:
        print("هیچ آیتمی پیدا نشد! بررسی کن کلاس CSS درست باشد.")
        return []

    series_list = [item.get_text(strip=True) for item in toc_items]
    return series_list
import random
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

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

# View برای نمایش سریال تصادفی
def random_series_view(request):
    series_list = get_series_list()
    random_series = choice_random(series_list)
    context = {'series': random_series}
    return render(request, 'random_series.html', context)
