import requests

from bs4 import BeautifulSoup

import pandas as pd
url = "https://www.amazon.in/s?k=mobiles&crid=YWGHDY2ESUI6&sprefix=mobiles%2Caps%2C322&ref=nb_sb_noss_2"

header={"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

# now I am sending the request to get the response from Amazon.com

response= requests.get(url,headers=header)

if response.status_code==200:
    print("Response received ! ")
else:
    print("Response receive Failed")

soup = BeautifulSoup(response.content, "html.parser")


mobile_names=soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")

names=[]
for name in mobile_names:
    names.append(name.text.strip())

prices= soup.find_all("span", class_="a-price-whole")

pricelist=[]

for price in prices:
    pricelist.append(price.text.striip())

info={"Model name": names, "Price": pricelist}

df = pd.DataFrame(info)

df.to_csv("web_scrap.csv", index=False)

print("Data saved to the respective CSV file. Thanks !")