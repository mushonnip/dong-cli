import requests
from bs4 import BeautifulSoup

response = requests.get('https://animexin.xyz')
soup = BeautifulSoup(response.text, 'html.parser')

def main():
    pass

if __name__ == "__main__":
    main()