import requests

url = 'https://solana.com/discord'

# Send a GET request with allow_redirects set to True to follow redirects
response = requests.get(url, allow_redirects=True)

# Get the final URL after following redirects
final_url = response.url

print("Final URL:", final_url)
