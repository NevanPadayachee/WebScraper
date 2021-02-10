from bs4 import BeautifulSoup as bs
from selenium import webdriver
import requests
import csv

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


print(dollar_to_rand()[0])