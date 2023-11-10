

import time
from requests import Session
from requests.exceptions import Timeout, TooManyRedirects, MissingSchema


session = Session()

def is_valid_link_checker(session: Session,code: str) -> bool:
    "return False for invalid link"
    try:
        response = session.get(f"https://discord.com/api/v10/invites/{code}",
                               headers={"Authorization": "Bearer vh4jtqRCG5tW7NljfdihoIcBxCuspl",})
        print(response.status_code)
        limit_remining : str = response.headers.get('x-ratelimit-remaining')
        print(f"==>> limit_remining: {limit_remining}")
        print(type(limit_remining))
        if int(limit_remining) <= 1:
            
            time.sleep(float(response.headers.get('x-ratelimit-reset-after')))
        if response.status_code != 200:
            
            if response.status_code == 429:
                print(f"==>> limit_remining: {limit_remining}")
                print(f"==>> x-ratelimit-limit: {response.headers.get('x-ratelimit-limit')}")
                print(f"==>> response.headers.get('x-ratelimit-remaining'): {response.headers.get('x-ratelimit-remaining')}")
                print(f"==>> response.headers.get('x-ratelimit-reset-after'): {response.headers.get('x-ratelimit-reset-after')}")
                pass
            return False
    except (ConnectionError, Timeout, TooManyRedirects, MissingSchema) as e:
        print(e)
        return False
    return True

result = is_valid_link_checker(session=session,code="vae4zvy")
if not result:
    print("working")
result = is_valid_link_checker(session=session,code="nsp9JTC")
if result:
    print("working fine")
print("Everything fine")