from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import json

s = HTMLSession()

location = "London"
url = f"https://www.google.com/search?q=weather+{location}"

r = s.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

r2 = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
soup = BeautifulSoup(r.content, "html.parser")

temp = soup.find('text', 'wob_t wob_gs_l3')

r.html.render(sleep=10)

weather = r.html.find('wob_t.wob_gs_l0', first=True)
print(weather)


svg = r.html.find('svg#wob_gsvg', first=True)
print(svg.attrs)