import os
from alba_main import get_result
from alba_company import extract_jobs
from AlbaConvertToCsv import convert_to_csv

os.system("clear")
alba_url = "http://www.alba.co.kr"

def get_all_jobs(URL):
  results = get_result(URL)
  for result in results:
    print(f"---------SCRAPPING {result['company']} 채용공고 ----------")
    jobs = extract_jobs(result["link"])
    convert_to_csv(result["company"], jobs)

get_all_jobs(alba_url)