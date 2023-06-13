from bs4 import BeautifulSoup
import requests


req_data=requests.get("https://stackoverflow.com/questions/tagged/python")
data=BeautifulSoup(req_data.text,"html.parser")
quest=data.find("div",{"id":"questions"})
head=quest.find_all("div",{"class":"s-post-summary--content"})
for i in range(len(head)):
    head=quest.find_all("div",{"class":"s-post-summary--content"})[i]
    link=head.find("a",{"class":"s-link"})
    print(link.get_text())



