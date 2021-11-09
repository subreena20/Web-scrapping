from bs4 import BeautifulSoup
import json
import requests
movie_details=[]
def scrap_movie_details(link):
    dict={}
    link_data=requests.get(link)
    soup=BeautifulSoup(link_data.text,'html.parser')
    dict["name"]="Black panther"
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    dict["Bio"]=movie_bio

    rating=soup.find_all("div",class_="meta-label subtle")
    value=soup.find_all("div",class_="meta-value")

    for i in range(len(rating)):
        dict[str(rating[i].get_text().strip())[:-1]]=value[i].get_text().strip()
    movie_details.append(dict)
    with open("task4.json","w")as file:
        json.dump(movie_details,file,indent=4)

        

scrap_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")


