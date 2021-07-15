"""
In this script scrape Data From this web page,
https://noonies.tech/award/top-programming-guru
the data collected is stored table of three columns
the channel Name, the channel url and the rank
"""

import re
from tqdm import tqdm
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless")

url = 'https://noonies.tech/award/top-programming-guru'
path = '/home/zaki/Downloads/chromedriver_linux64/chromedriver'  # path to chromedriver
driver = webdriver.Chrome(path, options=chrome_options)
driver.get(url)
time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all(href=re.compile('youtube.com'))
# print(results)
data = {'channelName': [], 'url': []}
for c in tqdm(results):
    # print(c)
    # print(c.text)
    # print(c.get('href'))
    data['channelName'].append(c.text)
    data['url'].append(c.get('href'))
    # break
    
df = pd.DataFrame.from_dict(data)
# adding ranking column
ranking = df.index + 1
df['rank'] = ranking 

print(df.head())

df.to_csv('data/top-programming-guru.csv', index=False)
