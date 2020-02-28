import requests
from requests.auth import HTTPBasicAuth
import json

server = 'http://121.41.43.141:8880/'

url = 'https://aweme-hl.snssdk.com/aweme/v1/commit/item/digg/?aweme_id=6798030229194525965&type=1&channel_id=0&manifest_version_code=920&_rticket=1582705896535&app_type=normal&iid=97500286766&channel=wandoujia_aweme2&device_type=Nexus_6P&language=zh&uuid=867686022307696&resolution=1440*2392&openudid=23f919d5e27ff2ed&update_version_code=9202&cdid=31823612-954c-4bf9-88b6-c4032e498af7&os_api=27&dpi=560&ac=wifi&device_id=67047745479&os_version=8.1.0&version_code=920&app_name=aweme&version_name=9.2.0&device_brand=google&ssmix=a&device_platform=android&aid=1128&ts=1582706009'

cookie = 'd_ticket=a6eef25e70eec1832f3e0cc26679e59392999; sid_guard=ddd400e867e28f993095309d800e2b48%7C1582711147%7C5184000%7CSun%2C+26-Apr-2020+09%3A59%3A07+GMT; uid_tt=16d69c042cad4490247bc838b8d197a0; sid_tt=ddd400e867e28f993095309d800e2b48; sessionid=ddd400e867e28f993095309d800e2b48; odin_tt=be07257f026c9b9005872270b7e2a3fbcc5d35693fd49ce22615b641da7ade4854d596adc4937ef0d1848ae6a55657a1'
body = ''

content_type = ''

user = ''
password = ''

resp = requests.post(url=server+'douyin/calc/xg', data={'url': url, 'cookie': cookie, 'body': body, 'dy_http_method': "get", "token":"199385623ef1da00e51b88303a6a914e"}, headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}, auth=HTTPBasicAuth(user, password))
print(resp.text)
headers = resp.json()['data']["headers"]
headers["Cookie"] = cookie
headers['User-Agent'] = 'com.ss.android.ugc.aweme/920 (Linux; U; Android 8.1.0; zh_CN_#Hans; Nexus 6P; Build/OPM7.181205.001; Cronet/TTNetVersion:4df3ca9d 2019-11-25)'


resp = requests.get(url=url, headers=headers)
print(resp.text)
