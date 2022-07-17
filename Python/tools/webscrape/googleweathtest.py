from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup

s = HTMLSession()

location = "London"
url = f"https://www.google.com/search?q=weather+{location}"

r = s.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

temp = print(r.html.find('span#wob_tm', first=True).text)

r2 = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
soup = BeautifulSoup(r.text)
for image_src in soup.find_all("img"):
    print(image_src['src'])