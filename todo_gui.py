import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        listbox.insert(tk.END, f"{i+1}. {task}")

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

app = tk.Tk()
app.title("To-Do List")

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

add_btn = tk.Button(app, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(app, width=50)
listbox.pack(pady=10)

delete_btn = tk.Button(app, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

app.mainloop()
