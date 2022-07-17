from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

# Get Data with requests-html
url = "https://www.google.com/search?q=weather+London"
r = HTMLSession().get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})

# Define Parser
soup = bs(r.text, 'html.parser')
# Parse Text
title = soup.find_all('title').text
print(title)
# Parse Image

# Parse link