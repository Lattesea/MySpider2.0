import requests


def handle_douyin_web_share():
    share_web_url = 'https://www.douyin.com/share/user/' + task['share_id']
    print(share_web_url)
    share_web_header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    }
    share_web_response = requests.get(url=share_web_url, headers=share_web_header)
    # handle_decode(share_web_response.text, share_web_url, task)