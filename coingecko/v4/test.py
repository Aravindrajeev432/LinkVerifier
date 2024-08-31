
import json
import re
import time

from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType
from utils import read_contacts_from_json
from selenium.webdriver.chrome.options import Options
# driver = webdriver.Chrome()
all_discord_links: list = []
def main():

    json_file_path = "all_coins_links.json"
    # Read contacts from the JSON file
    json_data: list = read_contacts_from_json(json_file_path)
    proxies:list = get_proxies()
    
    print(len(json_data))
    current_proxy_index = 0
    
    for link in json_data:
        # proxy = proxies[current_proxy_index]
        proxy = "14abf8ac537ea:5041996603@166.0.131.167:12323"
        # Rotate to the next proxy
        options = {
            'proxy': {
                'http': f'http://{proxy}', 
                'https': f'https://{proxy}',
                'verify_ssl': False,
            
            }
        }
        driver = webdriver.Chrome(
            seleniumwire_options=options
        )
        driver.get("https://www.coingecko.com/en/coins/alaska-gold-rush")
        # driver.implicitly_wait(15.5)
        time.sleep(35)
        
        
        # current_proxy_index = (current_proxy_index + 1) % len(proxies)
        break
    driver.quit()



def get_proxies()->list:
    # read valid ips from file
    file_path = "valid_ips.json"
    with open(file_path, "r", encoding="utf-8") as json_file:
        ips = json.load(json_file)
    return ips

if __name__ == "__main__":
    main()