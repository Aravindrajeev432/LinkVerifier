import time
from requests import Session
from icecream import ic
from utils import coingecko_code_extracter

session: Session = Session()
coingecko_url: str = "https://api.coingecko.com/api/v3/coins/list"
coingecko_coin_url = "https://www.coingecko.com/en/coins/"

coingecko_res = session.get(coingecko_url)
ic(len(coingecko_res.json()))
limit = 0
for coin in coingecko_res.json():
    limit += 1
    coin.get('name')
    time.sleep(1)
    code = coingecko_code_extracter(session=session,coin_name=coin.get('name'))
    if code:
        print(code)
        break
    else:
        time.sleep(1)