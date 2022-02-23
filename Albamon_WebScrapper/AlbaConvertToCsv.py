import csv

def convert_to_csv(company, jobs):
    if '/' in company:
      company = company.replace('/', ' ')
  
    file = open(f"{company}.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return