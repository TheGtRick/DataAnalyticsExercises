from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import numpy as np
from selenium.webdriver.chrome.service import Service
import time
service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-quic')
driver = webdriver.Chrome(service=service, options=options)
URL = "https://www.worldometers.info/coronavirus/"
driver.get(URL)
time.sleep(3)
content = driver.page_source
soup = bs(content, 'html.parser')
data = []
for tr in soup.table.find_all('tr', attrs={'data-continent': None}):
    data.append([td.text for td in tr.find_all('td')])
table = pd.DataFrame(columns=['Country name', 'Total cases', 'Total deaths', 'Total recovered', 'Active cases', 'New cases', 'New deaths', 'Total tests', 'Population'])
for info in data:
    try:
        name = info[1]
    except:
        name = np.nan
    try:
        tcases = info[2]
    except:
        tcases = np.nan
    try:
        tdeaths = info[4]
    except:
        tdeaths = np.nan
    try:
        trecover = info[6]
    except:
        trecover = np.nan
    try:
        acases = info[8]
    except:
        acases = np.nan
    try:
        ncases = info[3]
    except:
        ncases = np.nan
    try:
        ndeaths = info[5]
    except:
        ndeaths = np.nan
    try:
        ttests = info[12]
    except:
        ttests = np.nan
    try:
        population = info[14]
    except:
        population = np.nan
    table.loc[len(table)] = [name, tcases, tdeaths, trecover, acases, ncases, ndeaths, ttests, population]
table.to_csv('Lab 7\\Table.csv')