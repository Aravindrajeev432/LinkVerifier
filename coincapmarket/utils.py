import time
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from icecream import ic
def is_valid_link(session: Session,code: str) -> bool:
    try:
        response = session.get(f"https://discord.com/api/v10/invites/{code}",
                               headers={"Authorization": "Bearer vh4jtqRCG5tW7NljfdihoIcBxCuspl",})
        limit_remining : str = response.headers.get('x-ratelimit-remaining',2)
        
        if int(limit_remining) <= 2:
            ic("sleeping")
            time.sleep(float(response.headers.get('x-ratelimit-reset-after',20)))
        if response.status_code != 200:
            
            if response.status_code == 429:
                ic(f"==>> limit_remining: {limit_remining}")
                ic(f"==>> x-ratelimit-limit: {response.headers.get('x-ratelimit-limit')}")
                ic(f"==>> response.headers.get('x-ratelimit-remaining'): {response.headers.get('x-ratelimit-remaining')}")
                ic(f"==>> response.headers.get('x-ratelimit-reset-after'): {response.headers.get('x-ratelimit-reset-after')}")
                pass
            return False
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        ic(e)
        return False
    return True

