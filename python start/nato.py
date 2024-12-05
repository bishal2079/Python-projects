import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv") 
nato_dict = {row['letter']: row['code'] for _, row in data.iterrows()}
# print(nato_dict)
def generate_alphabet():
    User_input=input("enter the name\t").upper()
    try:
        User_input_list=[nato_dict[letter] for letter in User_input]
    except KeyError:
        print("invalid input! only letters valid")
        generate_alphabet()
    else:      
        print(User_input_list)


generate_alphabet()