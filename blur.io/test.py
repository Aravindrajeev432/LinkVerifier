import re
import requests
from utils import is_valid_link_checker

session = requests.Session()
def main():
    discord_url = "https://discord.gg/animo"
    code_regex = r"https?://discord\.gg/([a-zA-Z0-9-]+)"
    code = re.search(code_regex, discord_url).group(1)
    print(f"==>> code: {code}")
    result = is_valid_link_checker(session=session, code=code)
    print(f"==>> result: {result}")
    

if __name__ == "__main__":
    main()