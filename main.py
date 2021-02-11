from bs4 import BeautifulSoup as bs
from selenium import webdriver
import csv


def get_amazon_url(search_term):
    temp = "https://www.amazon.com/s?k={}&ref=nb_sb_noss"
    search_term = search_term.replace(' ', '+')
    return temp.format(search_term)


def amazon_price(item):
    driver = webdriver.Chrome()
    temp = get_amazon_url(item)

    driver.get(temp)
    soup = bs(driver.page_source, 'html.parser')
    results = soup.findAll('div', {'data-component-type': 's-search-result'})
    driver.close()

    item_list = []
    for items in results:
        record = amazon_list(items)
        if record:
            item_list.append(record)

    return item_list


def amazon_list(item):
    try :
        atag = item.h2.a
        description = atag.text.strip()
        temp = 'https://www.amazon.com' + atag.get('href')

        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen')

        rating = item.i.text

        results = (description, price.text, rating, temp)
        return results
    except :
        return


def dollar_to_rand():
    test = True
    count = 0
    while test:
        try:
            driver = webdriver.Chrome()
            temp = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=ZAR"
            driver.get(temp)
            soup = bs(driver.page_source, 'html.parser')
            results = soup.find('p', {'class': 'sc-AxjAm ConvertedSubText-fcQdYJ efOulh'})
            driver.close()
            return results.text.split()[0]
        except:
            test = True
            count = count + 1
            if count == 4:
                test = False
            print("failed Attempt ")


list = amazon_price("ryzen 3700")

for items in list :
    print(items)

with open("amazon.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Description', 'Price', 'Rating', 'URL'])
    writer.writerows(list)


