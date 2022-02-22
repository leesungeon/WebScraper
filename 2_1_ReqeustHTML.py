import requests
from bs4 import BeautifulSoup

spans = []

# Request Page
r = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

# Extracting Page
soup = BeautifulSoup(r.text, "html.parser")
pagination = soup.find("div", {"class" : "pagination"})
pages = pagination.find_all('a')

for page in pages[:-1]:
    #spans.append(page.find("span").string)
    spans.append(int(page.string))
max_page = spans[-1]

# Result
print(spans)
print(max_page)