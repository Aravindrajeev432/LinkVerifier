import json
import time
import requests

headers = {
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://coinranking.com/?page=1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
}

offset = 0
limit = 100
data= []
while True:
    url = f'https://coinranking.com/api/v2/coins?offset={offset}&orderBy=marketCap&limit=50&orderDirection=desc&referenceCurrencyUuid=yhjMzLPhuIDl&timePeriod=24h&search=&tiers[]=1&tiers[]=2'
    response = requests.get(
        url,
    )
    offset += 50
    print(f"==>> offset: {offset}")
    try:
        data.extend(response.json().get('data').get('coins'))
        print(f"==>> len of data: {len(data)}")
    except Exception as e:
        print(e)
        print(f"==>> response.status_code: {response.status_code}")
        print(f"==>> response.text: {response.text}")
        break
    time.sleep(5)
    if len(data) >= 1000:
        break


# save data to a json file
with open('coins.json', 'w') as f:
    json.dump(data, f)