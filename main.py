import requests 
import time
import os
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
s = requests.Session()

# score:>80 -animated 1girl rating:safe  solo -from_behind -realistic
response = s.get('https://danbooru.donmai.us/login',headers = headers)
soup = BeautifulSoup(response.content, features='lxml')
fst = soup.find('input', attrs={"name" : "authenticity_token"})
token = fst['value']
data = {'authenticity_token':token,
        'session[name]':'',
        'session[password]': '',
        'commit': 'Login'
}
re = s.post('https://danbooru.donmai.us/session',headers = headers, data = data)
pa = {'tags':'-realistic',
    'page':'1'}

    
for p in range(1,30):
    pa['page'] = str(p)
    response = s.get("https://danbooru.donmai.us/posts",params = pa,headers = headers)
    soup = BeautifulSoup(response.content, features='lxml')
    fst = soup.find('div', {"class": "user-disable-cropped-false"})
    snd = fst.find_all('article')
    if not os.path.exists('img'):
        os.makedirs('img')
    print(p)
    for e in snd:
        imgurl = e['data-large-file-url']
        imgname =  imgurl.split('/')[-1]
        t = s.get(imgurl, stream=True)
        print(imgurl)
        with open('img/'+imgname, 'wb') as f:
            f.write(t.content)

while True:
    a = 1