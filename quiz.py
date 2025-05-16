import tkinter as tk

# Main Window Setup
root = tk.Tk()
root.title("Python Quiz Game")
root.geometry("1200x800")
root.configure(bg="#1e1e2f")  # Dark purple background

score = 0
username = ""

# Global widget containers
current_widgets = []

# Fancy Title
title = tk.Label(root, text="🔥 PYTHON QUIZ CHALLENGE 🔥", font=("Segoe UI", 36, "bold"),
                 bg="#1e1e2f", fg="#fcd12a")
title.pack(pady=30)

# Entry Frame
entry_frame = tk.Frame(root, bg="#1e1e2f")
entry_frame.pack()

tk.Label(entry_frame, text="Enter Your Name:", font=("Segoe UI", 20), bg="#1e1e2f", fg="#ffffff").pack(pady=10)
entry = tk.Entry(entry_frame, font=("Segoe UI", 20), width=25, justify='center')
entry.pack(pady=5)

# Hoverable button generator
def make_button(master, text, command, color="#6a5acd"):
    btn = tk.Button(master, text=text, font=("Segoe UI", 16, "bold"), bg=color, fg="white",
                    relief="flat", width=20, height=2, command=command, cursor="hand2")
    btn.bind("<Enter>", lambda e: btn.config(bg="#836fff"))
    btn.bind("<Leave>", lambda e: btn.config(bg=color))
    return btn

# Increase score
def increase_score():
    global score
    score += 1

# Clear widgets from screen
def clear():
    for w in current_widgets:
        w.destroy()
    current_widgets.clear()

# Show final score
def show_result():
    clear()
    result_label = tk.Label(root, text=f"🎉 {username}, Your Score: {score}/10 🎉",
                            font=("Segoe UI", 28, "bold"), bg="#1e1e2f", fg="#00ffcc")
    result_label.pack(pady=50)
    current_widgets.append(result_label)

# Generic question display function
def show_question(qno, question, options, correct_index, next_func):
    clear()
    q_label = tk.Label(root, text=f"Question {qno}", font=("Segoe UI", 26, "bold"), bg="#1e1e2f", fg="#ffffff")
    q_label.pack(pady=10)
    current_widgets.append(q_label)

    question_label = tk.Label(root, text=question, font=("Segoe UI", 20), wraplength=1000, bg="#1e1e2f", fg="white")
    question_label.pack(pady=20)
    current_widgets.append(question_label)

    for i, opt in enumerate(options):
        btn = make_button(root, opt, lambda i=i: (increase_score() if i == correct_index else None, next_func())[1])
        btn.pack(pady=10)
        current_widgets.append(btn)

# All 10 questions
def q1(): show_question(1, "Which of them is a keyword in Python?", ["range", "def", "Val", "to"], 1, q2)
def q2(): show_question(2, "Which of the following is a built-in function?", ["factorial()", "print()", "seed()", "sqrt()"], 1, q3)
def q3(): show_question(3, "Which is not a core data type in Python?", ["Tuple", "Dictionary", "List", "Class"], 3, q4)
def q4(): show_question(4, "Who developed Python?", ["Wick Van Rossum", "Rasmus Lerdorf", "Guido Van Rossum", "Niene Stom"], 2, q5)
def q5(): show_question(5, "File extension for Python file?", [".python", ".p", ".pl", ".py"], 3, q6)
def q6(): show_question(6, "Function to get list length?", ["count()", "size()", "length()", "len()"], 3, q7)
def q7(): show_question(7, "Correct file extension?", [".pyt", ".pt", ".py", ".pyth"], 2, q8)
def q8(): show_question(8, "Keyword to define a function?", ["function", "define", "def", "fun"], 2, q9)
def q9(): show_question(9, "Type of [1, 23, 'hello', 1]?", ["List", "Dictionary", "Tuple", "Set"], 0, q10)
def q10(): show_question(10, "Used for comments in Python?", ["//", "/* */", "#", "<!-- -->"], 2, show_result)

# Start quiz
def start_quiz():
    global username
    username = entry.get().strip()
    if username:
        title.pack_forget()
        entry_frame.pack_forget()
        q1()
    else:
        entry.config(bg="#ffdddd")

start_button = make_button(root, "🚀 Start Quiz", start_quiz, color="#32cd32")
start_button.pack(pady=20)
current_widgets.append(start_button)

# Run app
root.mainloop()
