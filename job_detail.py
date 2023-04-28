import requests
from bs4 import BeautifulSoup
import lxml

result = requests.get('https://wuzzuf.net/jobs/p/xDDQRHJRw9kb-Junior-Odoo-Python-Developer-Ulemt-Cairo-Egypt?o=2&l=sp&t=sj&a=python%20developer|search-v3|hpb')
src = result.content
soup = BeautifulSoup(src, 'lxml')
print(soup.find('section',{'class':'css-dy1y6u'}))
Job_Categories = soup.find('span',{'class':'css-158icaa'})
#print(Job_Categories)
job_salary = soup.find('div',{'class':'css-rcl8e5'})
#print(job_salary)
job_discribtions = soup.find('div', class_='css-1uobp1k')
#salary.append(job_salary)
    #print(job_discribtions)
#print(salary)    