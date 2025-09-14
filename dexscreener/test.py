# import the required libraries
from bs4 import BeautifulSoup
import nodriver as uc
import asyncio

async def scraper():

    # start a new Chrome instance
    driver = await uc.start()

    # visit the target website
    page = await driver.get("https://dexscreener.com/gainers/page-1?min24HTxns=300&min24HSells=30")

    # get the full-page HTML
    html_content = await page.get_content()
    # print(html_content)
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("div", {"class": "ds-dex-table ds-dex-table-top"})
    if table:
        print("table found")
    else:
        print("table not found")

    # close the page
    await page.close()

# run the scraper function with asyncio
if __name__ == "__main__":
    asyncio.run(scraper())
