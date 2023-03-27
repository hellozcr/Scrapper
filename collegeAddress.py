import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def collegeAdd(urlx):
    url1 = urlx


    page = requests.get(url1)

    soup = bs(page.content, 'html.parser')
    add = soup.find(attrs={'class': 'col-md-4 col-sm-12 ftr-item'}).find_all('p')
 

    for i in range(1, 6):
        add2 = str(add[i])
        add3 = add2.replace('<p>', " ")
        add4 = add3.replace('</p>', " ")
        return add4


url = 'https://www.acharya.ac.in/'
print(f"College Address: {collegeAdd(url)}")
