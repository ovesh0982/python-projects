import tkinter as tk
from tkinter import messagebox

# Quiz data (Questions, Options, and Correct Answer)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "C.S. Lewis"],
        "answer": "J.K. Rowling"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    }
]

# Initialize variables for tracking quiz state
current_question = 0
score = 0

# Function to load the next question
def load_question():
    global current_question
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])
        option1.config(text=question_data["options"][0])
        option2.config(text=question_data["options"][1])
        option3.config(text=question_data["options"][2])
        option4.config(text=question_data["options"][3])
    else:
        show_result()

# Function to check if the selected answer is correct
def check_answer(selected_option):
    global current_question, score
    correct_answer = questions[current_question]["answer"]
    selected_answer = selected_option.cget("text")
    if selected_answer == correct_answer:
        score += 1
    current_question += 1
    load_question()

# Function to show the result at the end
def show_result():
    result = f"Your score: {score}/{len(questions)}"
    messagebox.showinfo("Quiz Finished", result)
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("500x400")

# Question label
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
question_label.pack(pady=20)

# Option buttons
option1 = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda: check_answer(option1))
option1.pack(pady=5)

option2 = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda: check_answer(option2))
option2.pack(pady=5)

option3 = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda: check_answer(option3))
option3.pack(pady=5)

option4 = tk.Button(root, text="", font=("Arial", 14), width=30, command=lambda: check_answer(option4))
option4.pack(pady=5)

# Start the quiz
load_question()

# Run the Tkinter event loop
root.mainloop()
