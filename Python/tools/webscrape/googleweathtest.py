from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup as bs
import json


url = f"https://www.google.com/search?q=weather+London"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"

session = requests.Session()
session.headers['User-Agent'] = USER_AGENT
session.headers['Accept-Language'] = LANGUAGE
session.headers['Content-Language'] = LANGUAGE
html = session.get(url)
soup = bs(html.text, "html.parser")
days = soup.find("div", attrs={"id": "wob_dp"})
for day in days.findAll("div", attrs={"class": "wob_df"}):
    temp = day.findAll("span", {"class": "wob_t"})
    print(temp[2].text)