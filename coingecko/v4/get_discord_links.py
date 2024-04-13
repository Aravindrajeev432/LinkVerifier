
import json
import re
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

from utils import read_contacts_from_json

# driver = webdriver.Chrome()
all_discord_links: list = []
def main():


    json_file_path = "all_coins_links.json"
    # Read contacts from the JSON file
    json_data: list = read_contacts_from_json(json_file_path)
    # print(json_data)
    for link in json_data:
        match = re.search(r"/([^/]+)$", link)
        if match:
            
            reqUrl = f"https://api.coingecko.com/api/v3/coins/{match.group(1)}?community_data=true&localization=false"
            response = requests.get(reqUrl)
            if response.status_code != 200:
                print(response.status_code)
                print(link)
                print(response.text)
                break
            
            chat_urls = [x for x in response.json().get("links").get("chat_url") if x != ""]
        for url in chat_urls:
            discord_regex = r"(?:https?://)?(?:discord\.(?:[a-z]+))"
            # discord_url = url_obj.get("href")
            if re.match(discord_regex, url):
                # if discord_url == "https://discord.gg/EhrkaCH":
                #     continue
                
                all_discord_links.append({"slug":link,"discord_url":url})
                continue
    
    print(len(all_discord_links))
    file_path = "all_discord_links.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(all_discord_links, json_file, indent=2)




if __name__ == "__main__":
    main()