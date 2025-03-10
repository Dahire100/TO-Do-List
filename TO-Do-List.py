import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import pyttsx3
import openai
import os
from pathlib import Path

engine = pyttsx3.init()

api_key = os.getenv("OPENAI_API_KEY")

def load_tasks():
    tasks = []
    file_path = Path("To-Do-List.txt")
    if file_path.exists():
        with file_path.open("r") as f:
            for line in f:
                try:
                    task, done = line.rsplit(" - ", 1)
                    done = done.strip() == "done"
                    tasks.append({"task": task, "done": done})
                except ValueError:
                    continue  
    return tasks

def save_tasks(tasks):
    with Path("To-Do-List.txt").open("w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['task']} - {status}\n")

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def mark_done():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[index]["done"] = True
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Select a task to mark as done!")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        del tasks[index]
        save_tasks(tasks)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

def chatbot_response():
    user_input = chatbot_entry.get()
    if user_input:
        if not api_key:
            chatbot_output.configure(text="Error: Set OPENAI_API_KEY.")
            return
        try:
            client = openai.OpenAI(api_key=api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            reply = response.choices[0].message.content.strip()
            chatbot_output.configure(text=reply)
        except Exception as e:
            chatbot_output.configure(text=f"Error: {e}")

tasks = load_tasks()
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("To-Do List with AI Chatbot")
root.geometry("500x550")

task_entry = ctk.CTkEntry(root, placeholder_text="Enter Task...", width=300)
task_entry.pack(pady=10)

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=5)

ctk.CTkButton(button_frame, text="Add Task", command=add_task).grid(row=0, column=0, padx=5)
ctk.CTkButton(button_frame, text="Mark Done", command=mark_done).grid(row=0, column=1, padx=5)
ctk.CTkButton(button_frame, text="Delete", command=delete_task).grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

chatbot_entry = ctk.CTkEntry(root, placeholder_text="Ask AI...", width=300)
chatbot_entry.pack(pady=10)
ctk.CTkButton(root, text="Chat", command=chatbot_response).pack()

chatbot_output = ctk.CTkLabel(root, text="", wraplength=400)
chatbot_output.pack(pady=5)

update_task_list()

root.mainloop()
