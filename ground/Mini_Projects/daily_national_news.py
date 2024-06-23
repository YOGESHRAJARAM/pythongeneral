from distutils.filelist import findall
from logging import exception
from bs4 import BeautifulSoup
import requests

try:
    print(" ! -----Todays Top 25 National News-----! ")
    print("")
    responce=requests.get("https://indianexpress.com/section/india")
    soup= BeautifulSoup(responce.text,"html.parser")
    Today_=soup.find('div',class_="nation").find_all('div',class_="articles")
    #print(Today_)
    s=1
    for news in Today_:
        news_title = news.find('h2',class_='title').a.text
        news_Date = news.find('div',class_="date").text
        news_details = news.find("p").text
        
        
        print(s,news_title,"    (", news_Date,")")
        print("")
        print(news_details,)
       
        print("  ")
        s=s+1
        
        
        
except exception as e:
    print(e)