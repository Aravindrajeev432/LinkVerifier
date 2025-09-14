import time
import json

from bs4 import BeautifulSoup


page: int = 0
tables: list = []
all_links: list = []


# url = f"https://www.coingecko.com/?items=300&page={page}"
with open("gecko.html", "r", encoding="utf-8") as f:
    html_page = f.read()
soup = BeautifulSoup(html_page, 'html.parser')
table = soup.find("div", {"class": "gecko-sticky-table-wrapper"})

if table:
    print("inside table")
    all_page_links: list = table.find_all(
        "a", href=lambda href: href and "en" in href
    )
    for link in all_page_links:

        if "www.coingecko.com" in link.get("href"):
            # redirect link
            all_links.append(link.get("href"))
        else:
            page_link = f"https://www.coingecko.com{link.get('href')}"
            all_links.append(page_link)
        

all_coin_links: list = list(set(all_links))
print(len(all_coin_links))
try:
    file_path = "all_coins_links.json"
    with open(file_path, "r", encoding="utf-8") as f:
        existing_links = json.load(f)
except FileNotFoundError:
    existing_links = []
all_coin_links.extend(existing_links)
all_coin_links = list(set(all_coin_links))

with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(all_coin_links, json_file, indent=2)
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()
#

# message = driver.find_element(by=By.ID, value="message")
# text = message.text


