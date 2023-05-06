import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://biblehub.com/asv/john/1.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

verses = soup.findAll('p', class_='reg')
#print(len(verses))
#for v in verses:
#    print(v.text)

'''
verse_list = [v.text.split('.') for v in verses]

print(verse_list)
print(len(verse_list))

print(random.choice(verse_list))

print(verse_list[0])
'''

verse_list = [v.text.split('.') for v in verses]

print(random.choice(random.choice(verse_list)))