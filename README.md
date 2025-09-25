# Link Verifer

Checking a Discord invitaion Link valid or not
This project is not for public use, so it may go private 🫥

## Installation

Use an Env(install if you dont)

### activate env and..

## Installation

Use an Env(install if you dont)

### activate env 

mac
```
source env/bin/activate
```

```bash

  pip install -r requirements.txt

```

Use python for Windows, python3 for Mac/Linux

## Sites


## CoinCapMarket V3

*API key required
```bash
  cd coincapmarket
  python3 coinmarketcapv3.py

```




## Blur.io

```bash
  cd blur.io
  python3 blurv1.py
```

## Coingecko Version 4

Under development

Clear all_coins_links.json before start
```bash
    cd coingecko/new
    python3 -c 'from utils import *; create_invalid_discord_links_history()'
```
goto https://www.coingecko.com/
copy page source and paste in gecko.html
run 
```bash
python3 load_html.py
```
continue the process for next 9 pages
```bash
python3 remove_old_discord_links_history.py
python3 get_discord_linksv2.py
python3 check_discord_links.py
```


## Crypto.com

```
  cd cryptocom
  python3 cryptov1.py
```

## Opensea
v3,v4 depricated

Current working version is opensea_api_v1
```
  cd opensea
  python3 opensea_api_v1.py
```

## Dexscreener

```
  cd dexscreener
  python3 dexscreenerv1.py
```

# Notes

Make sure installed required packages.
Try latest version specified.
