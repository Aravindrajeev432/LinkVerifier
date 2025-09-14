import json
import time
import requests

params = {
    'limit': '50',
    'skip': '0',
}

data = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
while True:
    url = 'https://skynet.certik.com/api/leaderboard-all-projects/query-leaderboard-projects'
    response = requests.get(url=url, params=params, headers=headers)
    if not response.ok:
        print(response.status_code)
        print(response.url)
        print(response.text)
        break
    # print(response.json())
    data.extend(response.json().get('items'))
    print(len(data))
    if len(data) >= 1000:
        break
    params['skip'] = str(int(params['skip']) + 50)
    time.sleep(5)
    # break

with open('skynet_coins.json', 'w') as f:
    json.dump(data, f)

print("hi 1")
print("hi 2")
