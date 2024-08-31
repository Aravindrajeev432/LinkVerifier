import json

import requests


file_path = "valid_ips.json"
with open(file_path, "r", encoding="utf-8") as json_file:
    proxies:list[str] = json.load(json_file)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "_ga=GA1.2.683743457.1711516675; _ga_C09NSBBFNH=GS1.1.1711516674.1.1.1711516788.0.0.0; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX18WFP6ESiYxvGknNvKZwvUyNwtCd3YLuX4%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2BLaMjsaRNe3KRwOJU%2FNdPzZPEr7Teos0E%3D; __cf_bm=69wsiQ1wKlQ9A39205LuESy23m01MauaViCoFzlM6QY-1711606769-1.0.1.1-AWy4MFZrPvEojsrKyuT4gqYFgSfGXUdqb57IkP_FS20VoXhTXuW0rW.Mo3D3TqnxwY.qhGuWKD5N5TLMNWXRmA; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2BdgGtCGHTPdq9aNF8tPaYJoqnhE5mzBBw%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX18DENqnHylpO%2FukZPqAa%2FSnp7gcoVTgdcs%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18cH6Qq5277BnKackQcdSFvXoA98sL8tlA%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18Q7wxo7bV8DTX9eBGiywnku33%2FT1GnF3E%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19jZ6BcTbYFJNKsEQUAnJiZFKfvr09l%2FJlHuV3OveWxk8Y%2Fm4P6v5Xg1w7NtAPdtZGeQSWmWK4UIA%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BtWZcyIQtof0QQMNH79M9HcO0U6%2F49q%2BMuAvtpr2Bvzl2KezVLhiNvJ73hyivdx9SQYG9PmewenkvIRTOFL3z50xi9gRacE0zqXRwozukV5piQV7qj%2BFA5KHy3FB94Y4MrobfnS6wqnA%3D%3D",
    "f-None-Match": 'W/"11e-J71MkGrfI5JPwChTpPTaXgGZh1s"',
    "Origin": "https://blur.io",
    "Referer": "https://blur.io",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
}

for proxy in proxies:
    print(proxy)
    try:
        res = requests.get('https://core-api.prod.blur.io/v1/collections/0xbd3531da5cf5857e7cfaa92426877b022e612cf8/socials',
                        proxies={'https':proxy},headers=headers, timeout=5)
        j = res.json()
    except Exception as e:
        print(e)
        print(f'{proxy} failed')
        print("remove from list")
