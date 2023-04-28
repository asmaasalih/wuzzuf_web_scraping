import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest


job_title = []
company_name = []
location_name = []
skills = []
job_links = []
salary = []

results = requests.get('https://wuzzuf.net/search/jobs/?q=python+developer&a=hpb')
src = results.content
soup = BeautifulSoup(src, 'lxml')

jobs_titles = soup.find_all("h2", {'class':"css-m604qf"})
company_names = soup.find_all("a", {'class':"css-17s97q8"})
locations = soup.find_all("span", {'class':"css-5wys0k"})
job_skills = soup.find_all("div", {'class':"css-y4udm8"})
    
for i in range(len(jobs_titles)):
    job_title.append(jobs_titles[i].text)
    job_link = 'https://wuzzuf.net' + jobs_titles[i].find('a').attrs['href']
    job_links.append(job_link)
    company_name.append(company_names[i].text)
    location_name.append(locations[i].text)
    skills.append(job_skills[i].text)
   

file_list = [job_title,company_name,location_name,skills,job_links,salary]
exported = zip_longest(*file_list)
with open('jobs.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Company Name', 'Location', 'Skills', 'Job Links'])
    writer.writerows(exported)


