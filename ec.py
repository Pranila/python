import requests
from bs4 import BeautifulSoup

url="http://whatismyip.host/"
get_l=requests.get(url,headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"})
#print(get_l.content)
v=BeautifulSoup(get_l.text,'html.parser')
t=v.find_all(class_="ipaddress")[0].text
#p=v.find_all(class_='ipaddress')
print(t)
