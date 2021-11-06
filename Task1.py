import requests
from bs4 import BeautifulSoup
import json


# sample=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
# print(BeautifulSoup(sample.text, "html.parser"))
def scrape_top_list():
    scrape_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    scarpe_response=requests.get(scrape_url)
    # print(scarpe_response)
    
    soup=BeautifulSoup(scarpe_response.text,"html.parser")
    # print(soup)
 
    tr=soup.find("table",class_="table")
    # print(tr)
    td=tr.find_all("tr")
    # print(td[1])
  
    top_movies=[]
    
    for i in td[1:]:
        all=i.find_all("td")
        e=all[2].find("a")
        print(e['href'])
        

        movie_rank=i.find_all("td",class_="bold")
        # print(movie_rank)
        for j in movie_rank:
            ranks=j.get_text()
            # print(ranks)
 

        movie_rating=i.find_all("span",class_="tMeterScore")
        for rate in movie_rating:
            rates=rate.get_text()
            # print(rates)

        
        
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for review in movie_reviews:
            reviews=review.get_text()
            # print(reviews)

        movie_name=i.find("a",class_="unstyled articleLink")
        done=" ".join(movie_name.text.split())
        start=len(done)-5
        name=done[:start-1]
        #print(name)

        end=len(done)-1
        year=done[start:end]
       
        # print(year)
       
        
        movie_url=i.find("a", class_="unstyled articleLink")
        # print(movie_url)
        for i in movie_url:
            print(i)
        movie_link="https://www.rottentomatoes.com"+str(movie_url)
        details={"movie_rank":"","movie_rating":"","movie_name":"","movie_reviews":"","movie_url":"","year":""}
        details["movie_rank"]=ranks
        details["movie_rating"]=rates
        details["movie_name"]=name
        details["movie_reviews"]=reviews
        details["movie_url"]=movie_link
        details["year"]=year
        top_movies.append(details)
    # print(top_movies)

    with open("task1.json","w") as file:
        json.dump(top_movies,file,indent=4)
            
    return top_movies
scrape_top_list()


