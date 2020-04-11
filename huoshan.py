import requests
#  忽略警告代码
requests.packages.urllib3.disable_warnings()

# 获取字符串中指定字符
def getMidString(html, start_str, end):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end]

def getRealUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }

    # 重定向地址
    response = requests.get(url, headers=headers, allow_redirects=False,verify=False)

    item_id = getMidString(response.headers["Location"], 'item_id=', '&tag=')

    api_url = 'https://share.huoshan.com/api/item/info?item_id=' + item_id

    api_response = requests.get(api_url,headers=headers,verify=False).json()

    waterMarkVideo = api_response['data']['item_info']['url']

    # 替换reflow为resource mark=2为mark=0
    noWaterMarkVideo = waterMarkVideo.replace('reflow','source').replace('mark=2','mark=0')

    print(noWaterMarkVideo)

if __name__ == '__main__':
    getRealUrl('https://share.huoshan.com/hotsoon/s/yvCRrUngm78/')