from dataclasses import dataclass
import json
import re
import threading
import queue
import time
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from utils import read_contacts_from_json

q = queue.Queue()
all_discord_links:list[dict[str,str]] = []
@dataclass
class DiscordLink:
    page_url: str
    discord_url: str

def get_proxies()->list:
    # read valid ips from file
    file_path = "valid_ips.json"
    with open(file_path, "r", encoding="utf-8") as json_file:
        ips = json.load(json_file)
    return ips


proxies:list = get_proxies()
print(f"==>> proxies: {proxies}")
json_file_path = "all_coins_links.json"
# Read contacts from the JSON file
json_data: list = read_contacts_from_json(json_file_path)
print(f"==>>len json_data: {len(json_data)}")
count = 0
for link in json_data:
    if count == 2000:
        break
    q.put(link)
    count += 1


def get_discord_links(proxy:str):
    
    global q
    global all_discord_links
    options = {
            'proxy': {
                'http': f'http://{proxy}', 
                'https': f'https://{proxy}',
                'verify_ssl': False,
                
            }
        }
    chrome_options = Options()
    chrome_options.add_argument("--disable-javascript")
    
    # chrome_options.add_argument("--headless") 
    driver = webdriver.Chrome(options=chrome_options,
            seleniumwire_options=options
        )
    
    count = 0

    while not q.empty():
        link = q.get()
        print(f"==>> link: {link}")
        try:
            driver.get(link)
            if count == 0:
                driver.implicitly_wait(15.5)
            else:
                driver.implicitly_wait(1.5)
            count += 1
            driver.execute_script("setTimeout(function(){ window.stop(); }, 1000);")
            # time.sleep(25)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        
            discord_links = soup.find_all("a", href=lambda href: href and "discord" in href)
            if len(discord_links) == 0:
                continue
            for url_obj in discord_links:
                discord_regex = r"(?:https?://)?(?:discord\.(?:[a-z]+))"
                discord_url = url_obj.get("href")
                if re.match(discord_regex, discord_url):
                    if discord_url == "https://discord.gg/EhrkaCH":
                        continue
                    
                    all_discord_links.append({"slug":link,"discord_url":discord_url})
        except Exception as e:
            print(f"==>> proxy: {proxy}")
            print(f"==>> Exception: {e}")
            pass
    driver.quit()

threads = []
for proxy in proxies:
    thread = threading.Thread(target=get_discord_links, args=(proxy,))
    thread.start()
    threads.append(thread)
    

for thread in threads:
    thread.join()

file_path = "all_discord_links.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(all_discord_links, json_file, indent=2)

