import tkinter as tk
from tkinter import messagebox, simpledialog

# Initial task list
task_list = [
    ("Buy groceries", "Pending"),
    ("Complete homework", "In Progress"),
    ("Clean the house", "Completed"),
    ("Read a book", "Pending")
]

# Function to refresh the listbox
def display_tasks():
    task_box.delete(0, tk.END)
    if not task_list:
        task_box.insert(tk.END, "No tasks available.")
    else:
        for idx, task in enumerate(task_list, 1):
            task_box.insert(tk.END, f"{idx}. {task[0]} - Status: {task[1]}")

# Add Task
def add_task():
    task_name = simpledialog.askstring("Add Task", "Enter task name:")
    if task_name:
        status = simpledialog.askstring("Task Status", "Enter status (default: Pending):") or "Pending"
        task_list.append((task_name, status))
        display_tasks()
        messagebox.showinfo("Success", f"Task '{task_name}' added with status '{status}'.")

# Remove Task
def remove_task():
    try:
        index = task_box.curselection()[0]
        removed_task = task_list.pop(index)
        display_tasks()
        messagebox.showinfo("Removed", f"Task '{removed_task[0]}' removed.")
    except:
        messagebox.showwarning("Warning", "Select a task to remove.")

# Update Task
def update_task():
    try:
        index = task_box.curselection()[0]
        new_name = simpledialog.askstring("Update Task", "Enter new task name:")
        new_status = simpledialog.askstring("Update Status", "Enter new status:")
        if new_name and new_status:
            old_task = task_list[index]
            task_list[index] = (new_name, new_status)
            display_tasks()
            messagebox.showinfo("Updated", f"Task '{old_task[0]}' updated to '{new_name}' with status '{new_status}'.")
    except:
        messagebox.showwarning("Warning", "Select a task to update.")

# Sort Tasks
def sort_tasks():
    task_list.sort(key=lambda task: task[0].lower())
    display_tasks()
    messagebox.showinfo("Sorted", "Tasks sorted alphabetically.")

# Exit App
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Task Manager")
root.geometry("600x600")
root.configure(bg="#2c3e50")

title = tk.Label(root, text="📝 Task Manager", font=("Helvetica", 28, "bold"), bg="#2c3e50", fg="#f1c40f")
title.pack(pady=20)

task_box = tk.Listbox(root, font=("Courier", 14), width=50, height=10, bg="#ecf0f1")
task_box.pack(pady=20)

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=10)

# Buttons
tk.Button(btn_frame, text="Add Task", command=add_task, width=15, bg="#27ae60", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Remove Task", command=remove_task, width=15, bg="#c0392b", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
tk.Button(btn_frame, text="Update Task", command=update_task, width=15, bg="#2980b9", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
tk.Button(btn_frame, text="Sort Tasks", command=sort_tasks, width=15, bg="#8e44ad", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Exit", command=exit_app, width=20, bg="#34495e", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

# Load initial tasks
display_tasks()

# Start main loop
root.mainloop()
