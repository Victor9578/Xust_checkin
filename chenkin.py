from typing import AsyncGenerator
import requests ,os
from requests import status_codes
import datetime

ntt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
nt = datetime.datetime.now().strftime('%Y-%m-%d')
nt1 = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')

def start():
    sckey = 'SCT8420Tj8Jsg1kXgply7DHe5JxOVzzA'
    url = 'https://ehallplatform.xust.edu.cn/default/jkdk/mobile/com.primeton.eos.jkdk.xkdjkdkbiz.jt.biz.ext'
    ua = 'Mozilla/5.0 (Linux; Android 11; M2006J10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045513 Mobile Safari/537.36 MMWEBID/8445 MicroMessenger/8.0.1.1840(0x28000159) Process/tools WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64'
    cookie = 'JSESSIONID=0806C1E3FD59615A594BE72728C21A51; JSESSIONID=7FFAA9AD5F0093316B95DB8EF0CF0B36'
    ori = 'http://ehallmobile.xust.edu.cn'
    re = 'https://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid=RkE2QjI1N0VBNzZBQjgxMTNFODNFRTE0Q0EwMzMwNUY='
    cn = 'keep-alive'
    payload = {"xkdjkdk":{"procinstid":"","empid":"76838","shzt":"-2","id":"","jrrq1":nt1,"sjh2":"13002982631","jrsfzx3":"否","szdd4":"中国陕西省西安市莲湖区","xxdz41":"教场门77号","jrtwfw5":"正常体温:36～37.2℃","jrsfjgwh6":"否","jrsfjghb7":"否","jrsfcxfrzz8":"否","jrsfywhrjc9":"否","jrsfyhbrjc10":"否","jrsfjcgrrq11":"否","jssfyqzysgl12":"否","sfcyglq13":"否","glkssj131":"","gljssj132":"","sfyyqxgzz14":"否","qtxx15":'',"gh":"18409040213","xm":"仵西龙","xb":"男","sfzh":"","szyx":"地质与环境学院","xydm":"4008","zy":"","zydm":"","bj":"地质工程1802班","bjdm":"4008024","jg":"","yx":"","sfxs":"是","xslx":"1","jingdu":"108.93285","weidu":"34.255","guo":"中国","sheng":"陕西省","shi":"西安市","xian":"莲湖区","sfncxaswfx16":"否","dm":"4008024","jdlx":"0","tbsj":ntt,"fcjtgj17Qt":"","fcjtgj17":"","hqddlx":"1","ymtys":"","time":nt}}

    r = requests.get(url , headers = {'user-agent':ua,'origin':ori,'referer':re,'connection':cn,'cookie':cookie},data = payload)

    r.text
    print(r.text)
    print(r.status_code)
    requests.get('https://sctapi.ftqq.com/' + sckey + '.send?title= '+ r.text)

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()
