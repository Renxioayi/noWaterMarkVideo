import requests
import re
import json

def get_video_src(vid):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }

    api_url = 'http://vv.video.qq.com/getinfo?vids=' + vid + '&platform=101001&charge=0&otype=json&defn=shd'

    html = requests.get(api_url, headers=headers).text

    # 获取json数据
    p = re.compile(r'({.*})', re.S)
    jsonstr = re.findall(p, html)[0]
    json_data = json.loads(jsonstr)

    # 解析json数据获取url
    baseurl = json_data['vl']['vi'][0]['ul']['ui'][0]['url']
    fn = json_data['vl']['vi'][0]['fn']
    fvkey = json_data['vl']['vi'][0]['fvkey']

    real_url = baseurl + fn + '?vkey=' + fvkey

    print(real_url)

if __name__ == '__main__':
    # url的话自己写个正则匹配即可
    get_video_src('c09457i5ok5')
