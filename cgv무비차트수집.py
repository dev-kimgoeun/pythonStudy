import requests
from bs4 import BeautifulSoup

code = requests.get("http://www.cgv.co.kr/movies/?lt=1&ft=0")
#print(code.text)

soup = BeautifulSoup(code.text, "html.parser")
#print(soup)

title=soup.select("strong.title")
for i in range(len(title)) :
    print(f"{i+1}위 : {title[i].text}")