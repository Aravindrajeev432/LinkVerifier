import requests
import json
import hashlib
url = "https://api.coingecko.com/api/v3/coins/list"
res = requests.get(url=url)
print(len(res.json()))

json_string = json.dumps(res.json())
# print(json_string[:100])
# # json_string = json.dumps(sample)
sha256 = hashlib.sha256()
sha256.update(json_string.encode('utf-8'))
hash_value = sha256.hexdigest()
print(hash_value)


with open("coin_list_hash.txt", "w") as f: 
    f.write(str(hash_value))



