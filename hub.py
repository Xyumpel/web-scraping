import requests
from bs4 import BeautifulSoup
from pprint import pprint
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
response = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(response.text, features = 'html.parser')
articles = soup.find_all('article')
for article in articles:
    time = article.find('time datetime', class_ = 'tm-article-snippet__dateitem-published')
    header = article.find('h2', class_ = "tm-article-snippet__title tm-article-snippet__title_h2")
    hubs = article.find_all('span', class_ = 'tm-article-snippet__hubs-item')
    hubs = set([hub.text for hub in hubs])
    title = article.find('a', class_='post__title_link')
    link = header.text.find('a')
    if KEYWORDS & hubs:
         print('<{}>-<{}>-<{}>'.format(time.text, title.text, link.text))

