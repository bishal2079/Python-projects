# import pandas as pd
# data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241121.csv ")
# print(data.columns)
# grey_squarrel=data[data["Primary Fur Color"]=="Gray"]
# red_squarrel=data[data["Primary Fur Color"]=="Cinnamon"]
# black_squarrel=data[data["Primary Fur Color"]=="Black"]
# print(grey_squarrel)
# print(len(grey_squarrel))
# print(len(red_squarrel))
# print(len(black_squarrel))

# data_dict={
#     "Fur Color":["Grey","Cinnamon","Red"],
#     "Cout":[grey_squarrel,red_squarrel,black_squarrel]
# } 
# df=pd.DataFrame(data_dict)
# df.to_csv("squirrel_csv") 

# list=[1,2,3,4,5,6,7,8,9,10,11]
# new_list =[n+1 for n in list]
# print(new_list)
# bin="abcdefghijklmnopqrstuvwxyz"
# new_bin=[i for i in bin]
# print(new_bin)
import random
list=[1,1,2,3,5,8,13,21,34,55]
new_list=[n for n in list if n%2 ==0]
print(new_list)
#dictionary comprehension
Name=["abb","bb","cc","dd","ee","ef","ff"]
scores=[1,1,2,3,5,8,13]
student_score={new_key:random.randint(1,100) for new_key in Name }
print(student_score)