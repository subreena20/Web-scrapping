import json 
import pprint


def final(text):
    return "".join(text.split())

def analyse_movies_directors():
    f=open("my_file_5.json","r")
    var=json.load(f)
    # pprint.pprint(var)
    list=[]
    for i in var:
        # print(i)
        f=final(i["Director:"])
        if f not in list:
            list.append(f)
        
    list1=[]
    dict={}
    for i in list:
        j=0
        count=0
        while j<len(var):
            if i==final(var[j]["Director:"]):
                count+=1
            j+=1
            dict.update({i:count})
    # print(dict)
    list1.append(dict)
    # print(list1)
    with open("task7.json","w") as file:
        json.dump(list1,file,indent=2)

            
analyse_movies_directors()