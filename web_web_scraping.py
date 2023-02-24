from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Mathematics'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
#print(doc.prettify())

algebra = doc.find_all(text="Algebra")
parent = algebra[3].parent
#a = parent.find('a')
print(parent.string)

