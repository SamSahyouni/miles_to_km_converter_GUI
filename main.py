from tkinter import *


# calculate function
def calculate():
    miles_input = entry.get()
    km_output = int(miles_input) * 1.609
    answer_label.config(text=km_output)

    
# make the window
window = Tk()
window.title("Miles to Km Converter")
window.wm_minsize(height=200,width=300)
window.config(padx=40,pady=40)

# make the entry box
entry = Entry(width=10,font=("Arial",12))
entry.grid(column=1, row=0)

# make the static labels
label1 = Label(text="is equal to",font=("Arial",12))
label1.grid(column=0, row=1)
label2 = Label(text="Miles",font=("Arial",12))
label2.grid(column=2, row=0)
label3 = Label(text="Km",font=("Arial",12))
label3.grid(column=2, row=1)

# make the answer label
answer_label = Label(text="0",font=("Arial",12))
answer_label.grid(column=1, row=1)


# make the button
button = Button(text="Calculate",font=("Arial",12),command=calculate)
button.grid(column=1, row=2)
window.mainloop()