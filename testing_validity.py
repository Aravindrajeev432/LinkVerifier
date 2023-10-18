import requests

res = requests.get("https://coinmarketcap.com/")
if res.status_code != 200:
    print("ConiMarkert cap not working")
else:
    print("ConiMarkert cap working")

res = requests.get("https://discord.com/api/v10/invites/2up5U32")
if res.status_code != 200:
    print("Discord not working")
else:
    print("Discord working")