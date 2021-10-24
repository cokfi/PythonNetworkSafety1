#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://www.israelhayom.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "lxml")
print("------ISRAELHAYON.COM HEADLINES:--------")
for titles in soup.find_all(class_="jeg_post_title"):
	title = titles.a
	print(title.string)