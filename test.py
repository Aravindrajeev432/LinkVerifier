
from pprint import pprint
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from concurrent.futures import ThreadPoolExecutor

session = Session()
def is_valid_link(code: str) -> bool:
    try:
        response = session.get(f"https://discord.com/api/v9/invites/{code}")
        
        
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
batch = ["2up5U32"] * 10
[executor.submit(is_valid_link, c) for c in batch]

executor.shutdown()
    

