
import pandas

data= pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251219.csv")
g=0
c=0
b=0


lis=data["Primary Fur Color"].to_list()
for i in lis:
    if i=="Gray":
        g+=1
    elif i=="Cinnamon":
        c+=1
    elif i=="Black":
        b+=1


data_dict={

    "fur":["","",""],
    "color":["Gray","Cinnamon","Black"],
    "count":[g,b,c]


}
dat=pandas.DataFrame(data_dict)
dat.to_csv("new_dat.csv")







