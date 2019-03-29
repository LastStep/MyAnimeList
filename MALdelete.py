import requests
from bs4 import BeautifulSoup as bs
import MyAnimeList.MALsearch as search

def run(login = None):
  login_page = 'https://myanimelist.net/login.php?from=%2F'
  payload = {'user_name':'USERNAME',
           'password':'PASSWORD',
           'cookie':1,
           'sublogin':'Login',
           'submit':1,
           }
  headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

  Mediaid, MediaType, Search = search.run()
  url = 'https://myanimelist.net/ownlist/{}/{}/delete'.format(MediaType, Mediaid)

  with requests.Session() as req:
    code = req.get(login_page)
    soup = bs(code.content, 'lxml')
    payload['csrf_token'] = soup.find('meta', attrs={'name':'csrf_token'})['content']
    if login is None:
     login = req.post(login_page, data=payload, headers=headers)

    req.post(url, {'csrf_token': payload['csrf_token']})
    print('Deleted : {}'.format(Search).title())

if __name__ == '__main__':
  run()
