
import json
import time
import requests

all_discord_links:list[dict[str,str]] = []

token_ids = [
    "solana",'ethereum','bsc','base','arbitrum','polygon',
    'tron','avalanche','optimism','ton','linea','scroll',
    'blast','sui','mantle','osmosis','celo','harmony',
    'zksync','fantom','pulsechain','hyperliquid',
    'starknet','core','seiv2','cronos','mode','polygonzkevm',
    'manta','multiversx','metis','hedera','near','flare'
    ,'kava','canto','algorand','gnosischain','injective','venom','confulx']
pair_count = 0 
for token_id in token_ids:
    time.sleep(2)
    url = f"https://api.dexscreener.com/latest/dex/search?q={token_id}"
    response = requests.get(url)
    pairs = response.json().get('pairs',[])
    print('token_id:',token_id,'pairs:',len(pairs))
    continue
    for pair in pairs:
        pair_count += 1
        continue
        if pair.get('info') is None:
            continue
        socials = pair.get('info').get('socials',[])
        for social in socials:
            if social.get("type") == "discord":
                data={'chain_id':pair.get('chainId'),
                      'page_url':pair.get('url'),
                      'discord_url':social.get('url')}
                all_discord_links.append(data)
    

# file_path = "all_discord_links.json"
# with open(file_path, "w", encoding="utf-8") as json_file:
#     json.dump(all_discord_links, json_file, indent=2)
print(pair_count)