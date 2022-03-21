import requests
from bs4 import BeautifulSoup

url = 'https://ng.indeed.com/jobs?q=python%20developer&l=Lagos&vjk=15a2d3eab4e47e5a'
page = requests.get(url)
from csv import writer

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='job_seen_beacon')

with open('Jobs.csv', 'w', newline='', encoding='utf8') as f:
    mywriter = writer(f)
    header = ['title', 'company']
    mywriter.writerow(header)


for result in results:
    title = result.find('h2', class_='jobTitle').text
    company = result.find('span', class_='companyName').text

    info = [title, company]
    mywriter.writerow(info)

    '''
    print(f'Position: {title.text}')
    print(f'Company: {company.text}', end='\n'*2)
    '''


