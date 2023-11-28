import json
from pprint import pprint
def read_contacts_from_json(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            contacts = json.load(json_file)
        return contacts
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file: {json_file_path}")
        return []

# Specify the path to the JSON file
json_file_path = 'scriptjson.json'

# Read contacts from the JSON file
json_data = read_contacts_from_json(json_file_path)
# "data": {
#         "rankings": {
#             "edges": [
#                 {
#                     "node": 

collection_name = json_data['props']['pageProps']['variables']['collection']
print(collection_name)
uniquekey = json_data['props']['pageProps']['initialRecords']['client:root'][f"collection(collection:\"{collection_name}\")"]["__ref"]
print(uniquekey)
discord_url = json_data['props']['pageProps']['initialRecords'][f"{uniquekey}"]["discordUrl"]
print(discord_url)