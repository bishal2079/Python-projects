try:
    file=open("error_handeling\bishal.txt")
except FileNotFoundError:
    print("there was no such file")
    file=open("bishal.txt","w")
    file.write("aaaa")