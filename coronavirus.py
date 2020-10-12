# import necessary libraries

import csv
import requests
from bs4 import BeautifulSoup

# get the website html
html = requests.get('https://www.worldometers.info/coronavirus/').text

html_soup = BeautifulSoup(html, 'html.parser')  # create BeautifulSoup instance
rows = html_soup.find_all('tr') # filter all rows in the html tag

def extract_text(row, tag):
    element = BeautifulSoup(row, 'html.parser').find_all(tag)
    text = [col.get_text() for col in element]
    return text

# extract the first row which is header for data
heading = rows.pop(0)
heading_row = extract_text(str(heading), 'th')[1:9]

with open('corona.csv', 'w') as store:
    Store = csv.writer(store, delimiter=',')
    Store.writerow(heading_row)
    for row in rows:
        test_data = extract_text(str(row), 'td')[1:9]
        Store.writerow(test_data)