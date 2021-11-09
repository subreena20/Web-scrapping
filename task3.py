import json
from Task1 import scrape_top_list

a=scrape_top_list()
def group_by_decade(movies):
    dict={}
    list1=[]
    for i in movies:
        mod=int(i["year"])%10
        decade_year=int(i["year"])-mod
        if decade_year not in list1:
            list1.append(decade_year)
    list1.sort()
    # print(list1)
    for i in list1:
        movie_list=[]
        for j in movies:
            if int(j["year"])>=i and int(j["year"])<=i+10:
                movie_list.append(j)
                dict[i]=movie_list
            # print(movie_list)
            # print(dict)
                with open ("task3.json","w") as f:
                    json.dump(dict,f,indent=4)

group_by_decade(a)
