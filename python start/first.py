print("hello word")
print("print('what to print')")
print("hello "+input("enter the name "))
excercise
a= input("a:")
b=input("b:")
c=a
a=b
b=c
print("a :"+ a  +"\n b :"+ b)

print("welcome to the generator.")
city=input( "in which city they grew up\n")
pet=input("which is your favourite pet\n")
print("your band name is " + city +" " + pet)
print("hello"[3])
num=len(input("enter your name hera \n"))
print(type(num))
new_num=str(num)

print("your name has "+" "+ new_num+"character")
number=input("enter the numbers")
print(type(number))
first=number[0]
second=number[1]
result=int(first)+int(second)
print(result)
weight=float(input("enter the weight in kg"))
height=float(input("enter the height in meter"))
bmi=int(weight/(height**2))
print(bmi) 
print(f"your weight is {weight}")
current_age=int("enter your current age") 
max_age=90
remaining_age=max_age-current_age
print(remaining_age)
days_rem=remaining_age*365
week_rem=remaining_age*52
months_rem=remaining_age*12
print(f"you have remaining {week_rem} weeks {days_rem} days{months_rem} months")

third days

height=int(input("enter  the height"))
if height>10:
    print("eligible")
    age=int(input("age:"))
    if age<=18:
        print("pay 7 rs")
    else:
        print("pay 50 rs")
else:
    print("not eiligible")
num3=int(input("enter the number"))
if num3%2==0:
    print("even")
else:
    print("odd")

 leap year challenge 
year=int(input("which year do you want to check"))
if year%4==0:
    if year % 100==0:
        if year%400==0:
            print("leapyear")
        else:
            print("not leapyear")
    else:
        print("leap year")
else:
    print("not a leapyear")

pizza challenge
print("welcome to pizzza deleviries")
size=input("what size do you want to ? s,m,l")
add_pepperoni=input("do you eant to add peperoni?y,n")
extra_cheese=input("do you want to add extra cheesea?y ,n")
bill=0
if size=="s":
    bill+=15
elif  size=="m":
    bill+=20
else:
    bill+=25
if add_pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
if extra_cheese=="y":
    bill+=1
print(f"tour final bill is {bill}") 

#buzzfeed example
name1=input("what is your name ")
name2=input("what is her name ")
combo=name1+name2
combined_string=combo.lower()
t=combined_string.count("t")
r=combined_string.count("r")
u=combined_string.count("u")
e=combined_string.count("e")
true=t+r+u+e
l=combined_string.count("l")
o=combined_string.count("o")
v=combined_string.count("v")
e=combined_string.count("e")
love=l+o+v+e
# lovecalc=str(true)+str(love) 
print(f"your love percentage is {lovecalc}")
if (lovecalc>10) and (locals<90):
    print("good choice")
elif(lovcalc>=40) and (lovecalc<=50):
    print("you are alright")
else:
    print("good")
print("welcome to the treasure hunt game please select right and left")
select=input("left or right").lower()
select2=input("swim or wait").lower()
color=input("select color red , blue ,yellow").lower()
if select=="left":
    if select2=="wait":
        if (color=="red")or (color=="blue"):
            print("game over")
        elif color=="yellow":
            print("game win")
    else:
        print("gameover")
else:
    print("game win")