
import requests

headers: dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en;q=0.8',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'core-api.prod.blur.io',
    'Origin': 'https://blur.io',
    'Connection': 'keep-alive',
    'Referer': 'https://blur.io/',
    # 'Cookie': 'rl_session=RudderEncrypt%3AU2FsdGVkX1%2BiKD7%2Fmsx0d8RNLulZtHqOyXMPi7DH0Wj%2FlWlFtZWalRPs3uOzNBnZUI99LALysFw3wsciJZ4XOKKBdEejmKbyOpqfSAkQ6tYku06EBshSKZ8ugqc7xJAwpr8Ucvn1EViCq9%2B2OH2Y%2BQ%3D%3D; __cf_bm=HZYHia3Jtb7Qu9Vys15Z6ao1pBVorJO3qVGCZai7EOw-1701674502-0-Aa49w1SRqx236JC3TQj84YUr3Bvzg06sPKHZvSxtYUV0Fp6Vlj7HLSW9FLVSFoPbOoU5BQp/BQNx8TRHMk2dPwI=; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FmMBLg4RACJHkxi6iB0htt8xfcfG88ecNXJG9wgAD8SWYjKylIlnNQHgkFMYZMnghJtBTpVpEUow%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19023c0IQ9iTCW%2F4FD6129UI%2FO9OmiT80Y%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FLPqsbMpsXy%2FraQtfdQ0FVNtO7gDPWraw%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX195Yt3tZ49YB%2BJZLCjtQsVOCXHmfc3a6FQ%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FegYa1BkX1c0KKGsKYRVIBZqx9HUSapX0%3D; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1875dDBWNlNKTWy4j2ETPq2K2jVBn9r8kFpEH3jwU5x5q7EQsPb7sWY; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19ZquLEOTRJ%2FrRlvf1WDHzlnN5O00Kaams%3D',
    'Sec-Fetch-Dest': 'empty',
}

params = {
    'filters': '{"cursor":{"contractAddress":"0xc99c679c50033bbc5321eb88752e89a93e9e83c5","volumeOneDay":"9.784020100502512563"},"sort":"VOLUME_ONE_DAY","order":"DESC"}',
}

response = requests.get('https://core-api.prod.blur.io/v1/collections/', params=params,  headers=headers)
print(response.status_code)
