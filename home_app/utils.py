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
