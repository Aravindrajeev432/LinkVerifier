import json
import requests
import time


def fetch_all_data(initial_url, headers):
    all_data = []
    api_url = initial_url
    retries = 3
    while api_url:
        try:
            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            items = data.get("collections", [])
            all_data.extend(items)
            if items:
                last_item = items[-1]
                contract_address = last_item.get("contractAddress")
                volume_one_day = last_item.get("volumeOneDay")
                amount = volume_one_day.get("amount") if volume_one_day else None
                if amount:
                    next_url = f"https://core-api.prod.blur.io/v1/collections/?filters=%7B%22cursor%22%3A%7B%22contractAddress%22%3A%22{contract_address}%22%2C%22volumeOneDay%22%3A%22{amount}%22%7D%2C%22sort%22%3A%22VOLUME_ONE_DAY%22%2C%22order%22%3A%22DESC%22%7D"
                    api_url = next_url
                else:
                    api_url = None
            else:
                api_url = None
            
        except requests.exceptions.RequestException as e:
            # print("Error fetching data:", e)
            retries -= 1
            time.sleep(5)
    if retries == 0:
        print("Failed to fetch data after retries.")
    return all_data


def save_to_json(data, filename="blur_data.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


initial_url = "https://core-api.prod.blur.io/v1/collections/?filters=%7B%22sort%22%3A%22VOLUME_ONE_DAY%22%2C%22order%22%3A%22DESC%22%7D"
headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,ml;q=0.8,tr;q=0.7,ta;q=0.6",
        "Cookie": "_ga=GA1.2.683743457.1711516675; _gid=GA1.2.746631795.1711516675; _ga_C09NSBBFNH=GS1.1.1711516674.1.1.1711516788.0.0.0; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BL2Q5Pfpu47n9LgWvZD9fEfAeoP1HHYKSq04g9RTsGwWyYN3aO94KU; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX191M%2FFoyIp2gVfrh%2BYhb7X8pUfucMy1DxQ%3D; __cf_bm=QE5LK9VGiAcE3pWZViC_AvTcOyCitvbaM9nxFnByx_Q-1711519150-1.0.1.1-T8B35h0dcKjdV.HxemtpjVR_yz62taCuT.Ld3vPMoFledMk7_SO2KtUZfMPjBK5peimy2U6nK8ffM8CK1i9p8g; rl_user_id=RudderEncrypt%3AU2FsdGVkX19vYFCC%2Bp0krkU3e5HFL2h%2B5c9BXvIk8kk%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2FwbmmSGVj9PntOhquumJ9MHpvo8pneWes%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18c5%2BAIuMkJyG4r8gGzLlA70A%2FGTYjGnow%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX196I%2B8X0LtlYCb6Uu4GNJ5%2BsoHaQLf0vH0%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX18coVyT%2Fy0MiW47iQ%2BLmEzKGKnyZ%2BcyUVpflvrKFj2mvZZvVZrrIuMzaZK2XY3uxh9xH5UPBALkPQ%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX19oUlQhJ1m4%2BEFJboceNJspszLzpUfd%2FvfhAzgKpg9znPKDhBKqthmJlN%2FBnI3tZLOZG6hzitD%2FvVA936cfGTdK0LkDgddq6l6Whp1WtJXPR1kj%2FxeM6int0AfdZoXw4DuFXRZUQNDVNw%3D%3D",
        "Origin": "https://blur.io",
        "Referer": "https://blur.io/",
        "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    }

start_time = time.time()
print("collecting collection information....")
all_data = fetch_all_data(initial_url, headers)
end_time = time.time()

if all_data:
        save_to_json(all_data)
        print("Data saved to blur_data.json")

        time_taken = end_time - start_time
        print(f"Time taken to fetch all data: {time_taken} seconds")


