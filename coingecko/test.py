import requests

headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

redirect_url = f"https://www.coingecko.com/en/search_redirect?id=3shares&type=coin"

response = requests.get(url = redirect_url, headers=headers)
print(response.status_code)
print(response.url)
print(response.headers)