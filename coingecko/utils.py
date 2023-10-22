import time
from requests import Session
from typing import Optional
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects, MissingSchema
from bs4 import BeautifulSoup
import re
def is_valid_link_checker(session: Session,code: str) -> bool:
    try:
        response = session.get(f"https://discord.com/api/v10/invites/{code}",
                               headers={"Authorization": "Bearer vh4jtqRCG5tW7NljfdihoIcBxCuspl",})
        limit_remining : str = response.headers.get('x-ratelimit-remaining')
        
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

def coingecko_code_extracter(session: Session,coin_id : str) -> Optional[dict]:
    """
    Returns None for if something goes wrong/ No Discord Links
    Return  {coin:"coin_id", url: url} for valid link
    Return {"captcha" :  true} for captcha links
    """

    headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
    }
    redirect_url = f"https://www.coingecko.com/en/search_redirect?id={coin_id}&amp;type=coin"
    response = session.get(url = redirect_url, headers=headers, allow_redirects=True)
    if response.status_code != 200:
        print("rate Limit Exceeded")
        return None
    url = response.url
    try:
        time.sleep(2)
        response = session.get(url=url, headers=headers)
        if response.status_code != 200:
            # if response.status_code == 429:
            #     time.sleep(int(response.headers.get('Retry-After')))
            print(f"==>> url: {url}")
            print(f"==>> status_code: {response.status_code}")
            return None
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return None
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    discord_links = soup.find_all("a", href=lambda href: href and "discord" in href)
    if len(discord_links) == 0:
        return {"discord_links": False}
    for url_obj in discord_links:
        discord_regex = r'(?:https?://)?(?:discord\.(?:[a-z]+))'
        discord_url = url_obj.get("href")
        if re.match(discord_regex, discord_url):
            if ".com" in discord_url:
                # urls ends with .com
                # extract code from url .com
                code_regex = r'https?:\/\/discord\.com\/invite\/([a-zA-Z0-9-]+)'
                try:
                    code = re.search(code_regex, discord_url).group(1)
                    return {'code':code,'url':url}
                except Exception as e:
                    return {'captcha':True}
            elif ".gg" in discord_url:
                # extract code from url .gg
                code_regex = r'https?://discord\.gg/([a-zA-Z0-9-]+)'
                try:
                    code = re.search(code_regex, discord_url).group(1)
                    return {'code':code,'url':url}
                except Exception as e:
                    return {'captcha':True}
        else:
            # non discord direact urls
            response = session.get(discord_url, allow_redirects=True)
            final_url = response.url
            try:
                code_regex = r'https?:\/\/discord\.com\/invite\/([a-zA-Z0-9-]+)'
                code = re.search(code_regex, final_url).group(1)
                return {'code':code,'url':url}
            except Exception as e:
                return {'captcha':True}