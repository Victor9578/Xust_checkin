from typing import AsyncGenerator
import requests ,os
from requests import status_codes
import datetime,json
from requests.sessions import cookiejar_from_dict, session

def ck(data,payload,msggg):
    import re
    s = requests.Session()

    data1 = data
    url1 = 'http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd.jsp?'+data1
    headers1 = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'}

    req = s.post(url1,headers =headers1)
    cookies = str(req.headers)
    ckk = re.findall(r'JSESSIONID=[A-Za-z0-9]*',cookies)
    print(cookies)
    print(ckk)



    url2 = 'http://ehallplatform.xust.edu.cn/default/jkdk/mobile/com.primeton.eos.jkdk.xkdjkdkbiz.jt.biz.ext'
    ua = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36'
    ori = 'http://ehallmobile.xust.edu.cn'
    referer = 'http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd_test.jsp?uid=RkE2QjI1N0VBNzZBQjgxMTNFODNFRTE0Q0EwMzMwNUY='
    cn = 'keep-alive'
    payload = payload
    r= s.post(url2 , headers = {'user-agent':ua,'origin':ori,'referer':referer,'connection':cn,'Cookie':ckk[0]},json = payload)

    url3 = 'http://ehallplatform.xust.edu.cn/default/jkdk/mobile/mobJkdkAdd1.jsp?'+data1
    requests.get(url3)

    print(r.text)
    print(r.status_code)
    if '{}' in r.text:
        neirong = '打卡成功了，啾咪！！！'
    else:
        neirong = '打卡失败了，呜呜呜'+r.text

    ID='ww86317246d173f4bf'
    SECRET='aQHCKSgBhPFNxsBcQWohfYuyqKYrjeBiehv4XlzJAH8'
    ra = requests.post("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+ ID + "&corpsecret="+ SECRET)
    raa= ra.text
    rb = re.findall(r'(?<="access_token":").*(?=",)',raa)
    urlsend = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+rb[0]
    msg = {"touser":"WuXiLong","agentid":"1000002","msgtype":"textcard","textcard":{"title" :"XUST打卡","description" : neirong,"url" : " "}}
    msg['touser'] = msggg
    msgg = json.dumps(msg)
    print(msgg)
    t=requests.post(urlsend,data=msgg)

def main():
    
    ntt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nt = datetime.datetime.now().strftime('%Y-%m-%d')
    nt1 = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    data9613 = (
        'uid=RkE2QjI1N0VBNzZBQjgxMTNFODNFRTE0Q0EwMzMwNUY=',
        'uid=RENGQjhBQzkwMkY4Mzg3MzRBREE1NTAzMUVGQTVCRjA=',
        'uid=RDEzRjI0OEFEOUFFNzEwRjlDMjhDNTVFMTMzOUEzNjc=',
        'uid=RkRBRDFDQkVFNTIzNDAxRjc1QkQ0QTRFOUJCNEYyNTA='
    )
    payloadd = {"xkdjkdk":{"procinstid":"","empid":"76838","shzt":"-2","id":"","jrrq1":nt1,"sjh2":"13002982631","jrsfzx3":"是","szdd4":"中国陕西省西安市临潼区","xxdz41":"九号宿舍楼","jrtwfw5":"正常体温:36～37.2℃","jrsfjgwh6":"否","jrsfjghb7":"否","jrsfcxfrzz8":"否","jrsfywhrjc9":"否","jrsfyhbrjc10":"否","jrsfjcgrrq11":"否","jssfyqzysgl12":"否","sfcyglq13":"否","glkssj131":"","gljssj132":"","sfyyqxgzz14":"否","qtxx15":'',"gh":"18409040213","xm":"","xb":"男","sfzh":"","szyx":"地质与环境学院","xydm":"4008","zy":"","zydm":"","bj":"地质工程1802班","bjdm":"4008024","jg":"","yx":"","sfxs":"是","xslx":"1","jingdu":"108.93285","weidu":"34.255","guo":"中国","sheng":"陕西省","shi":"西安市","xian":"临潼区","sfncxaswfx16":"否","dm":"4008024","jdlx":"0","tbsj":ntt,"fcjtgj17Qt":"","fcjtgj17":"","hqddlx":"1","ymtys":"","time":nt}}
    xx = [
       ['13002982631','18409040213','','WuXiLong','陕西省','西安市','莲湖区','教场门77号'],
       ['13891198746','18409040216','','Fan','陕西省','延安市','子长市','张家沟小区'],
       ['15719269901','18409040218','','JiangShanXiaoYanYuYao','陕西省','汉中市','城固县','张骞路春熙花苑'],
       ['18591310709','18409040215','','varvel','陕西省','渭南市','临渭区','老城渭运小区'],
    ]
    for i in range(0,4):
        data = data9613[i]
        payloadd['xkdjkdk']['sjh2'] = xx[i][0]
        payloadd['xkdjkdk']['gh'] = xx[i][1]
        payloadd['xkdjkdk']['xm'] = NAME[i]
        msggg = xx[i][3]
        payload = payloadd
        print(payload)
        ck(data,payload,msggg)

main()
