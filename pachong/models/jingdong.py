import json
import requests
from bs4 import BeautifulSoup
from requests import RequestException


def download(url, headers, num_retries=3):
    print("download", url)
    try:
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException as e:
        print(e.response)
        html = ""
        if hasattr(e.response, 'status_code'):
            code = e.response.status_code
            print('error code', code)
            if num_retries > 0 and 500 <= code < 600:
                html = download(url, headers, num_retries - 1)
        else:
            code = None
        return html


def get_json():
    jd_html = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=8674557,100000769466,8443496,100000769432,100000117782,100000679465,100000863175,100000612187,8461498,8461490,8461496,7765111,100001045546,7999189,100000667974,100001045648,6072622,100000644947,100002470752,8484118,7690501,7621213,8596169,100000863245,100001045514,100001269968,100001692089,100000863247,100000400472,100001521818&callback=jQuery9848036&_=1546399791459"
    headers = {
        'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        "referer": "https://www.jd.com"
    }
    get = download(jd_html, headers=headers)
    print(get)


if __name__ == "__main__":
    get_json()
