import requests
from loguru import logger
import parsel
import re
import execjs
import time
import js2py


def get_room(room_id):
    url = f'https://www.douyu.com/{room_id}'

    headers = {
        'referer': f'https://www.douyu.com/{room_id}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    }

    r = requests.get(url, headers=headers).text
    func = re.search("(function ub98484234.*?)return.*?;}", r).group(0)
    funcc = re.search("var v =(.*).slice\(0\);", func).group(1)
    keyfunc = re.search(f'var{funcc}(.*?)];',r).group(0)
    with open('douyusss.js', 'w', encoding='utf-8')as f:
        f.write(func)
        f.write(keyfunc)
    try:
        roomid = re.search("\$ROOM.room_id =(\d+);", r).group(1)
        return roomid
    except Exception as e:
        logger.error(e)
        roomid = re.search("\\$ROOM.room_id =(.*?);", r).group(1).split(' ')[1]
        return roomid


def sign(xx0):
    xx1 = str(int(time.time()))
    xx2 = 'ca1f68a016f39ab829cc86f600031601'
    with open('douyusss.js', 'r', encoding='utf8')as dou_yu, open('crypto-js.js', 'r', encoding='utf8') as crypto:
        context = js2py.EvalJs()
        context.execute(f'{dou_yu.read()}{crypto.read()}')
        sdd = context.ub98484234(xx0, xx2, xx1)
        sdds = sdd.split('&')[-1].replace('sign=', '')
        logger.info(f'SIGN值为:{sdds}')
    return xx1, sdds


def room_data(roomid, xx1, sdds):
    gethf = f'https://www.douyu.com/lapi/live/getH5Play/{roomid}'
    headers = {
        'referer': f'https://www.douyu.com/{roomid}',
        # 'referer':'https: // www.douyu.com / topic / LPLXJS?rid = 5067522',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
    }
    vtime = time.strftime('%Y%m%d',time.localtime())
    vtime = '2201' + str(vtime)
    data = {
        'v': vtime,
        'did': 'ca1f68a016f39ab829cc86f600031601',
        'tt': xx1,
        'sign': sdds,
        'cdn':'',
        'rate': -1,
        'ver': 'Douyu_221083105',
        'iar': 1,
        'ive': 0,
        'hevc': 0,
        'fa': 0
    }
    resp = requests.post(gethf, headers=headers, data=data).text
    if "房间未开播" in resp:
        logger.debug('房间状态:未开播')
    else:
        logger.debug('房间状态:已开播')
    logger.info(resp)
    return resp


if __name__ == '__main__':
    while 1:
        id = input("输入房间号：")
        xx0 = get_room(id)
        logger.info(f"真实房间号:{xx0}")
        xx1,sdds = sign(xx0)
        room_data(xx0,xx1,sdds)
        time.sleep(1)
