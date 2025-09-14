import requests

cookies = {
    '__cf_bm': 'S7.QKHyLrSOSk2iLGQqu3XXCjCgIHWvXfRMWeK_N5F8-1725165924-1.0.1.1-Vrn2sSZ_G7l9DaAEmaMzFZ1uCm8JY4oV7brUUevHYPApbwrGsljbJJqG.GJ2R8dVVNccipzirEnBBvVU6.Px5.dRD0YRXAjZqp0WyynKRws',
    'chakra-ui-color-mode': 'dark',
    '_ga': 'GA1.1.587883010.1725165929',
    'cf_clearance': 'G8zq6wUUDldf9aG7C1aAfso9s6BxgVQeJCCTiYEz3CQ-1725166753-1.2.1.1-SG2PrElu6AoawOQoY04mYCkPONk6aehX9TEBG6I5l8f0UFu1IdET4ekBzLy8nUy6Fai5AIj5yn6kXEDSespu7ys.H_ShyEsiHFdB.XMP_6qKJbOucBu5bW.3wUZzgNcw8iB3VUaZSIqN1rFdbH8GNNHpp9CmTTTuhuthcM1_vlM.zvikNYAccgwERU8MALxoyM3cW4Ozr3hBxHgzQEGXQqn_kZjUVuib5ykNKGSjSTyPAf6Qj0P8UkNMwsXde1ImcEkZGTsRVcScgVjiLrA.D6r9fZjqpEmk0KHDvRoNtfuDqgiIHWx3ZbglFseDzneI8DCY_h9MKjk0bleNqp6N3SCAVZEwZ.5gQC3ZRgldoacNUxA_64MTwRj7qVj1PMMmj_jr4iqShKx175aeLCy7Z84TUtfIHOONBUYd9y8D.WAt3L0HIO6lKX3FvHEQR5Fb',
    '_ga_532KFVB4WT': 'GS1.1.1725165928.1.1.1725167142.60.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__cf_bm=S7.QKHyLrSOSk2iLGQqu3XXCjCgIHWvXfRMWeK_N5F8-1725165924-1.0.1.1-Vrn2sSZ_G7l9DaAEmaMzFZ1uCm8JY4oV7brUUevHYPApbwrGsljbJJqG.GJ2R8dVVNccipzirEnBBvVU6.Px5.dRD0YRXAjZqp0WyynKRws; chakra-ui-color-mode=dark; _ga=GA1.1.587883010.1725165929; cf_clearance=G8zq6wUUDldf9aG7C1aAfso9s6BxgVQeJCCTiYEz3CQ-1725166753-1.2.1.1-SG2PrElu6AoawOQoY04mYCkPONk6aehX9TEBG6I5l8f0UFu1IdET4ekBzLy8nUy6Fai5AIj5yn6kXEDSespu7ys.H_ShyEsiHFdB.XMP_6qKJbOucBu5bW.3wUZzgNcw8iB3VUaZSIqN1rFdbH8GNNHpp9CmTTTuhuthcM1_vlM.zvikNYAccgwERU8MALxoyM3cW4Ozr3hBxHgzQEGXQqn_kZjUVuib5ykNKGSjSTyPAf6Qj0P8UkNMwsXde1ImcEkZGTsRVcScgVjiLrA.D6r9fZjqpEmk0KHDvRoNtfuDqgiIHWx3ZbglFseDzneI8DCY_h9MKjk0bleNqp6N3SCAVZEwZ.5gQC3ZRgldoacNUxA_64MTwRj7qVj1PMMmj_jr4iqShKx175aeLCy7Z84TUtfIHOONBUYd9y8D.WAt3L0HIO6lKX3FvHEQR5Fb; _ga_532KFVB4WT=GS1.1.1725165928.1.1.1725167142.60.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"127.0.6533.122"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.122", "Chromium";v="127.0.6533.122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.6.1"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'min24HTxns': '300',
    'min24HSells': '30',
}

response = requests.get('https://dexscreener.com/gainers', params=params, cookies=cookies, headers=headers)
print(response.text)