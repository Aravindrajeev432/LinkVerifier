import requests

res = requests.get("https://coinmarketcap.com/")
if res.status_code != 200:
    print("ConiMarkert cap not working")
else:
    print("ConiMarkert cap working")

res = requests.get("https://discord.com/api/v10/invites/hQs894U", headers={"Authorization": "Bearer vh4jtqRCG5tW7NljfdihoIcBxCuspl"})

print(f"==>> 'x-ratelimit-limit': {res.headers.get('x-ratelimit-limit')}")

print(f"==>> 'x-ratelimit-remaining': {res.headers.get('x-ratelimit-remaining')}")
if res.status_code != 200:
    print("Discord not working")
else:
    print("Discord working")