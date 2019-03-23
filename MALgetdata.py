import requests
from bs4 import BeautifulSoup as bs
import json

ListStatus = {'All Anime/Manga' : 7,
             'Currently Watching/Reading' : 1,
             'Completed' : 2,
             'On Hold' : 3,
             'Dropped' : 4,
             'Plan To Watch/Read' : 6}
#Input for desired data
MediaType = input('Anime/Manga : ').lower()
username = input('Username : ')
print(ListStatus)
Status = input('Type of Status : ')
url = 'https://myanimelist.net/{}list/{}?status={}'.format(MediaType,username,Status)

data = requests.get(url)
data = data.content         #Go to url and read content
soup = bs(data, 'lxml')    #Convert to BeautifulSoup object

#Read all animes/mangas as a string of list of dictionaries
samples = soup.find('table', {'class':'list-table'})['data-items']
#Convert to list of dictionaries
data = json.loads(samples)
for item in data:
  print('\n')
  print(item['{}_title'.format(MediaType)])
  print('Score : ',item['score'])
  print('URL : https://myanimelist.net{}'.format(item['{}_url'.format(MediaType)]))

