import requests
from bs4 import BeautifulSoup as bs

def run():
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

  if __name__ == '__main__':
    return search_url, MediaType
  else:
    Mediaid = search_url.split('/')[4]
    return Mediaid, MediaType, Search

if __name__ == '__main__':
  search_url, MediaType = run()
  print('URL : ', search_url)
  Mediaid = search_url.split('/')[4]
  print('{} id : '.format(MediaType.title()), Mediaid)



