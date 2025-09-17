# Link Verifer

Checking a Discord invitaion Link valid or not
This project is not for public use, so it may go private 🫥

## Installation

Use an Env(install if you dont)

### activate env and..

## Installation

Use an Env(install if you dont)

### activate env and..

```bash

  pip install -r requirements.txt

```

Use python for Windows, python3 for Mac/Linux

## Sites

## CoinCapMarket

```bash
  python3 conincapdirect.py
```

## CoinCapMarket V2

```bash
  cd coincapmarket
  python3 coincapdirectv2.py
  python3 extract_discord_links.py
  python3 check_discord_links.py

```

coinmarketcap_meta_data.json will be created
then

```bash
  python3 extract_discord_links.py
```

## Blur.io

```bash
  cd blur.io
  python3 blurv1.py
```

## Coingecko Version 4

Under development

```bash
    cd coingecko/new
    python3 -c 'from utils import *; create_invalid_discord_links_history()'
```
goto https://www.coingecko.com/
copy page source and paste in gecko.html
run 
```bash
python3 load_html.html
```
continue the process for next 9 pages
```bash
python3 remove_old_discord_links.py
python3 get_discord_linksv2.py
python3 check_discord_links.py
```


## Crypto.com

```
  cd cryptocom
  python3 cryptov1.py
```

## OpenSea

get all coin data from https://opensea.io/rankings?sortBy=total_volume
select All, and lookfor a graphql request in network tab . copy the data.
create and paste in 'custom_data.json' file . then run openseav3.py,
After completion run check_discord_links.py to get the invalid dicord links

```
   cd opensea
   python3 openseav3.py
   python3 check_discord_links.py
   
```

## OpenSea From Every Category

in early we're only fetching 24h volume coin details,
in this we're going through every volumes,

goto https://opensea.io/rankings and
and lookfor a graphql request in network tab . copy the data.
create and paste in 'custom_data.json' file
do this for every every voulume

and run openseav4.py in each step , distint discord urls are saved

## Dexscreener

```
  cd dexscreener
  python3 dexscreenerv1.py
```

# Notes

Make sure installed required packages.
Try latest version specified.
