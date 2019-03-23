import requests
from bs4 import BeautifulSoup as bs

#login
login_page = 'https://myanimelist.net/login.php?from=%2F'
payload = {'user_name':'',
         'password':'',
         'cookie':1,
         'sublogin':'Login',
         'submit':1,
         }
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

ListStatus = {'All Anime/Manga' : 7,
             'Currently Watching/Reading' : 1,
             'Completed' : 2,
             'On Hold' : 3,
             'Dropped' : 4,
             'Plan To Watch/Read' : 6}

MediaType = input('Anime/Manga : ').lower()
url = 'https://myanimelist.net/ownlist/{}/{}/edit?hideLayout'.format(
MediaType,input('Anime/Manga id : '))
Score = input('Score : ')
print(ListStatus)
Status = input('Type of Status : ')

with requests.Session() as req:
  code = req.get(login_page)
  soup = bs(code.content, 'lxml')
  payload['csrf_token'] = soup.find('meta', attrs={'name':'csrf_token'})['content']

  login = req.post(login_page, data=payload, headers=headers)

  edit = req.get(url)
  soup = bs(edit.content, 'lxml')
  form = soup.find(id='main-form')
  form_inputs = form.find_all('input')

  if MediaType == 'manga':
    edit_form = {
                    'entry_id': form_inputs[0]['value'],
                    'manga_id': form_inputs[1]['value'],
                    'add_manga[status]': Status, #form_inputs[3]['value']
                    'add_manga[is_rereading]': form_inputs[4]['value'],
                    'add_manga[num_read_volumes]': form_inputs[5]['value'],
                    'last_completed_vol':form_inputs[6]['value'] ,
                    'add_manga[num_read_chapters]': form_inputs[7]['value'],
                    'add_manga[score]': Score,
                    'add_manga[start_date][month]':'' ,
                    'add_manga[start_date][day]':'' ,
                    'add_manga[start_date][year]':'' ,
                    'add_manga[finish_date][month]':'' ,
                    'add_manga[finish_date][day]':'' ,
                    'add_manga[finish_date][year]':'' ,
                    'add_manga[tags]':'' ,
                    'add_manga[priority]': 0,
                    'add_manga[storage_type]':'' ,
                    'add_manga[num_retail_volumes]': form_inputs[10]['value'],
                    'add_manga[num_read_times]': form_inputs[11]['value'],
                    'add_manga[reread_value]':'' ,
                    'add_manga[comments]':'' ,
                    'add_manga[is_asked_to_discuss]': 0,
                    'add_manga[sns_post_type]': 0,
                    'submitIt': 0,
                    'csrf_token': payload['csrf_token']
                 }
  else:
    edit_form = {
                    'anime_id': form_inputs[0]['value'],
                    'aeps': form_inputs[1]['value'],
                    'astatus': form_inputs[2]['value'],
                    'add_anime[status]': Status,
                    'add_anime[num_watched_episodes]': form_inputs[4]['value'],
                    'add_anime[score]': Score,
                    'add_anime[start_date][month]':'',
                    'add_anime[start_date][day]': '',
                    'add_anime[start_date][year]':'',
                    'add_anime[finish_date][month]': 6,
                    'add_anime[finish_date][day]': 7,
                    'add_anime[finish_date][year]': 2017,
                    'add_anime[tags]': 'THANK YOU',
                    'add_anime[priority]': 0,
                    'add_anime[storage_type]':'',
                    'add_anime[storage_value]': form_inputs[7]['value'],
                    'add_anime[num_watched_times]': form_inputs[8]['value'],
                    'add_anime[rewatch_value]': '',
                    'add_anime[comments]':'',
                    'add_anime[is_asked_to_discuss]': 0,
                    'add_anime[sns_post_type]': 0,
                    'submitIt': 0,
                    'csrf_token': payload['csrf_token']
                }

  edit = req.post(url, data=edit_form)
  print('Done!')





