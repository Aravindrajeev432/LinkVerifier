import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
page: int = 0
tables: list = []
all_links: list = []
while True:
    page += 1
    url = f"https://www.coingecko.com/?items=50&page={page}"
    driver.get(url)
    driver.implicitly_wait(2.5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find("div", {"class": "tw-overflow-x-auto 2lg:tw-overflow-x-visible 2lg:tw-flex 2lg:tw-justify-center"})
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
        print("all links")


        break
    else:
        break

all_coin_links: list = list(set(all_links))
print(len(all_links))
file_path = "all_coins_links.json"
with open(file_path, "w", encoding="utf-8") as json_file:
    json.dump(all_coin_links, json_file, indent=2)
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()
#

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

driver.quit()
