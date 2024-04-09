from django.shortcuts import render

from json import load
import json
import requests
from bs4 import BeautifulSoup


HEADERS = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
}
DOMEN = "http://tengrinews.kz"
URL = "https://tengrinews.kz/search/?text="

def get_response(url_def, headers_def=HEADERS):      
    # function to get response from server
    response = requests.get(url=url_def, headers=headers_def) # get response from server
    if response.status_code == 200:     # response status  
        src = response.content          # response content from  server
        return src                      # return response
    else:
        return f"bad response {response.status_code}"

def get_soup(response):
    # function to get soup from response
    soup = BeautifulSoup(response, 'html.parser')
    all_news = soup.find_all("div", class_="content_main_item")
    news_info = []
    for item in all_news:
        try:
            title = item.find("span", class_="content_main_item_title").find("a")
            date_time = item.find("div", class_="content_main_item_meta").find("span")
            news_url = DOMEN + item.find("span", class_="content_main_item_title").find("a").get("href")
            image = item.find("a").find("picture").find("img", class_="content_main_item_img").get("src")
        except Exception: # if exception happens during the creation of the image element code above    then the        image element will be    removed from the DOM
            information = {
            "title": title.text,
            "date_time": date_time.text.strip(),
            "image": image,
            "url": news_url
            }
        else:
            information = {
            "title": title.text,
            "date_time": date_time.text.strip(),
            "image": image,
            "url": news_url
            }
        news_info.append(information)
        
    return news_info


def parser(search):
    response = get_response(url_def=URL + search)
    soup = get_soup(response)
    with open(f"tengrinews.json", "w", encoding="UTF-8") as file:
        json.dump(soup, file, indent=4, ensure_ascii=False)

    return soup

def index(request):

    data = {
        'news': parser('Сегодня')
    }
    
    return render(request, 'main/index.html', data)

def life(request):
    data = {
        'news': parser('Забавные')
    }
    return render(request, 'main/life.html', data)
    
def sport(request):
    data = {
        'news': parser('Спорт')
    }
    return render(request, 'main/sport.html', data)
    
def travel(request):
    data = {
        'news': parser('Путешествия Страны')
    }
    return render(request, 'main/travel.html', data)
    
def music(request):
    data = {
        'news': parser('Музыка Рэп')
    }
    return render(request, 'main/music.html', data)