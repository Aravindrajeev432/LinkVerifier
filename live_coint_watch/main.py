import time
import requests
import json
from decouple import config
url = "https://api.livecoinwatch.com/coins/list"
API_KEY = config('API_KEY')

offset = 0
headers = {
    'content-type': 'application/json',
    'x-api-key': API_KEY
    }
data = []
while True:
    payload = json.dumps({
    "currency": "USD",
    "sort": "rank",
    "order": "ascending",
    "offset": offset,
    "limit": 1000,
    "meta": True
    })
    offset += 1000
    response = requests.request("POST", url, headers=headers, data=payload)
    
    data.extend(response.json())
    print(f"==>> len of data: {len(data)}")
    time.sleep(1)
    if len(data) >= 5000:
        break
# save data as json
with open('coins.json', 'w') as f:
    json.dump(data, f)