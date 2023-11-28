import json

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
json_file_path = 'custom_data.json'

# Read contacts from the JSON file
coins_from_file = read_contacts_from_json(json_file_path)
# "data": {
#         "rankings": {
#             "edges": [
#                 {
#                     "node": 
coins = coins_from_file.get('data').get('rankings').get('edges')
print(len(coins))