from bs4 import BeautifulSoup as bs
from selenium import webdriver

def get_takealot_url(search_term):
    temp = "https://www.takealot.com/all?_sb=1&_r=1&_si=34561dea791c4dd754020d0411807e90&qsearch={}"
    search_term = search_term.replace(' ','%20')
    return temp.format(search_term)

def takealot_prices(item):
    driver = webdriver.Chrome()
    temp = get_takealot_url(item)
    driver.get(temp)

    soup = bs(driver.page_source, 'html.parser')
    results = soup.findAll('div', {'class': 'cell small-4'})
    return results


print(takealot_prices("monitors"))