import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizzInterface():

    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz

        self.window = tkinter.Tk()
        self.window.title("Quizller")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",15,"bold"))
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white") 
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(150,125,text="", fill=THEME_COLOR, font=FONT, width=280, justify="center")

        self.true_label = tkinter.Label(text="TRUE", bg=THEME_COLOR, fg="white")
        self.true_label.grid(row=2, column=0)

        self.false_label = tkinter.Label(text="FALSE", bg=THEME_COLOR, fg="white")
        self.false_label.grid(row=2, column=1)

        right_image = tkinter.PhotoImage(file="images\\true.png")
        self.right_button = tkinter.Button(image=right_image, highlightthickness=0, borderwidth=0, command=self.right_button_click)
        self.right_button.grid(row=3, column=0)

        wrong_image = tkinter.PhotoImage(file="images\\false.png")
        self.wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=self.wrong_button_click)
        self.wrong_button.grid(row=3, column=1)
        
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):

        self.canvas.config(bg="white")
        self.score_label.configure(text=f"Score: {self.quiz.score}")
    
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
            self.right_button.config(state="active")
            self.wrong_button.config(state="active")

        else:
            self.canvas.itemconfig(self.question_text, text=f"Congratulations, you completed a quiz with a score {self.quiz.score}/{self.quiz.question_number}")


    def right_button_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_button_click(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.right_button.config(state="disable")
        self.wrong_button.config(state="disable")
        self.function = self.window.after(1000, self.get_next_question)
