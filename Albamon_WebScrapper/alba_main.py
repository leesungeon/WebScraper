import requests
from bs4 import BeautifulSoup

def get_company_page(URL):
  r = requests.get(URL)
  soup = BeautifulSoup(r.text, "html.parser")
  pagination = soup.find("div", {"id" : "MainSuperBrand"}).find_all("li", {"class" : "impact"})
  return pagination

def get_data(page):
  link = page.find("a", {"class" : "goodsBox-info"})["href"]
  company = page.find("a", {"class" : "goodsBox-info"}).find("span", {"class" : "company"}).string
  return {'link' : link, 'company' : company}


def get_result(URL):
  pagination = get_company_page(URL)
  datas = []
  
  for page in pagination:
    data = get_data(page)
    datas.append(data)
  return datas