

import json
from pprint import pprint


import requests
from decouple import config
api_key = config('API_KEY')

with open('unique_symbols.txt', 'r') as f:
    unique_symbols = f.read().splitlines()
print(unique_symbols[0])

params = {
"CMC_PRO_API_KEY": api_key,
"aux":"urls",
'symbol': f'{unique_symbols[0]}'}  

res = requests.get("https://pro-api.coinmarketcap.com/v2/cryptocurrency/info", params=params)
pprint(res.url)
try:
    # pprint(res.json())
    with open('coinmarketcap_meta_data.json', 'w') as f:
        json.dump(res.json(), f, indent=2)
except:
    print(res.text)



    