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
        self.canvas.grid(column=0, row=0, columnspan=3)

        # Note - sukurti visiems constant kur keist
        self.question_theme = self.canvas.create_text(400, 120, text="What Is A Super-class?", fill='black', font=('Arial', 40, 'italic'))
        self.question_text = self.canvas.create_text(400, 280, text="A super class is the basis of all the classes. The object of the rest of the class "
                                                                    "has all the characteristics related to the superclass. ",
                                                     fill='black', font=('Arial', 20, 'bold'), width=500)


        self.flip_photo = PhotoImage(file='Images/button_photos/flip_card.png')
        self.knew_photo = PhotoImage(file='Images/button_photos/knew.png')
        self.next_photo = PhotoImage(file='Images/button_photos/next_card.png')

        self.flip_card_btn= Button(image=self.flip_photo, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.knew_card_btn = Button(image=self.knew_photo, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.next_card_btn = Button(image=self.next_photo, highlightthickness=0, bg=BACKGROUND_COLOR)

        self.flip_card_btn.grid(column=0, row=1, pady=50)
        self.knew_card_btn.grid(column=1, row=1)
        self.next_card_btn.grid(column=2, row=1)

        self.window.mainloop()