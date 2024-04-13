
import json
import requests


def main():
    """
    creates all coins.json

    """
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    file_path = "all_coins.json"
    with open(file_path, "w", encoding="utf-8") as json_file:
        json.dump(response.json(), json_file, indent=2)

if __name__ == "__main__":
    main()