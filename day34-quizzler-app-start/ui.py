from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.timer = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Amazon acquired Twitch in August 2014 for $970 million dollars",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.handle_true_answer)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.handle_false_answer)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            )

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.configure(bg="white")
        self.get_next_question()

    def handle_true_answer(self):
        if self.timer:
            self.window.after_cancel(self.timer)

        self.quiz.check_answer("True")
        self.canvas.configure(bg="green")
        self.timer = self.window.after(1000, self.update_score)

    def handle_false_answer(self):
        if self.timer:
            self.window.after_cancel(self.timer)

        self.quiz.check_answer("False")
        self.canvas.configure(bg="red")
        self.timer = self.window.after(1000, self.update_score)
