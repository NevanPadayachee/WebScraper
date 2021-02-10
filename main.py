from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import csv

driver = webdriver.Chrome()

url = "https://www.amazon.com/"
driver.get(url)

def get_url(search_term):
    temp = "https://www.amazon.com/s?k={}&ref=nb_sb_noss"
    search_term = search_term.replace(' ', '+')
    return temp.format(search_term)

url=get_url("ryzen 5600")
print(url)
driver.get(url)

soup = bs(driver.page_source, 'html.parser')

results = soup.findAll('div', {'data-component-type' : 's-search-result'})
print(len(results))

item = results[0]
atag = item.h2.a
description = atag.text.strip()
url = 'https://www.amazon.com'+atag.get('href')

price_parent = item.find('span', 'a-price')
price = price_parent.find('span', 'a-offscreen')

rating = item.i.text

def dollar_to_rand():
    test = True
    count = 0
    while(test):
        try:
            temp = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ZAR"
            driver = webdriver.Chrome()
            driver.get(temp)
            soup = bs(driver.page_source, 'html.parser')
            results = soup.find('p', {'class': 'sc-AxjAm ConvertedSubText-fcQdYJ efOulh'})
            return results.text.split()
        except:
            test = True
            count = count + 1
            if count == 4:
                test = False
            print("failed Attempt ")


print(price.text)
#print(str(dollar_to_rand()[0]))
print(rating)