import urllib.request
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
import io
import json
from datetime import datetime
from collections import OrderedDict
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def updatedate():
    current_time = datetime.now()

    # JSON 데이터 생성

    updatedate = [{
            "model": "movies.updatedate",
            "pk": 1,
            "fields": {
                "date": str(current_time)[:19],
                }
            }]

    with open('movies/fixtures/updatedate.json', 'w', encoding='utf-8') as f:
        json.dump(updatedate, f, ensure_ascii=False, indent="\t")


def moviedata():
    API_KEY = 'cb3b78b75f8e073c2ad862fb44c113e0'
    HOST = "https://api.themoviedb.org"
    MOVIE_LIST_URI = "/3/movie/popular"
    MOVIE_INFO_URI = "/3/movie/"
    GENRE_LIST_URI = "/3/genre/movie/list"

    movie_list = []
    movie_Ids = []
    genre_list = []

    genre_request = (f'{HOST}{GENRE_LIST_URI}?api_key={API_KEY}&language=ko')
    response = urllib.request.urlopen(genre_request)
    json_str = response.read().decode('utf-8')
    json_object = json.loads(json_str)

    genre_data = json_object.get("genres")

    for data in genre_data:

        my_data = {
            "number": data.get("id"),
            "name": data.get("name")
        }

        my_genre = {
            "model": "movies.genre",
            "pk": my_data.get("number"),
            "fields": {
                "name": my_data.get("name")
            },
        }
        genre_list.append(my_genre)

    for i in range(1, 50):
        request = (f'{HOST}{MOVIE_LIST_URI}?api_key={API_KEY}&language=ko&page={i}')
        response = urllib.request.urlopen(request)
        json_str = response.read().decode('utf-8')
        json_object = json.loads(json_str)

        data_movies = (json_object.get("results"))

        for movie in data_movies:
            movie_Ids.append(movie.get("id"))

    for idx, movie_Id in enumerate(movie_Ids):
        movie_request = (f'{HOST}{MOVIE_INFO_URI}{movie_Id}?api_key={API_KEY}&language=ko&')
        response = urllib.request.urlopen(movie_request)
        json_str = response.read().decode('utf-8')
        json_object = json.loads(json_str)
    
        if json_object.get("poster_path") and json_object.get("backdrop_path"):
            if json_object.get("genres"):
                
                my_object = {
                    "model": "movies.movie",
                    "pk": idx+1,
                    "fields": {
                        "movie_id": json_object.get("id"),
                        "title": json_object.get("title"),
                        "adult": json_object.get("adult"),
                        "popularity": json_object.get("popularity"),
                        "poster_path": json_object.get("poster_path"),
                        "release_date": json_object.get("release_date"),
                        "runtime": json_object.get("runtime"),
                        "vote_average": json_object.get("vote_average"),
                        "vote_count": json_object.get("vote_count"),
                        "overview": json_object.get("overview"),
                        "genres": [json_object.get("genres")[0].get("id")],
                        "original_title": json_object.get("original_title"),
                        "backdrop_path": json_object.get("backdrop_path"),
                    }  
                }
            else:
                my_object = {
                    "model": "movies.movie",
                    "pk": idx+1,
                    "fields": {
                        "movie_id": json_object.get("id"),
                        "title": json_object.get("title"),
                        "adult": json_object.get("adult"),
                        "popularity": json_object.get("popularity"),
                        "poster_path": json_object.get("poster_path"),
                        "release_date": json_object.get("release_date"),
                        "runtime": json_object.get("runtime"),
                        "vote_average": json_object.get("vote_average"),
                        "vote_count": json_object.get("vote_count"),
                        "overview": json_object.get("overview"),
                        "genres": json_object.get("genres"),
                        "original_title": json_object.get("original_title"),
                        "backdrop_path": json_object.get("backdrop_path"),
                    }
                }
            movie_list.append(my_object)

    with open('movies/fixtures/movies.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(movie_list, ensure_ascii=False))

    with open('movies/fixtures/genres.json', 'w', encoding='UTF-8') as file:
        file.write(json.dumps(genre_list, ensure_ascii=False))



def netflix():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://m.kinolights.com/ranking/netflix')

    netflix = []

    for i in range(1, 21):  # i from 1 to 20
        title_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.title-text'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.poster-img > img'.format(i))
        title = title_element.text
        poster = img_element.get_attribute('src')

        netflix.append({
            "model": "movies.ott",
            "pk": i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "rank": i
                }
            })

    with open('movies/fixtures/netflix.json', 'w', encoding='utf-8') as f:
        json.dump(netflix, f, ensure_ascii=False, indent="\t")

    driver.quit()



def tving():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://m.kinolights.com/ranking/tving')

    tving = []

    for i in range(1, 21):  # i from 1 to 20
        title_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.title-text'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.poster-img > img'.format(i))
        title = title_element.text
        poster = img_element.get_attribute('src')

        tving.append({
            "model": "movies.ott",
            "pk": 20+i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "rank": i
                }
            })

    with open('movies/fixtures/tving.json', 'w', encoding='utf-8') as f:
        json.dump(tving, f, ensure_ascii=False, indent="\t")

    driver.quit()


def wavve():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://m.kinolights.com/ranking/wavve')

    wavve = []

    for i in range(1, 21):  # i from 1 to 20
        title_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.title-text'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.poster-img > img'.format(i))
        title = title_element.text
        poster = img_element.get_attribute('src')

        wavve.append({
            "model": "movies.ott",
            "pk": 40+i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "rank": i
                }
            })

    with open('movies/fixtures/wavve.json', 'w', encoding='utf-8') as f:
        json.dump(wavve, f, ensure_ascii=False, indent="\t")

    driver.quit()


def disney():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://m.kinolights.com/ranking/disney')

    disney = []

    for i in range(1, 21):  # i from 1 to 20
        title_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.title-text'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.poster-img > img'.format(i))
        title = title_element.text
        poster = img_element.get_attribute('src')

        disney.append({
            "model": "movies.ott",
            "pk": 60+i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "rank": i
                }
            })

    with open('movies/fixtures/disney.json', 'w', encoding='utf-8') as f:
        json.dump(disney, f, ensure_ascii=False, indent="\t")

    driver.quit()


def watcha():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://m.kinolights.com/ranking/watcha')

    watcha = []

    for i in range(1, 21):  # i from 1 to 20
        title_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.title-text'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#contents > div.contents-area > div:nth-child(1) > div > div > ul.chart-list-container.active > li:nth-child({}) > a > span.left-content-wrap > span.poster-img > img'.format(i))
        title = title_element.text
        poster = img_element.get_attribute('src')


        watcha.append({
            "model": "movies.ott",
            "pk": 80+i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "rank": i
                }
            })

    with open('movies/fixtures/watcha.json', 'w', encoding='utf-8') as f:
        json.dump(watcha, f, ensure_ascii=False, indent="\t")

    driver.quit()


def navernow():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%9E%91')

    navernow = []

    for i in range(1, 9):
        title_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.title._ellipsis > div > a'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#m_dss_movie_img{}'.format(i-1))
        genre_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(1) > dd:nth-child(2)'.format(i))
        score_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(2) > dd:nth-child(4) > span'.format(i))
        runtime_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(1) > dd:nth-child(3)'.format(i))
        date_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(2) > dd:nth-child(2)'.format(i))
        # actor_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(3) > dd > span'.format(i))
        link_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > a'.format(i))
        
        
        title = title_element.text
        poster = img_element.get_attribute('src')
        genre = genre_element.text
        score = score_element.text
        runtime = runtime_element.text
        date = date_element.text
        # actor = actor_element.text

        link_temp = link_element.get_attribute('href')
        link_parse = link_temp.split('query=')[1]
        infolink = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94+' + link_parse
        reservelink = infolink + '+%EC%83%81%EC%98%81%EC%9D%BC%EC%A0%95'

        navernow.append({
            "model": "movies.cinemanow",
            "pk": i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "genre": genre,
                "score": score,
                "runtime": runtime,
                "date": date,
                # "actor": actor,
                "info_url": infolink,
                "reserve_url": reservelink,
                }
            })

    with open('movies/fixtures/navernow.json', 'w', encoding='utf-8') as f:
        json.dump(navernow, f, ensure_ascii=False, indent="\t")

    driver.quit()



def naverupcoming():
    driver_path = '/Users/SSAFY/Downloads/chromedriver_win32/chromedriver'
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B0%9C%EB%B4%89%EC%98%88%EC%A0%95%EC%9E%91')

    naverupcoming = []

    for i in range(1, 9):
        title_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.title._ellipsis > div > a'.format(i))
        img_element = driver.find_element(By.CSS_SELECTOR, '#m_dss_movie_img{}'.format(i-1))
        genre_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(1) > dd:nth-child(2)'.format(i))
    
        runtime_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(1) > dd:nth-child(3)'.format(i))
        date_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(2) > dd:nth-child(2)'.format(i))
        # actor_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > div > div.info > dl:nth-child(3) > dd > span'.format(i))
        link_element = driver.find_element(By.CSS_SELECTOR, '#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child({}) > div.data_area > a'.format(i))
        
        
        title = title_element.text
        poster = img_element.get_attribute('src')
        genre = genre_element.text
        runtime = runtime_element.text
        date = date_element.text
        # actor = actor_element.text

        link_temp = link_element.get_attribute('href')
        link_parse = link_temp.split('query=')[1]
        infolink = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94+' + link_parse
        reservelink = infolink + '+%EC%83%81%EC%98%81%EC%9D%BC%EC%A0%95'

        naverupcoming.append({
            "model": "movies.cinemaupcoming",
            "pk": i,
            "fields": {
                "title": title,
                "poster_url": poster,
                "genre": genre,
                "runtime": runtime,
                "date": date,
                # "actor": actor,
                "info_url": infolink,
                "reserve_url": reservelink,
                }
            })

    with open('movies/fixtures/naverupcoming.json', 'w', encoding='utf-8') as f:
        json.dump(naverupcoming, f, ensure_ascii=False, indent="\t")

    driver.quit()






updatedate()
# moviedata()
netflix()
tving()
wavve()
disney()
watcha()
navernow()
naverupcoming()



'''
movies/fixtures/ 만들고 

python trans.py 

python manage.py migrate

python manage.py loaddata genres.json movies.json netflix.json tving.json wavve.json disney.json watcha.json updatedate.json navernow.json naverupcoming.json

'''