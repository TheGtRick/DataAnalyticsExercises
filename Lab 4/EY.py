from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
import openpyxl as opx
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
URL = "https://aliexpress.ru/category/327/mobile-phones.html?SearchText=&g=y&page=1"
driver.get(URL)
content = driver.page_source
soup = bs(content, "html.parser")
ginfo = soup.findAll(class_="product-snippet_ProductSnippet__description__w6hatm")
sphone_table = pd.DataFrame(columns=['Description', 'Price', 'Discount', 'Price Without Discount', 'Shop', 'Sold', 'Rating', 'Delivery'])
wb = opx.Workbook()
writer = wb.active
row = 1
for info in ginfo:
    description = info.find('div', attrs={'class', 'product-snippet_ProductSnippet__name__w6hatm'}).text
    price = info.find('div', attrs={'class', 'snow-price_SnowPrice__mainS__jlh6el'}).text
    try:
        discount = info.find('div', attrs={'class', 'snow-price_SnowPrice__discountPercent__jlh6el'}).text
    except:
        discount = '-'
    try:
        sprice = info.find('div', attrs={'class', 'snow-price_SnowPrice__secondPrice__jlh6el'}).text
    except:
        sprice = '-'
    shop = info.find('div', attrs={'class', 'product-snippet_ProductSnippet__caption__w6hatm'}).text
    try:
        sold = info.find('div', attrs={'class', 'product-snippet_ProductSnippet__sold__w6hatm'}).text
    except:
        sold = '-'
    try:
        rating = info.find('div', attrs={'class', 'product-snippet_ProductSnippet__score__w6hatm'}).text
    except:
        rating = '-'
    try:
        delivery = info.find('div', attrs={'class', 'snow-price_SnowPrice__label__jlh6el'}).text
    except:
        delivery = '-'
    data = [description, price, discount, sprice, shop, sold, rating, delivery]
    for i in range(1, len(data) + 1):
        d = writer.cell(row, i)
        d.value = data[i - 1]
    row += 1
    sphone_table.loc[len(sphone_table)] = row
wb.save('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Table.xlsx')