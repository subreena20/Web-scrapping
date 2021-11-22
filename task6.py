import json
import pprint
def analyse_movies_language():
    f=open("my_file_5.json","r")
    var=json.load(f)
    # pprint.pprint(var)
    list=[]
    for i in var:
        print(i)
        if (i["Original Language:"] not in list):
            list.append(i["Original Language:"])
    # print(list)
    dict={}
    list1=[]
    for j in list:
        # print(j)
        i=0
        count=0
        while i<len(var):
            # print(i)
            if j==var[i]["Original Language:"]:
                count+=1
            i+=1
        dict.update({j:count})
    # print(dict)
    list1.append(dict)
    # print(list1)
    with open("task6.json","w") as f:
        json.dump(list1,f,indent=4)

analyse_movies_language()