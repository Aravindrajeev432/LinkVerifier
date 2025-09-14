import requests

cookies = {
    '_session_id': '18a4f1843fca2a82a4a92f6e04c0f196',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Sep+07+2024+12%3A42%3A32+GMT%2B0530+(India+Standard+Time)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=338c17b8-0e0d-474d-aa23-21d40d37f045&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    'cookie': '_session_id=18a4f1843fca2a82a4a92f6e04c0f196; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+07+2024+12%3A42%3A32+GMT%2B0530+(India+Standard+Time)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=338c17b8-0e0d-474d-aa23-21d40d37f045&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

response = requests.get('https://www.coingecko.com/', cookies=cookies, headers=headers)
print(f"==>> response: {response.status_code}")

