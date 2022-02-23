from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_stackoverflow_jobs
from ConvertToCsv import convert_to_csv

#Indeed
indeed_jobs = get_indeed_jobs()

#StackOverflow
so_jobs = get_stackoverflow_jobs()

#Merge
jobs = so_jobs + indeed_jobs

#Convert
convert_to_csv(jobs)