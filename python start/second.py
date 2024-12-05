import random
total_sum=0
for even in range(0,101,2):
    total_sum+=even
print(total_sum)
for number in range(1,101):
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3==0:
        print("fizz")
    elif number%5==0:
        print("buzz")
    else:
        print(number)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
,'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
new_letters=int(input("how many letters"))
new_symbols=int(input("how many symbols"))
new_numbers=int(input("how many numbers"))
Passwords=""
for char in range(1,new_letters+1):
    Passwords+=random.choices(letters) 
for char in range(1,new_symbols+1):
    Passwords+=random.choices(symbols)
for char in range(1,new_numbers+1):
    Passwords+=random.choices(letters)
   