# from Task1 import scrape_top_list
import json
from bs4 import BeautifulSoup
import requests 
with open("task1.json","r") as file:
    data=file.read()
    a=json.loads(data)
def get_movie_list_details(movies): 
    j=0
    list4=[]
    while j<len(movies):
        url=movies[j]["movie_url"]
        x=requests.get("https://www.rottentomatoes.com"+url)
        soup=BeautifulSoup(x.text,"html.parser")
        main=soup.find("div",class_="panel-body content_body")
        sub=main.find("ul",class_="content-meta info")
        all=sub.find_all("li",class_="meta-row clearfix")
        my_dict={}
        for i in all:
            my_dict[i.find("div",class_="meta-label subtle").get_text().strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n",'')
            
        list4.append(my_dict)
        j+=1
    # with open("my_file_5.json","w")as f:
    #    json.dump(list4,f,indent=4)
    print(list4) 
get_movie_list_details(a)
