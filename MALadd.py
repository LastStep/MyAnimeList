import requests
from bs4 import BeautifulSoup as bs
import MyAnimeList.MALsearch as search
import MyAnimeList.MALdelete as delete

def run(login = None):
  login_page = 'https://myanimelist.net/login.php?from=%2F'
  payload = {'user_name':'USERNAME',
           'password':'PASSWORD',
           'cookie':1,
           'sublogin':'Login',
           'submit':1,
           }
  headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

 ListStatus = {
               'Currently Watching/Reading' : 1,
               'Completed' : 2,
               'On Hold' : 3,
               'Dropped' : 4,
               'Plan To Watch/Read' : 6
               }

  Mediaid, MediaType, Search = search.run()
  url = 'https://myanimelist.net/ownlist/{}/add'.format(MediaType)
  Score = input('Score (0 for None) : ')
  print(ListStatus)
  Status = input('Type of Status : ')

  with requests.Session() as req:
    code = req.get(login_page)
    soup = bs(code.content, 'lxml')
    payload['csrf_token'] = soup.find('meta', attrs={'name':'csrf_token'})['content']
    if login is None:
     login = req.post(login_page, data=payload, headers=headers)

    if MediaType == 'manga':
      add_form = {
                    'queryTitle':'',
                    'entry_id': 0,
                    'manga_id':Mediaid,
                    'aeps':26,
                    'astatus':Score,
                    'add_manga[status]':Status,
                    'add_manga[num_read_volumes]':'',
                    'last_completed_vol': '',
                    'add_manga[num_read_chapters]': '',
                    'add_manga[score]':'',
                    'add_manga[start_date][month]':'',
                    'add_manga[start_date][day]':'',
                    'add_manga[start_date][year]':'',
                    'add_manga[finish_date][month]':'',
                    'add_manga[finish_date][day]':'',
                    'add_manga[finish_date][year]':'',
                    'add_manga[tags]':'',
                    'add_manga[priority]':0,
                    'add_manga[storage_type]':'',
                    'add_manga[num_retail_volumes]':'',
                    'add_manga[num_read_times]':'',
                    'add_manga[reread_value]':'',
                    'add_manga[comments]':'',
                    'add_manga[is_asked_to_discuss]':0,
                    'add_manga[sns_post_type]':0,
                    'submitIt':0,
                    "csrf_token":payload['csrf_token']
                }
    elif MediaType == 'anime':
      add_form = {
                    'queryTitle': '',
                    'anime_id': Mediaid,
                    'aeps': 26,
                    'astatus': Score,
                    'add_anime[status]': Status,
                    'add_anime[num_watched_episodes]': '',
                    'add_anime[score]': '',
                    'add_anime[start_date][month]': '',
                    'add_anime[start_date][day]': '',
                    'add_anime[start_date][year]': '',
                    'add_anime[finish_date][month]': '',
                    'add_anime[finish_date][day]': '',
                    'add_anime[finish_date][year]': '',
                    'add_anime[tags]': '',
                    'add_anime[priority]': 0,
                    'add_anime[storage_type]': '',
                    'add_anime[storage_value]': '',
                    'add_anime[num_watched_times]': '',
                    'add_anime[rewatch_value]': '',
                    'add_anime[comments]': '',
                    'add_anime[is_asked_to_discuss]': 0,
                    'add_anime[sns_post_type]': 0,
                    'submitIt': 0,
                    "csrf_token": payload['csrf_token']
                }

    req.post(url, add_form)
    print('Added {}'.format(Search).title())

if __name__ == '__main__':
  run()
