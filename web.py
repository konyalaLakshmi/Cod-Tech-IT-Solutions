import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://weather.com/en-IN/weather/today/l/dec09af69460c3be8472e727c60100f44b81d2e3aff28b127d003ee0e4398594'

# Fetch the HTML content from the URL
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the temperature element
temperature_element = soup.find(class_='CurrentConditions--tempValue--MHmYY')

# Find the weather phrase element
weather_phrase_element = soup.find(class_='CurrentConditions--phraseValue--mZC_p')

# Find the timestamp element
timestamp_element = soup.find(class_='CurrentConditions--timestamp--1ybTk')

# Extract temperature, weather phrase, and timestamp
temperature = temperature_element.text if temperature_element else 'Temperature not available'
weather_phrase = weather_phrase_element.text if weather_phrase_element else 'Weather phrase not available'
timestamp = timestamp_element.text if timestamp_element else 'Timestamp not available'

# Extract date from the timestamp
date = datetime.now().strftime('%Y-%m-%d')

# Print the extracted information

print(f'Temperature in Hyderabad, Telangana: {temperature}')
print(f'Weather Phrase: {weather_phrase}')
print(f'Date: {date}')
print(f'Timestamp: {timestamp}')
