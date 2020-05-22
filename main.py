import requests
from bs4 import BeautifulSoup

response = requests.get('http://kazefuri.me/')
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='grid3')

for post in posts:
    print(post)