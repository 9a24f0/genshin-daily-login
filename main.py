import requests
import browser_cookie3
import json

ACT_ID = 'e202102251931481'
DOMAIN_NAME = '.mihoyo.com'


def getCookies():
    cookies = browser_cookie3.firefox(domain_name=DOMAIN_NAME)
    return cookies


def getStatus(cookies):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.5',
        'Origin': 'https://webstatic-sea.mihoyo.com',
        'Connection': 'keep-alive',
        'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={ACT_ID}&lang=vi-vn',
        'Cache-Control': 'max-age=0',
   }

    params = (
        ('lang', 'vi-vn'),
        ('act_id', ACT_ID)
    )

    try:
        response = requests.get('https://hk4e-api-os.mihoyo.com/event/sol/info',
                                headers=headers, params=params, cookies=cookies)
        return response.json()

    except Exception as e:
        print("Error: ", e)
        return None


def claimReward(cookies):
    headers = {
         'Accept': 'application/json, text/plain, */*',
         'Accept-Language': 'vi-VN,vi;q=0.5',
         'Content-Type': 'application/json;charset=utf-8',
         'Origin': 'https://webstatic-sea.mihoyo.com',
         'Connection': 'keep-alive',
         'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={ACT_ID}&lang=vi-vn',
    }


    params = (('lang', 'vi-vn'),)


    json =  { 'act_id': ACT_ID }

    try:
        response = requests.post('https://hk4e-api-os.mihoyo.com/event/sol/sign',
                                headers=headers, params=params,
                                cookies=cookies, json=json)
        return response.json()

    except Exception as e:
        print("Error: ", e)
        return None


if __name__ == '__main__':
    cookies = getCookies()
    response = getStatus(cookies)
    if not response['data']['is_sign']:
        response = claimReward(cookies)
