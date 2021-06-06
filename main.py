import argparse
import browser_cookie3
import dill
import json
import requests

ACT_ID = 'e202102251931481'
DOMAIN_NAME = '.mihoyo.com'


def getCookies(browser):
    if browser.lower() == 'chrome':
        return browser_cookie3.chrome(domain_name=DOMAIN_NAME)
    elif browser.lower() == 'firefox':
        return browser_cookie3.firefox(domain_name=DOMAIN_NAME)
    elif browser.lower() == 'edge':
        return browser_cookie3.edge(domain_name=DOMAIN_NAME)
    else:
        return None


def getStatus(cookies):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.5',
        'Origin': 'https://webstatic-sea.mihoyo.com',
        'Connection': 'keep-alive',
        'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={ACT_ID}',
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
         'Referer': f'https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id={ACT_ID}',
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


def encodeCookie(dict_):
    output = {}
    for key in dict_:
        output.update({key.encode('utf-8'): dict_[key].encode('utf-8')})
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--browser",
        help='Set the browser that you use to claim daily reward\nCurrently only supports Chrome, Firefox and Edge')
    args = parser.parse_args()

    if (args.browser is not None):
        cookies = getCookies(str(args.browser))
        with open('cookie', 'wb') as file:
            dill.dump(obj=cookies, file=file)
    else:
        with open('cookie', 'rb') as file:
            cookies = dill.load(file)

    response = getStatus(cookies)
    if not response['data']['is_sign']:
        response = claimReward(cookies)
