from tkinter import *
window=Tk()
window.title=("first gui")
window.minsize(width=800, height=500)
window.config(padx=25,pady=25)
my_labele=Label(text="i am a label",font=("Arial",24,"bold"))
my_labele.grid(row=0, column=0)
my_labele["text"]="hello beautiful"
 

def button_click():
    my_labele.config(text=input.get() )
button=Button(text="click me",command=button_click)
button.grid(row=1,column=0)

input=Entry(width=10) 
input.grid(row=2,column=2)
input.get() 

new_buttoon=Button(text="new")
new_buttoon.grid(row=0,column=3)
window.mainloop()
