# read coins.json
import json
import time
from decouple import config
import requests

with open("coins.json", "r") as f:
    coins = json.load(f)



headers = {
  'x-access-token': config('API_KEY')
}
all_discord_links:list = []
for coin in coins:
    time.sleep(1)
    coin_uuid = coin['uuid']
    coin_slug = coin['coinrankingUrl']
    coin_details_url = f'https://api.coinranking.com/v2/coin/{coin_uuid}'
    response = requests.get(coin_details_url, headers=headers)
    data = response.json()
    links:list[dict] = data['data']['coin']['links']
    discord_link:str|None = None
    for link in links:
        if link['type'] == 'discord':
            discord_link = link['url']
            print(f"==>> discord_link: {discord_link}")
    if discord_link is None:
        continue
    all_discord_links.append({'coin_slug': coin_slug, 'discord_link': discord_link})
    

with open('all_discord_links.json', 'w') as f:
    json.dump(all_discord_links, f)