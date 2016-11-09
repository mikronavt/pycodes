import requests
import json
import operator

client_id = '85fe351b1a295572351c'
client_secret = 'fd527ca0d0603b1a197260bbb0bbee0a'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}


s = []
while(True):
    artist_id  = input()
    if artist_id == 'stop':
        break

    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/" + artist_id, headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)

    s.append(str(j['birthday']) + " " + j['sortable_name'])

s.sort()

for artist in s:
    print(artist[5::])



