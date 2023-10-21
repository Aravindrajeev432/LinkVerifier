import time
from requests import Session
from icecream import ic
from tqdm import tqdm
from utils import coingecko_code_extracter, is_valid_link_checker
from datetime import datetime
from openpyxl import Workbook

session: Session = Session()
coingecko_url: str = "https://api.coingecko.com/api/v3/coins/list"
coingecko_coin_url = "https://www.coingecko.com/en/coins/"

workbook = Workbook()
worksheet1 = workbook.active
worksheet1.title = "Coingecko Invalid Links"
worksheet2 = workbook.create_sheet(title="Captcha Links")
captcha_row = 1
row = 1
worksheet1.cell(row=1, column=1, value="Currency Name")
worksheet1.cell(row=1, column=2, value="Invalid Discord Link")
worksheet1.cell(row=1, column=3, value="Page Link")
worksheet2.cell(row=captcha_row, column=1, value="Currency Name")
worksheet2.cell(row=captcha_row, column=2, value="Discord Link")
worksheet2.cell(row=captcha_row, column=3, value="Page Link")


coingecko_res = session.get(coingecko_url)
ic(len(coingecko_res.json()))
limit = 0
for coin in tqdm(coingecko_res.json()):
    limit += 1
    code = coingecko_code_extracter(session=session,coin_id=coin.get('id'))
    discord_url = f"https://discord.com/invite/{code}"
    url = f"{coingecko_coin_url}{coin.get('id')}"
    # coingecko's discord link
    if code == "EhrkaCH":
        continue
    if code:
        
        is_valid_link : bool = is_valid_link_checker(session=session,code=code)
        if not is_valid_link:
            
            row += 1
            worksheet1.cell(row=row, column=1, value=coin.get('name'))
            discord_cell  = worksheet1.cell(row=row, column=2, value=discord_url)
            discord_cell.hyperlink = discord_url
            discord_cell.style = 'Hyperlink'
            url_cell = worksheet1.cell(row=row, column=3, value=url)
            url_cell.hyperlink = url
            url_cell.style = 'Hyperlink'
            
    else:
        
        captcha_row += 1
        worksheet2.cell(row=captcha_row, column=1, value=coin.get('name'))
        discord_cell = worksheet2.cell(row=captcha_row, column=2, value=discord_url)
        discord_cell.hyperlink = discord_url
        discord_cell.style = 'Hyperlink'
        url_cell = worksheet2.cell(row=captcha_row, column=3, value=url)
        url_cell.hyperlink = url
        url_cell.style = 'Hyperlink'
    

timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M")

# Create the filename with the timestamp
filename = f"coingecko_invalid_links_{timestamp}.xlsx"

# Save the workbook to the generated filename
workbook.save(filename)