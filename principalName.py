import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def getPName(urlx):
    url1 = urlx


    page = requests.get(url1)

    soup = bs(page.content, 'html.parser')

    name = soup.find_all(attrs={'class': 'TD2'})

    for i in name:
        wrd = str(i)
        indx = (wrd.find('Dr'))

        if (indx != -1):
            zx = wrd[0:16]

            result = wrd
            vv = result.replace(zx, " ")
            vv1 = vv.replace('</td>', " ")
            return vv1

url = 'https://www.collegeadmission.in/GangarampurCollege/Gangarampur_College.shtml'


print(f"Name of the Principal is: {getPName(url)}")
