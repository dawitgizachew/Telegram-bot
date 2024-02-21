# pip install bs4
# pip install requests

import requests
from bs4 import BeautifulSoup
url = 'https://amharic.voanews.com/ethiopia'

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

post = soup.find("div", class_="content")

title = post.find("h4", class_="media-block__title media-block__title--size-1 media-block__title--io").text.strip()
print(title)
