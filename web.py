from bs4 import BeautifulSoup

with open('index.html','r') as f:
    doc = BeautifulSoup(f,'html.parser')

#tag = doc.title
#tag.string ='hello'

tag = doc.find_all('p')[0]
b=tag.find_all('b')
print(b)