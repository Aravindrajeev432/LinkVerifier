import json

# Specify the path to the JSON file
json_file_path = 'coinmarketcap_meta_data.json'

# Read data from the JSON file
with open(json_file_path, 'r') as f:
    coinmarketcap_meta_data = json.load(f)

data_to_save:list[dict[str,str]] = []

# Print the data to verify
coin_data = coinmarketcap_meta_data['data']
for symbol_name, coin_list in coin_data.items():
    # print(coin_list)
    for coin in coin_list:
        urls_chat:list = coin.get('urls',{}).get('chat',[])
        # print(urls_chat)
        for link in urls_chat:
            if 'discord' in link:
                print(link)
                data_to_save.append({"slug":coin.get('slug'),"discord_url":link})
                

    
# Save data to a JSON file
with open('all_discord_links.json', 'w') as f:
    json.dump(data_to_save, f, indent=2)
