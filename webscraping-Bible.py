import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = list(range(1,22))

random_chapter = random.choice(chapters)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

#prints title and proves if webpage is scrapable
print(soup.title.text)

page_verses = soup.findAll('div', class_='main')
#print('Chapter:', len(page_verses))
for verse in page_verses:
    verse_list = verse.text.split('.')

myverses = verse_list[:-5]

mychoice = random.choice(myverses)

print(f'Chatper: {random_chapter}')
print(mychoice)

import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)

TWnumber = '+17064206923'
myphone=   '+15126604148'

textmsg = client.messages.create(to=myphone, from_=TWnumber, body=mychoice)
print(textmsg.status)

