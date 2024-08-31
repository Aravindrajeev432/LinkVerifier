

import requests


url = f'https://skynet.certik.com/projects/wagmi-game'
response = requests.get(url)   
print(response.status_code)