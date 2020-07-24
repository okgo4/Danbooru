import requests 
import os
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
s = requests.Session()


#school_swimsuit rating:questionable score:>50 order:score

pa = {'tags':'school_swimsuit rating:questionable score:>50 order:score',
    'page':'1'}
for p in range(1,72): 
    pa['page'] = str(p)
    response = s.get("https://konachan.com/post",params = pa,headers = headers)
    soup = BeautifulSoup(response.content, features='lxml')
    fst = soup.find_all('a', {"class": "directlink"})
    if not os.path.exists('img'):
        os.makedirs('img')
    print(p)
    for e in fst:
        imgurl = e['href']
        imgname =  imgurl.split('/')[-1]
        t = s.get(imgurl, stream=True)
        print(imgurl)
        with open('img/'+imgname, 'wb') as f:
            f.write(t.content)

while True:
    a = 1