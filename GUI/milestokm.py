from tkinter import *

# Create the main window
window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_result_label.config(text=f"{km:.2f}")

# Entry for miles input
miles_input = Entry()
miles_input.grid(column=1, row=0)

# Label for "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label for "is equal to"
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

# Label for kilometers result
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# Label for "km"
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button to calculate
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

# Start the GUI loop
window.mainloop()

