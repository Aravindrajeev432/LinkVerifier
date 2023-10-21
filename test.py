
from pprint import pprint
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects,MissingSchema
import time  
from concurrent.futures import ThreadPoolExecutor
import re

from utils import is_valid_link


session = Session()
headers = {
    "Authorization": "Bearer vh4jtqRCG5tW7NljfdihoIcBxCuspl",
}
session.headers.update(headers)

discord_regex = r'(?:https?://)?(?:discord\.(?:[a-z]+))'
discord_url = "view/discord-bots/"
if re.match(discord_regex, discord_url):
    
    # domain regx
    
    if ".com" in discord_url:
        print(".com")
        # urls ends with .com
        # extract code from url .com
        code_regex = r'https?:\/\/discord\.com\/invite\/([a-zA-Z0-9-]+)'
        try:
            code = re.search(code_regex, discord_url).group(1)
            result = is_valid_link(session=session,code=code)
            if not result:
                print("not valid")
        except Exception as e:
            # ic(e)
            
            print("captcha link")
    elif ".gg" in discord_url:
        print(".gg")
        # extract code from url .gg
        code_regex = r'https?://discord\.gg/([a-zA-Z0-9-]+)'
        try:
            code = re.search(code_regex, discord_url).group(1)
            result = is_valid_link(session=session,code=code)
            if not result:
                print("not valid")
        except Exception as e:
            # ic(e)
            print("captcha link")
        
else:
    
    # non discord direact urls
    print("non discord direact urls")
    try:
        response = session.get(discord_url, allow_redirects=True)
        final_url = response.url
        print(f"==>> final_url: {final_url}")
        
        try:
            code_regex = r'https?:\/\/discord\.com\/invite\/([a-zA-Z0-9-]+)'
            code = re.search(code_regex, final_url).group(1)
            print(f"==>> code: {code}")

            result = is_valid_link(session=session,code=code)
            if not result:
                print("not valid")
        except Exception as e:
            # ic(e)
            print("captcha link")
    except MissingSchema:
        print("missing schema")
        
    