import os.path
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
flip_timer = None

# Fetch Data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origin_data = pandas.read_csv("data/japanese_words.csv")
    to_learn = pandas.DataFrame(origin_data).fillna("").to_dict(orient="records")
else:
    to_learn = pandas.DataFrame(data).fillna("").to_dict(orient="records")

# Logic
def next_card():
    global flip_timer, current_card
    if flip_timer:
        window.after_cancel(flip_timer)

    if len(to_learn) > 0:
        current_card = choice(to_learn)
        kanji = current_card.get('jp_kanji', "")
        hira_kata = current_card.get('jp_hira_or_kata', "")

        canvas.itemconfig(bg_image, image=img_front)
        canvas.itemconfig(language_text, text="Japanese", fill="black")
        canvas.itemconfig(kanji_text, text=kanji, fill="black")
        canvas.itemconfig(hira_kata_text, text=hira_kata, fill="black")

        flip_timer = window.after(3000, func=flip_card)
    else:
        if os.path.exists("data/words_to_learn.csv"):
            os.remove("data/words_to_learn.csv")
        messagebox.showinfo("Chúc mừng!", "Bạn đã học hết tất cả các từ!")
        original_data = pandas.read_csv("data/japanese_words.csv")
        to_learn.extend(original_data.to_dict(orient="records"))
        next_card()


def flip_card():
    canvas.itemconfig(bg_image, image=img_back)
    canvas.itemconfig(language_text, text="Vietnamese", fill="white")
    canvas.itemconfig(kanji_text, text=current_card.get("vi", ""), fill="white")
    canvas.itemconfig(hira_kata_text, text="", fill="white")

def is_known():
    if len(to_learn) > 0:
        to_learn.remove(current_card)
        if len(to_learn) > 0:
            data = pandas.DataFrame(to_learn)
            data.to_csv("data/words_to_learn.csv", index=False)
        else:
            if os.path.exists("data/words_to_learn.csv"):
                os.remove("data/words_to_learn.csv")
    next_card()

# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

img_front = PhotoImage(file="images/card_front.png")
img_back = PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(400, 263, image=img_front)

language_text = canvas.create_text(400, 150, text="", font=("Noto Sans JP", 30, "italic"))

kanji_text = canvas.create_text(400, 243, text="", font=("Noto Sans JP", 40, "bold"))

hira_kata_text = canvas.create_text(400, 313, text="", font=("Noto Sans JP", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

img_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=next_card)
btn_wrong.grid(column=0, row=1)

img_right = PhotoImage(file="images/right.png")
btn_right = Button(image=img_right, highlightthickness=0, command=is_known)
btn_right.grid(column=1, row=1)

next_card()

window.mainloop()
