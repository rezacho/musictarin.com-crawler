import requests
from bs4 import BeautifulSoup

singers_list = []
chosen_singer = ''
scraped_data = []


# SEND A REQUEST AND RETURN HTML CONTENT AS TEXT
def get_page(url):
    try:
        response = requests.get(url)
    except:
        return None
    return response.text


# GET ALL AVAILABLE SINGERS ON SITE
def get_all_singers(html_doc):
    soap = BeautifulSoup(html_doc)
    content = soap.find('section', attrs={'class': 'umbox'})
    return content.find_all('a')


# GET ALL CHOSEN SINGER SONGS AND STORE THE LINKS
def get_singer_musics(html_doc):
    all_singer_musics = []
    soap = BeautifulSoup(html_doc)
    contents = soap.find_all('a', attrs={'class': 'umsngl'})
    for content in contents:
        all_singer_musics.append(content.get('href'))
    return all_singer_musics


# GET DOWNLOAD LINK AND TITLE OF THE CHOSEN SINGER
def fetch_data(html_doc):
    soap = BeautifulSoup(html_doc)
    title = soap.find('header', attrs={'class': 'aflex'}).find('a').get('title')
    download_link = soap.find('div', attrs={'class': 'umdl'}).find('a').get('href')
    scraped_data.append((title, download_link))
