import math
def greet(name, location):
    print(f"hello world {name} ")
    print(f"this is the python begning {location}")
    print("have a good day a head")

greet("bishal","kathmandu")

def paint_calc(height,width,cover):
    area=height*width
    number_can=math.ceil(area/cover)
    print(f"your required can is {number_can}")

test_height=float(input("enter the height"))
test_width=float(input("enter the width"))
test_cover=float(input("enter the cover"))
paint_calc(height=test_height,cover=test_cover,width=test_width)

#prime number checker 
def prime_checker(number):
    is_prime=True
    for i in range(2, number):
       if number % i==0:
        is_prime=False
    if is_prime:
        print("prime number ")
    else:
        print(" not prime")
n=int(input("enter the number to be checked "))
prime_checker(number=n)
    