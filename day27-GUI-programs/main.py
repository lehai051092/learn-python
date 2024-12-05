from tkinter import Tk, Entry, Label, Button, END

def convert_miles_to_km():
    miles = int(input_mile.get())
    km = round(miles * 1.609344)
    label_convert.config(text=f"{km}")

window = Tk()
window.minsize(width=1024, height=768)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input_mile = Entry(width=10)
input_mile.insert(END, string="0")
input_mile.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal_to = Label(text="is equal to")
label_equal_to.grid(column=0, row=1)

label_convert = Label(text="0")
label_convert.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)

window.mainloop()