import requests
from bs4 import BeautifulSoup
import re

#  忽略警告代码
requests.packages.urllib3.disable_warnings()

def GetRealUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.get(url, headers=headers, allow_redirects=False,verify=False)
    share_url = response.headers['Location']
    # print(share_url)

    share_response = requests.get(share_url,headers=headers,verify=False).text
    # print(share_response)

    # 通过BeautifulSoup提取无水印播放地址字符串
    soup = BeautifulSoup(share_response,'lxml')
    noWaterMarkVideo = soup.find(attrs={'id': 'hide-pagedata'}).attrs['data-pagedata']

    # print(noWaterMarkVideo)

    # 正则处理字符串获取真实地址
    pattern = re.compile('\"srcNoMark\":"(.*?)"},',re.S)

    real_url = re.findall(pattern,noWaterMarkVideo)[0]

    print(real_url)


if __name__ == '__main__':
    # 这里写视频地址
    GetRealUrl('https://f.kuaishou.com/2O9B0g')
