from typing import AsyncGenerator
import requests ,os,re
from requests import status_codes
import datetime

ntt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
nt = datetime.datetime.now().strftime('%Y-%m-%d')
nt1 = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')

def ck():
    url = 'http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd.jsp'
    data = {'uid':'RkE2QjI1N0VBNzZBQjgxMTNFODNFRTE0Q0EwMzMwNUY='}
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'}

    req = requests.post(url,data=data,headers =headers)
    cookies = req.headers['Set-Cookie']
    ckk = (re.findall(r'\s*([^\"]+); Path=/default',cookies))
    ckkk = ckk[0]
    print(ckkk)
    return ckkk

def start(cookie):
    sckey = 'SCT8420Tj8Jsg1kXgply7DHe5JxOVzzA'
    url = 'https://ehallplatform.xust.edu.cn/default/jkdk/mobile/com.primeton.eos.jkdk.xkdjkdkbiz.jt.biz.ext'
    ua = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'
    # cookie = 'JSESSIONID=0806C1E3FD59615A594BE72728C21A51; JSESSIONID=7FFAA9AD5F0093316B95DB8EF0CF0B36'
    ori = 'http://ehallmobile.xust.edu.cn'
    re = 'https://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid=RkE2QjI1N0VBNzZBQjgxMTNFODNFRTE0Q0EwMzMwNUY='
    cn = 'keep-alive'
    payload = 

    r = requests.get(url , headers = {'user-agent':ua,'origin':ori,'referer':re,'connection':cn,'Cookie':cookie},data = payload)

    r.text
    print(r.text)
    print(r.status_code)
    requests.get('https://sctapi.ftqq.com/' + sckey + '.send?title= '+ r.text)

def main_handler(event, context):
    cookie=ck()
    print(cookie)
    return  start(cookie)
if __name__ == '__main__':
    print(main_handler(None,None))

