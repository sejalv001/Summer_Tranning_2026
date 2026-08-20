import tkinter as tk
from tkinter import messagebox

# Quiz Questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Lucknow"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for Python?",
        "options": ["Java", "Python", "C++", "Ruby"],
        "answer": "Python"
    },
    {
        "question": "2 + 2 =?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who made Python?",
        "options": ["Elon Musk", "Guido van Rossum", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    }
]

score = 0
current_q = 0

# Main window
root = tk.Tk()
root.title("Quiz Game App")
root.geometry("500x350")
root.config(bg="#E3F2FD")

# Functions
def check_answer(selected):
    global score, current_q
    if selected == questions[current_q]["answer"]:
        score += 1
        messagebox.showinfo("Result", "Correct! 🎉")
    else:
        messagebox.showwarning("Result", f"Wrong! Correct answer: {questions[current_q]['answer']}")

    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Over", f"Your Final Score: {score}/{len(questions)}")
        root.destroy()

def load_question():
    q_label.config(text=questions[current_q]["question"])
    for i, btn in enumerate(buttons):
        btn.config(text=questions[current_q]["options"][i])

# UI Elements
q_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#E3F2FD", wraplength=400)
q_label.pack(pady=20)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=30,
                    command=lambda i=i: check_answer(questions[current_q]["options"][i]),
                    bg="#2196F3", fg="white")
    btn.pack(pady=5)
    buttons.append(btn)

# Load first question
load_question()

root.mainloop()