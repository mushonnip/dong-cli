import requests
from bs4 import BeautifulSoup
import os
from dateutil import parser
from datetime import datetime
import subprocess

response = requests.get('https://animexin.xyz')
soup = BeautifulSoup(response.text, 'html.parser')
detail = []

def get_stream_url(args):
    pass

def get_latest_single(data):
    donghua = data.find('a')
    if donghua.find(class_='eggepisode'):
        return {
            'url': donghua['href'],
            'title': donghua['title']
        }

def get_latest():
    entries = soup.find(class_='excstf').find_all('article')
    result = []
    for x in entries:
        temp = get_latest_single(x)
        if temp:
          result.append(temp)
    return result

def get_today():
    latest = get_latest()
    res = []
    for i, x in enumerate(latest, 0):
        detail.append(requests.get(x['url']))
        s = BeautifulSoup(detail[i].text, 'html.parser')
        date = s.find(class_='updated').text
        d = parser.parse(date)
        if d.date() == datetime.today().date():
            print('[{}] {title}'.format(i+1, **x))
            res.append(x)
        else:
            break
    return res
            

def option_today():
    os.system('clear')
    get_today()
    
    opt = int(input('Pilih Donghua: '))
    link = BeautifulSoup(detail[opt-1].text, 'html.parser').find('iframe').get('src')
    subprocess.run(['mpv','--no-terminal',link])
    os.system('clear')
    main()

def option_latest():
    pass

def option_search():
    pass

def main():
    print('[1] Today Updates')
    print('[2] Latest Updates')
    print('[3] Search Donghua')
    option = int(input('Masukkan pilihan: '))
    if option == 1:
        option_today()
    elif option == 2:
        pass
    else:
        pass


if __name__ == "__main__":
    main()