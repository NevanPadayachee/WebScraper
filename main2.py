from bs4 import BeautifulSoup as bs
import requests

def get_url(search_term):
    temp = "https://www.amazon.com/s?k={}&ref=nb_sb_noss"
    search_term = search_term.replace(' ', '+')
    return temp.format(search_term)

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

url = "https://www.amazon.com/Acer-SB220Q-Ultra-Thin-Frame-Monitor/dp/B07CVL2D2S/ref=sr_1_3?dchild=1&keywords=monitor&qid=1613041666&sr=8-3"
page = requests.get(url, headers=headers)

soup = bs(page.content, 'html.parser')

print(soup.prettify())