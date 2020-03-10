import requests
import pandas as pd # we will analyze our data with pandas
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?textField1=28.54&textField2=-81.38')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast-body')

items = (week.find_all(class_ ="tombstone-container"))# here the class is html class_  
#Items are the forecast weather days  
"""
print(items[0])
print('\n',items[1])
print('\n',items[2])
print('\n',items[3])

print(items[0].find(class_ = 'period-name').get_text())
print('\n')
print(items[0].find(class_ = 'short-desc').get_text())
print('\n')
print(items[0].find(class_ = 'temp').get_text())
print('\n')

"""

period_names = [item.find(class_ = 'period-name').get_text() for item in items]
short_descriptions = [item.find(class_ = 'short-desc').get_text() for item in items]
temperatures = [item.find(class_ = 'temp').get_text() for item in items]
"""
print(period_names)
print('\n',short_descriptions)
print('\n',temperatures)

"""

weather_stuff = pd.DataFrame(
    {'period':period_names,
    'short_descriptions':short_descriptions,
    'temperatures':temperatures,
    }
)

print('\n', weather_stuff)

weather_stuff.to_csv('weather.csv') # we make csv file here with data above with help of pandas.

