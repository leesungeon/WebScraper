import requests
from bs4 import BeautifulSoup
from sympy import comp

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    pagination = soup.find("div", {"class" : "pagination"})
    spans = []    
    pages = pagination.find_all('a')

    for page in pages[:-1]:
        spans.append(int(page.string))
    max_page = spans[-1]
    return max_page

#Extract Data
def extract_job(html):
    title = html.find("h2", {"class" : "jobTitle"}).find("span", title=True).string
    company = html.find("span", {"class" : "companyName"}).string
    location = html.find("div", {"class" : "companyLocation"}).text
    job_id = html["data-jk"]

    return{'title' : title, 'company' : company, 'location' : location,
    "link" : f"https://www.indeed.com/viewjob?jk={job_id}"}

# Request Each Page
def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"SCRAPPING INDEED PAGE ------> {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}")
        result_encode = result.text.encode('utf8')
        soup = BeautifulSoup(result_encode, "html.parser")
        
        results = soup.find_all("a", {"class" : "tapItem"})
        
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_indeed_jobs(last_page)
    return jobs