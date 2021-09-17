import requests
from loguru import logger
import parsel
import re
import execjs
import time
import js2py

url = 'https://www.douyu.com/22619'

headers = {
    'referer': 'https://www.douyu.com/22619',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
}

r = requests.get(url, headers=headers).text
# func = re.search("(function ub98484234.*?)return.*?];", r).group(0)
# with open('douyu.js', 'w', encoding='utf-8')as f:
#     jscode = f.write(func)
print(r)

# with open('douyu.js', 'r', encoding='utf-8')as f:
#     jscode = f.read()
xx0 = '5551871'
xx1 = str(int(time.time()))
xx2 = 'ca1f68a016f39ab829cc86f600031601'
# url = f'http://app.sjdshd.com/dy/dyjs.php?roomId=22619'
# rsp = requests.get(url)
# data = rsp.text
with open('douyu.js', 'r', encoding='utf8')as dou_yu, open('crypto-js.js', 'r', encoding='utf8') as crypto:
    # print(f'{dou_yu.read()}{crypto.read()}')
    context = js2py.EvalJs()
    context.execute(f'{dou_yu.read()}{crypto.read()}')
    print(f"{context.ub98484234(xx0, xx1, xx2)}")
# context = js2py.EvalJs()
# context.execute(data)
# print(f"{context.ub98484234(xx0, xx1, xx2)}")
#
# code = execjs.compile(jscode)
# dos  = code.call('ub98484234',xx0,xx1,xx2)
# print(dos)




