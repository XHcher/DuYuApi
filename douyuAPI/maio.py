import re
import requests




def cryjs():
    with open('crypto-js.js','r')as f:
        js = f.read()
    return js
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
    allfunc = func + '\n'+keyfunc + '\n'+cryjs()
    return allfunc
