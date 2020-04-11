import requests
from bs4 import BeautifulSoup

def GetRealUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    share_url = response.headers['Location']

    share_response = requests.get(share_url,headers=headers).text
    # print(share_response)

    # 通过beautifulSoup获取带水印的播放地址
    soup = BeautifulSoup(share_response,'lxml')
    waterMarkVideo = soup.find(attrs={'id':'theVideo'}).attrs['src']

    # 替换带水印播放地址中的'playwm'为'play'
    noWaterMarkVideo = waterMarkVideo.replace('playwm','play')

    # 使用手机的user-agent获取header中的真实地址
    real_url = requests.get(noWaterMarkVideo,headers=headers,allow_redirects=False).headers["Location"]

    print(real_url)

if __name__ == '__main__':
    # 这里写视频地址
    GetRealUrl('https://v.douyin.com/cr5jfa/')
