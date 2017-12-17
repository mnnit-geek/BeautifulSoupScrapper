#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:47:27 2017

@author: Aman
"""

# Used to extract DOM
import requests
# Used to parse DOM
from bs4 import BeautifulSoup
# Used to create data frame
import pandas as pd

# Page you want to parse
PAGE = 'https://coinmarketcap.com/'
dfColumns = []
data = []

# Collect and parse first page
page = requests.get(PAGE)
soup = BeautifulSoup(page.text, 'html.parser')

# Extract table header from DOM
tableHead = soup.body.table.thead.find_all('th')

# Get value of individual headers
for header in tableHead:
    dfColumns.append(header.get_text())

# Extract table body from DOM
tableBody = soup.body.table.tbody

# Extract rows from body
rows = tableBody.find_all('tr')

# Parsing individual rows
for val in rows:
    data_row = []
    for cols in val.find_all('td'):    
        data_row.append(cols.get_text().replace('\n','').replace(' ','').strip())
    data.append(data_row)

# Collating data in DataFrame
df = pd.DataFrame(data, columns=dfColumns).to_string(index=False)
print (df)

