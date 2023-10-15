from pprint import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"
parameters = {"page": 90}
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
# }

session = Session()
# session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    print(response.status_code)
    
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    target_links = soup.find_all(
        "a",
        href=lambda href: href
        and href.startswith("/currencies/")
        and not "#" in href and not "?" in href,
    )
    print(len(target_links))
    # Iterate through the target_links and print them
    # for link in target_links:
    #     print(link["href"])
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
