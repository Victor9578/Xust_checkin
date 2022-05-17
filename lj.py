# -*- coding: utf8 -*-
import requests,os,json,re
def main():
    cookie = os.environ['COOKIE']
    url = 'https://cloud.jiyunidc.com/user/checkin'

    r = requests.post(url,headers={
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "content-length": "0",
        "cookie": cookie,
        "origin": "https://cloud.jiyunidc.com",
        "referer": "https://cloud.jiyunidc.com/user",
        "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        })
    print(r.text)
    lj_msg = re.findall(r'msg":"(.*?)"',r.text)[0]
    lj_msgg = lj_msg.encode().decode('unicode_escape')
    ID='ww86317246d173f4bf'
    SECRET='aQHCKSgBhPFNxsBcQWohfYuyqKYrjeBiehv4XlzJAH8'
    ra = requests.post("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid="+ ID + "&corpsecret="+ SECRET)
    raa= ra.text
    rb = re.findall(r'(?<="access_token":").*(?=",)',raa)
    urlsend = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+rb[0]
    msg = {"touser":"WuXiLong","agentid":"1000002","msgtype":"textcard","textcard":{"title" :"lj_checkin","description" : event["Message"]+'\n'+r.text+'\n'+lj_msgg,"url" : " "}}
    msgg = json.dumps(msg)
    print(msgg)
    requests.post(urlsend,data=msgg)

main()