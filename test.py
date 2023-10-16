import re
discord_url = "https://discord.gg/eos-network"
code_regex = r'https?://discord\.gg/([a-zA-Z0-9-]+)'

code = re.search(code_regex, discord_url).group(1)
print(code)