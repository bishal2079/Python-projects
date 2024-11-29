from tkinter import *
import pandas as pd
import random 


BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}
try:
    data=pd.read_csv("data/words_to_learn")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000,func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    next_card()
    data.to_csv("data/words_to_learn",index=False)


    
window=Tk()
flip_timer=window.after(3000,func=flip_card)
window.title("Language converter")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526)
card_back_image=PhotoImage(file="images/card_back.png")
card_front_img=PhotoImage(file="images/card_front.png") 
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400, 150, text="title", font=("Ariel", 48, "italic"))
card_word=canvas.create_text(400,263,text="word", font=("Ariel", 60, "bold"))

cross_image=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1, column=0)

checked_image=PhotoImage(file="images/right.png")
known_button=Button(image=checked_image,highlightthickness=0,command=is_known)
known_button.grid(row=1, column=1)
next_card()
window.mainloop()
