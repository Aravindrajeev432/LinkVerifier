import json
import time
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects,MissingSchema, InvalidSchema
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

# from utils import is_valid_link

# session = Session()


# count: int = 1
# start = 1
# limit = 500
# params = {
#     "start": start,
#     "limit": limit,
#     "sortBy": "market_cap",
#     "sortType": "desc",
#     "convert": "USD,BTC,ETH",
#     "cryptoType": "all",
#     "tagType": "all",
#     "audited": "false",
#     "aux": "ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap",
# }
# all_data: list = []
# crypto_data: list = []
# while True:
#     try:
#         response = session.get(
#             "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing",
#             params=params,
#         )
#     except (ConnectionError, Timeout, TooManyRedirects) as e:
#         break
#     crypto_data = response.json().get("data").get("cryptoCurrencyList")
#     all_data += crypto_data
#     # if len(crypto_data) > 5000:
#     #     break
#     if len(crypto_data) == 0:
#         break
#     if count > 0:
#         params["start"] += limit

#     count += 1
#     time.sleep(1)

# print(len(all_data))
# with open('all_symbols.json', 'w') as f:
#     json.dump(all_data, f)

with open('all_symbols.json', 'r') as f:
    all_symbols = json.load(f)
# print(len(all_symbols))

unique_symbols = dict()
for coin in all_symbols:
    if coin['symbol'] not in unique_symbols:
        unique_symbols[coin['symbol']] = 1
    else:
        unique_symbols[coin['symbol']] += 1



# print(unique_symbols)
with open('unique_symbols.txt', 'w') as f:
    for symbol,count in unique_symbols.items():
        if count <=3:
            continue
        f.write(symbol + ',')
