from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
from tkinter.constants import END
from random import randint, shuffle, choice
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    letters_list = [choice(letters) for _ in range(nr_letters)]
    numbers_list = [choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [choice(symbols) for _ in range(nr_symbols)]

    hard_password_list = letters_list + numbers_list + symbols_list
    shuffle(hard_password_list)
    hard_password = "".join(hard_password_list)

    pass_input.insert(END, hard_password)
    copy(hard_password)
    messagebox.showinfo(title="", message="Copied to clipboard success!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    pwd = pass_input.get()

    if website == "" or email == "" or pwd == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {pwd} \nIs it ok to save?"
        )

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {pwd} \n")
                website_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=42)
website_input.grid(column=1, row=1, columnspan=2)
email_input = Entry(width=42)
email_input.insert(END, "test@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
pass_input = Entry(width=23)
pass_input.grid(column=1, row=3)

# Buttons
btn_gen_pass = Button(text="Generate Password", command=generate_password)
btn_gen_pass.grid(column=2, row=3)
btn_add = Button(text="Add", width=40, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
