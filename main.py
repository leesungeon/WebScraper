from indeed import extract_indeed_pages, extract_indeed_jobs

last_pages = extract_indeed_pages()
INDEED = extract_indeed_jobs(last_pages)
print(INDEED)