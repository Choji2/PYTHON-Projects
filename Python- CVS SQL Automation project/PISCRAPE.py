# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 12:02:54 2022

@author: vac59186
Used for scraping Lexmark and Zebra printer's internal web interface.
"""

def _zebraRequest(urlB):
    
    import requests 
    from bs4 import BeautifulSoup
    arry = []
    url = urlB
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    group = soup.find_all("center")
    
    list_3 = group[0].find_all('h2')
    name_ = list_3[0].text.strip()
    arry.append(name_)
    
    list_2 = group[0].find_all('h1')
    type_ = list_2[0].text.strip()
    arry.append(type_)
    
    list_1 = group[0].find_all('h3')
    status = list_1[0].text.strip()
    arry.append(status)
    
    return arry

def _lexmarkRequest(urlB):
    
    import requests 
    import time
    from bs4 import BeautifulSoup
    arry = []
    url = urlB
    page = requests.get(url, timeout=None)
    time.sleep(3)
    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup)
    
    
    divs_ = soup.find_all('div', class_='infoarea')
    
    list_1 = divs_[0].find_all('span')
    list_2 = [ h2_element.parent for h2_element in list_1]
    #print(list_2)
    status_ = soup.find_all("span", class_="statusline")
    print(status_)
    
        
    location_ = list_2[4].text.strip()
    arry.append(location_)
    
    contact_ = list_2[2].text.strip()
    arry.append(contact_)

_lexmarkRequest('http://10.132.2.60/')    
    