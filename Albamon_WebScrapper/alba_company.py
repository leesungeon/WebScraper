import requests
from bs4 import BeautifulSoup

def extract_jobs(link):
  jobs = []
  r = requests.get(link)
  r_encoding = r.text.encode('utf8')
  soup = BeautifulSoup(r_encoding, "html.parser")
  results = soup.find("tbody").find_all("tr", attrs={"id": False, "class": True})
  
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs


def extract_job(result):
  place = result.find("td", {"class" : "local first"})
  title = result.find("span", {"class": "company"})
  time = result.find("span", {"class": "time"})
  pay = result.find("td", {"class": "pay"})
  date = result.find("td", {"class" : "regDat last"})

  if place is not None:
    place = place.text.replace("\xa0","")
  if title is not None:
    title = title.text
  if time is not None:
    time = time.text
  if pay is not None:
    pay = pay.text
  if date is not None:
    date.text
  return{'place' : place, 'title' : title, 'time' : time, "pay" : pay, "date" : date}