import json
import pprint
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
# from selenium import webdriver



# website = "https://opensea.io/rankings?sortBy=total_volume"
# path = "/Users/arvindr/Downloads/chrome-mac-arm64/Google Chrome for Testing.app"

# driver = webdriver.Chrome()
# driver.get(website)
# collection_links = []
# # time.sleep(15)
# # for link in driver.find_elements_by_xpath("//a[@href[starts-with(., '/collection/')]]"):
# #     collection_links.append(link.get_attribute("href"))

# # print(collection_links)

# # driver.quit()



def main():
    json_file_path = 'custom_data.json'

    
    coins_from_file = read_contacts_from_json(json_file_path)
    coins = coins_from_file.get('data').get('topCollectionsByCategory').get('edges')
    print(len(coins))
    discord_urls : list = []
    for coin in tqdm(coins):
        slug = coin.get('node').get('slug')
        link = check_for_discord_links(url=f"https://opensea.io/collection/{slug}")
        if link:
            discord_urls.append({"slug":slug,"discord_url":link})

    file_path = "all_discord_links.json"

    # Write the list to the JSON file
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(discord_urls, json_file, indent=2)
    # check_for_discord_links(url="https://opensea.io/collection/mutant-ape-yacht-club")
    return
    
    
def read_contacts_from_json(json_file_path, encoding='utf-8'):
    try:
        with open(json_file_path, 'r', encoding=encoding) as json_file:
            contacts = json.load(json_file)
        return contacts
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {json_file_path}")
        return []
    # Specify the path to the JSON file

# "data": {
#         "rankings": {
#             "edges": [
#                 {
#                     "node": 


def check_for_discord_links(url: str):
    time.sleep(5)
    headers: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
    }

    res = requests.get(url=url, headers=headers)
    print(res.status_code)
    html = res.text
    soup = BeautifulSoup(html, "html.parser")
    # with open("output.html", "w", encoding="utf-8") as file:
    #     file.write(html)
    script_tag = soup.find('script', id='__NEXT_DATA__')

    if script_tag:
        # Get the JSON content from the script tag
        json_content = script_tag.string

        # Print or process the JSON content as needed
        
        # If you want to parse the JSON content
        json_data = json.loads(json_content)
        # pprint.pprint(json_data)
        collection_name = json_data['props']['pageProps']['variables']['collection']
        # print(collection_name)
        uniquekey = json_data['props']['pageProps']['initialRecords']['client:root'][f"collection(collection:\"{collection_name}\")"]["__ref"]
        # print(uniquekey)
        discord_url = json_data['props']['pageProps']['initialRecords'][f"{uniquekey}"]["discordUrl"]
        # print(discord_url)
        if discord_url:
            return discord_url
            # with open("discord.txt", "a") as file:
            #     file.write(discord_url + "\n")
        
        # json_file_path = 'filtered_contactstwo.json'
        # with open(json_file_path, 'w') as json_file:
        #     json.dump(json_data, json_file, indent=2)
        # Now you can work with the parsed JSON data

    pass

if __name__ == "__main__":
    main()