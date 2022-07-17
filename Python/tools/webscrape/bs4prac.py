from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession


# Get Data with requests-html
url = "https://www.google.com/search?q=weather+London"
r = HTMLSession().get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
# Define Parser
soup = bs(r.text, 'html.parser')

# Parse Text

lis = soup.find_all('li')
print(lis[0].text)

# Parse Image

image = soup.find('img', {'class': 'qIBnUc'})
print(image['src'])

# Parse link

link = soup.find_all('a')
print(link[2]['href'])