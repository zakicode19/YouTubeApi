'''
In this script scrape Data From this web page,
the data collected is table of youtube channels and their urls

'''

import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless")

url = 'https://noonies.tech/award/top-programming-guru'
path = '' # path to chromedriver
driver = webdriver.Chrome(path, options=chrome_options)
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all(href=re.compile('youtube.com'))
# print(results)
data = {'channelName': [], 'link': []}
for c in results:
    print(c)
    print(c.text)
    print(c.get('href'))
    data['channelName'].append(c.text)
    data['link'].append(c.get('href'))
    #break
    
df = pd.DataFrame.from_dict(data)
df.to_csv('top-programming-guru.csv')
