
import json
import re
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType
from utils import read_contacts_from_json

driver = webdriver.Chrome()
all_discord_links: list = []
def main():

    json_file_path = "all_coins_links.json"
    # Read contacts from the JSON file
    json_data: list = read_contacts_from_json(json_file_path)

    print(len(json_data))
    current_proxy_index = 0
    
    for link in json_data:
        
        # Rotate to the next proxy

        driver.get(link)
        driver.implicitly_wait(2.5)
        time.sleep(2)
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
        
    print(len(all_discord_links))
    file_path = "all_discord_links.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(all_discord_links, json_file, indent=2)




if __name__ == "__main__":
    main()