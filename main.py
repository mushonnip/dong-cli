import requests
from bs4 import BeautifulSoup

response = requests.get('http://kazefuri.me/')
soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='grid3')
for post in posts:
    title = post.find('b').get_text().replace('\n', '')
    link =  post.find('a')['href']
    if post.find(class_='newepisodefloat right bgwhitetr'):
        episode = post.find(class_='newepisodefloat right bgwhitetr').get_text().replace('\nEps.', '')
    print(title, episode, link)