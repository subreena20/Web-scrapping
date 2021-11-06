from Task1 import  scrape_top_list
import json

a=scrape_top_list()

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    print(years)
    final={}
    for i in years:
        final[i]=[]
        for k in movies:
            if k["year"]==i:
                final[i].append(k)

    with open("task2.json","w") as file:
        json.dump(final,file,indent=4)
        
    return final
            

        
print(group_by_year(a))
