from typing import AsyncGenerator
import requests ,os
from requests import status_codes
import datetime

ntt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
nt = datetime.datetime.now().strftime('%Y-%m-%d')
nt1 = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')

url = 'https://ehallplatform.xust.edu.cn/default/jkdk/mobile/com.primeton.eos.jkdk.xkdjkdkbiz.jt.biz.ext'

ck = 'JSESSIONID=187A247B22A5147B69F46F695C65A466; JSESSIONID=2E0B3E4B32F82897F4D3A30D4879DF84'
ua = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'
payload = {"xkdjkdk":{"procinstid":"","empid":"76838","shzt":"-2","id":"","jrrq1":nt1,"sjh2":"13002982631","jrsfzx3":"否","szdd4":"中国陕西省西安市碑林区","xxdz41":"教场门77号","jrtwfw5":"正常体温:36～37.2℃","jrsfjgwh6":"否","jrsfjghb7":"否","jrsfcxfrzz8":"否","jrsfywhrjc9":"否","jrsfyhbrjc10":"否","jrsfjcgrrq11":"否","jssfyqzysgl12":"否","sfcyglq13":"否","glkssj131":"","gljssj132":"","sfyyqxgzz14":"否","qtxx15":'',"gh":"18409040213","xm":"仵西龙","xb":"男","sfzh":"","szyx":"地质与环境学院","xydm":"4008","zy":"","zydm":"","bj":"地质工程1802班","bjdm":"4008024","jg":"","yx":"","sfxs":"是","xslx":"1","jingdu":"108.93285","weidu":"34.255","guo":"中国","sheng":"陕西省","shi":"西安市","xian":"碑林区","sfncxaswfx16":"否","dm":"4008024","jdlx":"0","tbsj":ntt,"fcjtgj17Qt":"","fcjtgj17":"","hqddlx":"1","ymtys":"","time":nt}}

r = requests.get(url,headers = {'cookie':ck ,'user-agent': ua },data=payload)

print(r.status_code)
print(r.text)

