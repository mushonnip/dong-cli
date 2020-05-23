import requests
from bs4 import BeautifulSoup
import tableprint as tp
import numpy as np

response = requests.get('http://kazefuri.me/')
soup = BeautifulSoup(response.text, 'html.parser')
posts = soup.find_all(class_='grid3')
data = np.empty((0, 2))
for post in posts:
    title = post.find('b').get_text().replace('\n', '')
    link =  post.find('a')['href']
    if post.find(class_='newepisodefloat right bgwhitetr'):
        episode = post.find(class_='newepisodefloat right bgwhitetr').get_text().replace('\nEps.', '')
    data = np.append(data, np.array([[title, episode]]), axis=0)

headers = ['Judul', 'Episode']
tp.table(data, headers, align='left')