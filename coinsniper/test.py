import pandas as pd

scraped = pd.read_html('https://coinsniper.net/new?page=1')

for idx, table in enumerate(scraped):
    print("************")
    print(idx)
    print(table)