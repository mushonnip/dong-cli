from threading import Thread
import requests
from bs4 import BeautifulSoup

response = requests.get('https://animexin.xyz')
soup = BeautifulSoup(response.text, 'html.parser')

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
        if temp != None:
          result.append(temp)  
    return result

def main():
    print('[1] Today Updates')
    print('[2] Latest Updates')
    print('[3] Search Donghua')
    option = int(input('Masukkan pilihan: '))
    while option != 0:
        if option == 1:
            break
        elif option == 2:
            break
        else:
            break


if __name__ == "__main__":
    main()