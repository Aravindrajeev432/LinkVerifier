"""
Removing old discord links , on ly checking new ones, Run before get_discord_linksv2.py

creating every invalid links history to a invalid discord link history file 

"""

import json
from utils import read_contacts_from_json

json_file_path = "all_coins_links.json"
# Read contacts from the JSON file
json_data: list = read_contacts_from_json(json_file_path)
with open("invalid_discord_links_history.json", "r") as json_file:
    try:
        invalid_discord_links_history:dict[str:str]= json.load(json_file)
    except FileNotFoundError:
        print("File not found: invalid_discord_links_history.json")
        invalid_discord_links_history = {}
    except json.JSONDecodeError:
        print("Error decoding JSON in file: invalid_discord_links_history.json")
        invalid_discord_links_history = {}

new_all_coin_links = []
for page_link in json_data:
    if page_link not in invalid_discord_links_history:
        new_all_coin_links.append(page_link)

with open("all_coins_links.json", "w") as json_file:
    json.dump(new_all_coin_links, json_file, indent=4)