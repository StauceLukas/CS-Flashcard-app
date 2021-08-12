from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

class QuizUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Flashcard App")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.canvas = Canvas(width=800, height=500, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.flashcard_photo = PhotoImage(file="Images/card_front.png")
        self.canvas.create_image(405, 257, image= self.flashcard_photo)
        self.canvas.grid(column=0, row=0)

        # Note - sukurti visiems constant kur keist
        self.question_theme = self.canvas.create_text(400, 120, text="What Is A Super-class?", fill='black', font=('Arial', 40, 'italic'))
        self.question_text = self.canvas.create_text(400, 280, text="A super class is the basis of all the classes. The object of the rest of the class "
                                                                    "has all the characteristics related to the superclass. ",
                                                     fill='black', font=('Arial', 20, 'bold'), width=500)

        self.window.mainloop()