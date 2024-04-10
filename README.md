# Link Verifer

Checking a Discord invitaion Link valid or not

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

## Blur.io

```bash
  cd blur.io
  python3 blurv1.py
```
## Coingecko

```bash
  cd coingecko
  python3 coingecko.py
```

## Coingecko Version 2(Depricated)

```bash
  cd coingecko
  python3 coingeckov2.py

```

## Coingecko Version 3 (outdated)

```bash
  cd coingecko
  python3 coingeckov3.py

```

## Coingecko Version 4

Under development

```bash
    cd coingecko/v4
    python3 coingeckov4.py
    python3 get_discord_links.py
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

# Notes

In coingeckov3 reduced coin page link fetch time
Try latest version specified
CoinSniper & Opensea coming soon..
