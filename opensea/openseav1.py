import time
import requests
from decouple import config

from requests import Session




start = time.time()
print(start)

session = Session()
api_key = config("APIKEY")

next: str = ""
collections: list = []
count: int = 0

def discord_link_filter(obj):
    if obj.get('discord_url') == '':
        return False
    return True


while True:
    count += 1
    print(f"==>> count: {count}")

    print(f"==>> next: {next}")
    opensea_collections_url: str = (
        f"https://api.opensea.io/api/v2/collections?include_hidden=false&chain_identifier=ethereum&next={next}"
    )
    headers = {"accept": "application/json", "x-api-key": api_key}
    response = session.get(opensea_collections_url, headers=headers)
    if response.status_code != 200:
        print(f"==>> response.status_code: {response.status_code}")
        print(f"==>> response.headers: {response.headers}")
        break
    res_collections_all : list = response.json().get("collections")
    
    if len(res_collections_all) == 0:
        break

    # filter collections with discord url link
    res_collections = filter(discord_link_filter, res_collections_all) 
    if len(list(res_collections)) != 0:
        
        collections.append(list(res_collections))
    print(f"==>> collections: {collections}")
    print(collections)
    
    next = response.json().get("next")


print(len(collections))

total_time = time.time() - start
print(f"time taken for contacts: {total_time:.2f} seconds")
print("all done")