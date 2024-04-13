import json
import re
import time

import requests
from utils import read_contacts_from_json
def main():
    json_file_path = "all_coins.json"
    # Read contacts from the JSON file
    json_data: list = read_contacts_from_json(json_file_path)
    print(len(json_data))
    discord_links = []
    for link in json_data:
        print(link)
        reqUrl = f"https://api.coingecko.com/api/v3/coins/{link.get('id')}?community_data=true&localization=false"
        while True:
            response = requests.get(reqUrl)
            
            if response.status_code != 200:
                if response.status_code == 429:
                    print("too many requests")
                    print(response.text)

                    time.sleep(20)
                    continue
                print(response.status_code)
                print(link)
                print(response.text)
                break
            else:
                break
            
        for url in response.json().get("links").get("chat_url"):
            if "discord" in url:
                discord_links.append({"coin_name": link.get("name"), "url": url})
                break
    print(f"==>> chat_urls: {discord_links}")
    file_path = "all_coins_data.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(discord_links, json_file, indent=2)
    

if __name__ == "__main__":
    main()