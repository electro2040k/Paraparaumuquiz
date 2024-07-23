import tkinter as tk
from tkinter import messagebox

# Define the questions and answers
questions = [
    {
        "question": "What is the name of the beach in Paraparaumu?",
        "options": ["Waikanae Beach", "Paraparaumu Beach", "Raumati Beach", "Kapiti Beach"],
        "answer": "Paraparaumu Beach"
    },
    {
        "question": "Which island lies off the coast of Paraparaumu?",
        "options": ["Kapiti Island", "Mana Island", "Somes Island", "Matiu Island"],
        "answer": "Kapiti Island"
    },
    {
        "question": "What is the main shopping center in Paraparaumu?",
        "options": ["Lindale Village", "Coastlands", "Kapiti Landing", "The Hub"],
        "answer": "Coastlands"
    },
    {
        "question": "What famous golfer played at Paraparaumu Beach Golf Club in 2002?",
        "options": ["Tiger Woods", "Scottie Scheffler", "Rory McIlroy", "Ludvig Aberg"],
        "answer": "Tiger Woods"
    },
    {
        "question": "How many colleges are there from Raumati to Waikanae? ",
        "options": ["1", "4", "3", "2"],
        "answer": "2"
    },
    {
        "question": "What is the name of the local airport in Paraparaumu?",
        "options": ["Wellington Airport", "Paraparaumu Airport", "Kapiti Coast Airport", "Palmerston North Airport"],
        "answer": "Kapiti Coast Airport"
    },
    {
        "question": "What year was Paraparaumu college founded?",
        "options": ["1870", "1969", "1940", "1977"],
        "answer": "1977"
    },
    {
        "question": "What is the name of the train line that goes from Waikanae to Wellington?",
        "options": ["Melling Line", "Kapiti Line", "Wairarapa Line", "Hutt Valley Line"],
        "answer": "Kapiti Line"
    },
    {
        "question": "Which local attraction features a collection of cars and motorbikes?",
        "options": ["Lindale Village", "Southward Car Museum", "Coastlands", "Paraparaumu Beach"],
        "answer": "Southward Car Museum"
    },
    {
        "question": "What is the name of the highway that goes through Paraparaumu",
        "options": ["State Highway 1", "Main Road", "Kapiti Road", "Beach Road"],
        "answer": "State Highway 1"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wellington Quiz")
        self.root.geometry("500x400")

        self.current_question = 0
        self.score = 0

        self.setup_start_screen()

    def setup_start_screen(self):
        self.start_frame = tk.Frame(self.root)
        self.start_frame.pack(pady=20)

        self.instructions_label = tk.Label(self.start_frame, text="Enter the number of questions (5 to 10):")
        self.instructions_label.pack(pady=5)

        self.num_questions_entry = tk.Entry(self.start_frame)
        self.num_questions_entry.pack(pady=5)

        self.start_button = tk.Button(self.start_frame, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)

    def start_quiz(self):
        try:
            self.num_questions = int(self.num_questions_entry.get())
            if self.num_questions < 5 or self.num_questions > 10:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a number between 5 and 10.")
            return

        self.start_frame.destroy()
        self.questions = questions[:self.num_questions]
        self.setup_quiz_screen()

    def setup_quiz_screen(self):
        self.question_label = tk.Label(self.root, wraplength=400)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()

        self.option_buttons = [tk.Radiobutton(self.root, variable=self.options_var) for _ in range(4)]
        for btn in self.option_buttons:
            btn.pack(anchor='w')

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(self.root)
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}")
        self.score_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        self.options_var.set(None)
        for btn, option in zip(self.option_buttons, question_data["options"]):
            btn.config(text=option, value=option)

    def submit_answer(self):
        if self.options_var.get() == self.questions[self.current_question]["answer"]:
            self.score += 1
        self.current_question += 1
        self.score_label.config(text=f"Score: {self.score}")
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            self.show_final_result()

    def show_final_result(self):
        result_text = f"You got {self.score} out of {len(self.questions)} correct."
        result_text += "\nCongratulations, you passed!" if self.score >= len(self.questions) / 2 else "\nSorry, you failed."
        self.question_label.config(text=result_text)
        for btn in self.option_buttons:
            btn.pack_forget()
        self.submit_button.pack_forget()
        self.result_label.pack_forget()
        self.score_label.pack_forget()

# Run the Quiz Application
root = tk.Tk()
app = QuizApp(root)
root.mainloop() 
