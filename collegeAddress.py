import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

def collegeAdd(urlx):
url1 = 'https://www.acharya.ac.in/'

page = requests.get(url1)

soup = bs(page.content,'html.parser')
add = soup.find(attrs={'class': 'col-md-4 col-sm-12 ftr-item'}).find_all('p')
# print(len(add))

for i in range(1,5):
    add2 = str(add[i])
    add3 = add2.replace('<p>'," ")
    add4 = add3.replace('</p>'," ")
    print(add4)

  
