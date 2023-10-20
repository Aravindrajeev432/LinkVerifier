
from pprint import pprint
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import time  
from concurrent.futures import ThreadPoolExecutor

session = Session()
headers = {
    "Authorization": "Bearer vh4jtqRCG5tW7NljfdihoIcBxCuspl",
}
session.headers.update(headers)
def is_valid_link(code: str) -> bool:
    try:
        response = session.get(f"https://discord.com/api/v9/invites/{code}")
        print(f"==>> response.headers['x-ratelimit-remaining']: {response.headers['x-ratelimit-remaining']}")
        print(f"==>> response.headers['x-ratelimit-reset']: {response.headers['x-ratelimit-reset']}")
        print(f"==>> response.headers['x-ratelimit-reset-after']: {response.headers['x-ratelimit-reset-after']}")
        print("---")
        if response.status_code != 200:
            
            print(response.json())
            
            return False
        else:
            pass
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return False
    return True



executor = ThreadPoolExecutor(10)
elements_per_interval = 4
batch = ["2up5U32"] * 15
  
epoch_time = int(time.time())

[executor.submit(is_valid_link, c) for c in batch]

executor.shutdown()
print(f"==>> epoch_time: {epoch_time}")

