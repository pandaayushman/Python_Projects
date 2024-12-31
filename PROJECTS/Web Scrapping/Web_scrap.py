import requests
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com/"

response = requests.get(url)

soup=BeautifulSoup(response.content, "html.parser")

for quote in soup.find_all("div",class_="quote"):

    words= quote.find("span",class_="text").text 
    writer= quote.find("small", class_="author").text 
    tags=[]
    for tag in quote.find_all("a",class_="tag"):
        tags.append(tag.text)
    print(f"Quote: {words}\nAuthor: {writer}\nTags: {', '.join(tags)}\n")
          
