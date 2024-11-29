from tkinter import*
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list) 
    password_name.delete(0, END)  # Clear any previous password
    password_name.insert(0, password)  # Insert the new password
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_name.get()
    email = Email_name.get()
    passwords = password_name.get()

    new_data = {
        website: {
            "email": email,
            "passwords": passwords
        }
    }

    if len(website) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="OOPS", message="Please fill all the fields!")
    else:
        try:
            # Open the file in read mode to load existing data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Read existing data
        except FileNotFoundError:
            # If file doesn't exist, initialize an empty dictionary
            data = {}

        # Update data with new data
        data.update(new_data)

        # Save updated data back to the file
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)  # Write updated data

        # Clear input fields
        website_name.delete(0, END)
        password_name.delete(0, END)
        messagebox.showinfo(title="Success", message="Data saved successfully!")
#----------------------------find password----------------------------#

def find_password():
    website=website_name.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error",Message="no data file found")
    else:
        if website in data:
                email=data[website]["email"]
                password=data[website]["passwords"]
                messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="error",message="no information")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,bd=5,highlightthickness=2, highlightbackground="black")
Locker_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=Locker_img)
canvas.grid(row=0,column=1)


website=Label(text="Website:")
website.grid(row=1, column=0)

Usernam=Label(text="Username/Mail:")
Usernam.grid(row=2, column=0)

password=Label(text="Password:")
password.grid(row=3, column=0)

website_name=Entry(width=21, font=("Courier", 12))
website_name.grid(row=1,column=1)
website_name.focus()

Email_name=Entry(width=32, font=("Courier", 12))
Email_name.grid(row=2,column=1,columnspan=2)
Email_name.insert(0, "Bishalsharma037.com")

password_name=Entry(width=21, font=("Courier", 12))
password_name.grid(row=3,column=1)

generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

search_button=Button(text="search",width=13,command=find_password)
search_button.grid(row=1,column=2)


add_button=Button(text="Add",width=36, command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()