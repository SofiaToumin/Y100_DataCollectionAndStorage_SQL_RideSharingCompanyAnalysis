#Write a code to parse the data on weather in Chicago in November 2017 from the website:
#[https://code.s3.yandex.net/data-analyst-eng/chicago_weather_2017.html)
#The name of the DataFrame should be weather_records, and it should be specified
#when you search: attrs={"id": "weather_records"} .
#Print the DataFrame in its entirety.

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://code.s3.yandex.net/data-analyst-eng/chicago_weather_2017.html'
req_text = requests.get(url).text
soup = BeautifulSoup(req_text, 'lxml')

table = soup.find('table',attrs={'id':'weather_records'})
#print(table)

heading_table = []
for row in table.find_all('th'):
    heading_table.append(row.text)
#print(heading_table)

content = []
for row in table.find_all('tr'):
    if not row.find_all('th'):
        content.append([element.text for element in row.find_all('td')])
#print(content)

weather_records = pd.DataFrame(content, columns=heading_table)
print(weather_records)
