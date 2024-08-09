import requests
from bs4 import BeautifulSoup

def scrape_website(url: str, tag: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(tag)
    return [element.text for element in elements]
