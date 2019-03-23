import requests
from bs4 import BeautifulSoup as bs

MediaType = input('Anime/Manga : ').lower()
Search = input('Search : ')

url = 'https://myanimelist.net/{}.php?q='.format(MediaType)+Search

data = requests.get(url)
data = data.content         #Go to url and read content
soup = bs(data, 'lxml')    #Convert to BeautifulSoup object
if MediaType == 'anime':
  search_url = soup.find('a', {'class':'hoverinfo_trigger fw-b fl-l'})['href']
else:
    search_url = soup.find('a', {'class':'hoverinfo_trigger fw-b'})['href']
print('\n')
print('URL : ',search_url)
Mediaid = search_url.split('/')[4]
print('\n')
print('{} id : '.format(MediaType.title()),Mediaid)

