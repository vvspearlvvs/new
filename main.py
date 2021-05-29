import requests
import base64
import json

import Search

client_id = "c87e807943a1483883faaaa881aa43ef"
client_secret = "110de254602e440ea1f72f08f8396ccc"

endpoint = "https://accounts.spotify.com/api/token"

encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

headers = {"Authorization": "Basic {}".format(encoded)}
payload = {"grant_type": "client_credentials"}

response = requests.post(endpoint, data=payload, headers=headers)
#print(json.loads(response.text))
access_token = json.loads(response.text)['access_token']
#print(access_token)

headers = {"Authorization": "Bearer  {}".format(access_token)}

#1.search artist (with search api)
search_data = Search.search('BTS', headers)['artists']
for item in search_data['items']:
    #print(item.keys())
    id = item['id']
    name = item['name']
    popularity = item['popularity']
    followers = item['followers']['total']
    artist_url = item['external_urls']['spotify']
    image_url = item['images'][0]['url']
    genres= item['genres']

#1.1 insert DB

#2.search music(