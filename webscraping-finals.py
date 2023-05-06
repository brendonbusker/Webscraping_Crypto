
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font

webpage = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url=webpage, headers= headers)

page = urlopen(req)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
print()

myclasses = ['MW 1:00 p.m.', 'MW 2:30 p.m.', 'TR 2:00 p.m.']

all_tables = soup.findAll('table')

finals_table = all_tables[1]

finals_rows = finals_table.findAll('tr')

#print(finals_rows[])
count = 1


#My way
'''
for i in range(0, len(finals_rows)):
    for j in range(0,len(myclasses)):
        if myclasses[j] in finals_rows[i].text.replace('\n', ' / '):
            print(f"Final #{count}")
            print(finals_rows[i].text)
            count+= 1
'''

#Bhojwani's way
for row in finals_rows:
    final = row.findAll('td')
    if final:

        myclass = final[0].text
        if myclass in myclasses:
            print(f'For class: {myclass} the final is scheduled for {final[1].text} at {final[2].text}')


#for i in range(0, len(finals_rows)):
#    print(finals_rows[i].text.replace('\n', ' / '))
